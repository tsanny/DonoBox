import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
import datetime
import json
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from autentikasi.forms import AccountRoleForm

# Create your views here.


def register(request):
    form = UserCreationForm()
    role_form = AccountRoleForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            new_user = form.save()
            role_form = AccountRoleForm(request.POST)
            new_profile = role_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('autentikasi:login')
    context = {'form':form, 'role_form':role_form}
    return render(request, 'register.html', context)



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("homepage:homepage")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return redirect(request.GET.get('next', 'homepage:homepage'))
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('homepage:homepage'))
    return response


@csrf_exempt
def loginFlutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "message": "Successfully Logged In!"
              # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def registerFlutter(request):
    data = json.loads(request.body)
    dataUser={
    'username':  data['username'],
    'password1': data['password1'],
    'password2': data['password2']
    }
    print(dataUser)
    dataProf={
        'role':data['role']
    }
    print(dataProf)
    form = UserCreationForm(dataUser or None)
    prof = AccountRoleForm(dataProf or None)

    if data['password1']==data['password2']:
        user = form.save()
  
        profile = prof.save()
        profile.user = user
        profile.save()
        role = data['role']
        group = Group.objects.get(name=role)
        user.groups.add(group)
        return JsonResponse({
        'status': 'success'
        }, status=200)
    else:
        return JsonResponse({
            'status': 'failed'
        }, status=401)
