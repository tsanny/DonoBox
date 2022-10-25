from django.shortcuts import render
from .models import Notification
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required()
def show_notification(request):
    return render(request, "notification.html")

def notification_json(request):
    user = request.user
    data = Notification.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")