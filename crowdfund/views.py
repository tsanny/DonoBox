from .models import *
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render

def show_crowdfunds(request):
    context = {"user": request.user}
    return render(request, "crowdfunds.html", context)

@login_required(login_url="/autentikasi/login/")
def show_crowdfund(request, id):
    context = {"id": id}
    return render(request, "crowdfund.html", context)

def show_crowdfunds_json(request):
    crowdfunds = Crowdfund.objects.all()
    return  HttpResponse(serializers.serialize("json", crowdfunds), content_type="application/json")

def show_crowdfunds_json_ongoing(request):
    crowdfunds = Crowdfund.objects\
        .filter(deadline__gt=datetime.now()) \
        .filter(collected__lt=F("target"))
    return HttpResponse(serializers.serialize("json", crowdfunds), content_type="application/json")

def show_crowdfund_json(request, id):
    crowdfund = Crowdfund.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", crowdfund), content_type="application/json")