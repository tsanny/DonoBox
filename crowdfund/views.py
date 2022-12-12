from .forms import CrowdfundForm, DonationForm
from .models import Crowdfund, Donation
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from notification.models import Notification
from pytz import timezone
import json

def show_crowdfunds(request):
    context = {
        "logged_in": request.user.is_authenticated,
        "user": request.user,
        "role": getattr(getattr(request.user, "userprofile", None), "role", None)
        }
    if context["role"] == "Fundraiser":
        return render(request, "crowdfunds_fundraiser.html", context)
    return render(request, "crowdfunds_donator.html", context)

@login_required(login_url="/autentikasi/")
def show_crowdfund(request, id):
    context = {
        "id": id,
        "role": request.user.userprofile.role
        }
    if context["role"] == "Fundraiser":
        return render(request, "crowdfund_fundraiser.html", context)
    return render(request, "crowdfund_donator.html", context)

def show_crowdfunds_json_ongoing(request):
    crowdfunds = Crowdfund.objects\
        .filter(deadline__gt=datetime.now().replace(tzinfo=timezone("UTC")))\
        .filter(collected__lt=F("target"))
    return HttpResponse(serializers.serialize("json", crowdfunds), content_type="application/json")

@login_required(login_url="/autentikasi/")
def show_crowdfunds_json_by_me(request):
    crowdfunds = Crowdfund.objects.filter(fundraiser__user=request.user)
    return HttpResponse(serializers.serialize("json", crowdfunds), content_type="application/json")

@login_required(login_url="/autentikasi/")
def show_crowdfund_json(request, id):
    crowdfund = Crowdfund.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", crowdfund), content_type="application/json")

@login_required(login_url="/autentikasi/")
def show_donations_json_by_fund(request, id):
    donations = Donation.objects.filter(crowdfund__pk=id)
    return HttpResponse(serializers.serialize("json", donations), content_type="application/json")

@login_required(login_url="/autentikasi/")
def add_crowdfund(request):
    form = CrowdfundForm(request.POST)
    form.instance.fundraiser = request.user.userprofile
    form.instance.fundraiser_name = request.user.username
    form.instance.collected = 0
    if form.is_valid():
        form.save()
        crowdfund = [Crowdfund.objects.all().last()]
        return HttpResponse(serializers.serialize("json", crowdfund), content_type="application/json")
    return JsonResponse({"error": True})

@login_required(login_url="/autentikasi/")
def add_donation(request, id):
    form = DonationForm(request.POST)
    form.instance.donator = request.user.userprofile
    form.instance.donator_name = request.user.username
    form.instance.crowdfund = Crowdfund.objects.get(pk=id)
    if form.is_valid() and form.instance.donator.saldo > form.instance.amount:
        form.save()
        form.instance.donator.saldo -= form.instance.amount
        form.instance.donator.save()
        form.instance.crowdfund.fundraiser.saldo += form.instance.amount
        form.instance.crowdfund.fundraiser.save()
        form.instance.crowdfund.collected += form.instance.amount
        form.instance.crowdfund.save()
        fundraiser_notif = Notification.objects.create(
            user=form.instance.crowdfund.fundraiser.user,
            title=f"Anda menerima donasi sebesar {form.instance.amount}",
            description=f"{form.instance.donator_name} memberikan donasi untuk penggalangan dana {form.instance.crowdfund.title}.",
            time=datetime.now(timezone('Asia/Jakarta'))
        )
        fundraiser_notif.save()
        donatur_notif = Notification.objects.create(
            user=request.user,
            title=f"Anda memberikan donasi sebesar {form.instance.amount}",
            description=f"Donasi diberikan kepada {form.instance.crowdfund.fundraiser_name} untuk penggalangan dana {form.instance.crowdfund.title}.",
            time=datetime.now(timezone('Asia/Jakarta'))
        )
        donatur_notif.save()
        donation = [form.instance.crowdfund]
        return HttpResponse(serializers.serialize("json", donation), content_type="application/json")
    return JsonResponse({"error": True})

def flutter_crowdfunds_by_fundraiser(request, fundraiser_name):
    crowdfunds = Crowdfund.objects.filter(fundraiser_name=fundraiser_name)
    return HttpResponse(serializers.serialize("json", crowdfunds), content_type="application/json")

@csrf_exempt
def flutter_add_crowdfund(request):
    data = json.loads(request.body)
    form = Crowdfund.objects.create(
        fundraiser=User.objects.get(username=form.instance.fundraiser_name),
        fundraiser_name=data["fundraiser_name"],
        title=data["title"],
        description=data["description"],
        collected=0,
        target=data["target"],
        deadline=data["deadline"],
    )
    form.save()
    return JsonResponse({"status": "success"})