from .forms import CrowdfundForm, DonationForm
from .models import Crowdfund, Donation
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def show_crowdfunds(request):
    context = {
        "logged_in": request.user.is_authenticated,
        "user": request.user,
        "role": getattr(getattr(request.user, "account", None), "role", None)
        }
    return render(request, "crowdfunds.html", context)

@login_required(login_url="/autentikasi/login/")
def show_crowdfund(request, id):
    context = {
        "id": id,
        "role": getattr(request.user.account)
        }
    return render(request, "crowdfund.html", context)

def show_crowdfunds_json_ongoing(request):
    crowdfunds = Crowdfund.objects\
        .filter(deadline__gt=datetime.now())\
        .filter(collected__lt=F("target"))
    return HttpResponse(serializers.serialize("json", crowdfunds), content_type="application/json")

@login_required(login_url="/autentikasi/login/")
def show_crowdfunds_json_by_me(request):
    crowdfunds = Crowdfund.objects.filter(fundraiser__user=request.user)
    return HttpResponse(serializers.serialize("json", crowdfunds), content_type="application/json")

@login_required(login_url="/autentikasi/login/")
def show_crowdfund_json(request, id):
    crowdfund = Crowdfund.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", crowdfund), content_type="application/json")

@login_required(login_url="/autentikasi/login/")
def show_donations_json_by_fund(request, id):
    donations = Donation.objects.filter(crowdfund__pk=id)
    return HttpResponse(serializers.serialize("json", donations), content_type="application/json")

def add_crowdfund(request):
    form = CrowdfundForm(request.POST)
    form.instance.fundraiser = request.user.account
    if form.is_valid():
        form.save()
        return JsonResponse(form.cleaned_data)
    return JsonResponse(form.errors)

def add_donation(request, id):
    form = DonationForm(request.POST)
    form.instance.donator = request.user.account
    form.instance.crowdfund = Crowdfund.objects.get(pk=id)
    if form.is_valid():
        form.save()
        return JsonResponse(form.cleaned_data)
    return JsonResponse(form.errors)