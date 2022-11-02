from django.shortcuts import render
from math import trunc
from .models import Artikel
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def show_artikel(request):
    list_artikel = Artikel.objects.all()
    date = datetime.today()
    context = {
    'list_artikel': list_artikel,
    'date':date,
    }
    return render(request, "artikel.html", context)

def show_artikel_detail(request, pk):
    data = Artikel.objects.filter(pk=pk)
    context = {
        'artikel':data,
        }
    return render(request, "artikel_detail.html", context)

def show_json(request):

    artikel = Artikel.objects.all()
    users = User.objects.all()
    seconds_in_day = 60 * 60 * 24
    print(" ===== ==== == = = === \n")
    time_diff = {}
    for art in artikel.values():
        total_seconds = (datetime.today().replace(tzinfo=None) -  (art["date"].replace(tzinfo=None))).total_seconds()
        day = trunc(total_seconds / seconds_in_day )
        hour = trunc((total_seconds - (day*seconds_in_day))/3600)
        minute = trunc((total_seconds - day*seconds_in_day - hour*3600)/60)
        second = trunc(total_seconds - day*seconds_in_day - hour*3600 - minute*60)
        if (day == 0):
            if (hour == 0):
                if (minute == 0):
                    diff = str(second) + " seconds ago"
                elif (minute == 1):
                    diff = str(minute) + " minute ago"
                else:
                    diff = str(minute) + " minutes ago"
            elif (hour == 1):
                diff = str(hour) + " hour ago"
            else:
                diff = str(hour) + " hours ago"
        elif (day == 1):
            diff = str(day) + " day ago"
        else:
            diff = str(day) + " days ago"
        time_diff[art["id"]] = diff
    return JsonResponse({"artikel":list(artikel.values()), "user":list(users.values('username', 'pk')), "time_diff":time_diff},)
    #return HttpResponse({0:data, 1:data1}, content_type="application/json")

@csrf_exempt
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = str(request.POST.get('description'))

        artikel = Artikel(user=request.user, title=title, description=description, date=datetime.today(), short_description=str(description)[0:60])
        artikel.save()
        return JsonResponse(
            {
            "pk": artikel.pk,
            "user": str(request.user),
            "title": title,
            "date": datetime.today(),
            "short_description": str(description)[0:60],
        }, status=200)