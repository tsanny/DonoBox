from django.shortcuts import render
from .models import Artikel
from django.contrib.auth.models import User
from datetime import datetime
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
    data = serializers.serialize('json', Artikel.objects.all()) 
    data1 = serializers.serialize('json', User.objects.all())
    return JsonResponse({"artikel":list(artikel.values()), "user":list(users.values('username', 'pk'))},)
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