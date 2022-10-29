from django.shortcuts import render
from .models import Notification
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.http.request import QueryDict

@login_required()
def show_notification(request):
    return render(request, "notification.html")

@login_required()
def notification_json(request):
    user = request.user
    data = Notification.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def ajax_tambah_saldo(request):
    if request.method=="PATCH":
        akun = UserProfile.objects.filter(user=request.user.id).first()
        data = QueryDict(request.body)
        akun.saldo += int(data['saldo'])
        akun.save()
        return HttpResponse(b"UPDATED", status=201)
    return HttpResponseBadRequest("PATCH method required")