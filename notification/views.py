from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.http.request import QueryDict
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


from .models import Notification
from .forms import SaldoForm

@login_required(login_url="/autentikasi/")
def show_notification(request):
    return render(request, "notification.html")

@login_required(login_url="/autentikasi/")
def notification_json(request):
    user = request.user
    data = Notification.objects.filter(user=user)
    for instance in data:
        instance.whenpublished()
        instance.save()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def ajax_tambah_saldo(request):
    user = request.user.userprofile

    if request.method=="PATCH":
        data = QueryDict(request.body)
        new_saldo = user.saldo + int(data["saldo"])
        form = SaldoForm(data={'saldo': new_saldo}, instance=user)

        if form.is_valid():
            form.save()
            return HttpResponse(b"UPDATED", status=201)

    return HttpResponseBadRequest("PATCH method required")

@csrf_exempt
def notification_json_flutter(request):
    session_key = request.COOKIES['sessionid']
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    data = Notification.objects.filter(user=user)
    for instance in data:
        instance.whenpublished()
        instance.save()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")