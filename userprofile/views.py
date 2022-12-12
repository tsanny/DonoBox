import os
from django.shortcuts import render
from userprofile.models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from userprofile.forms import *
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/autentikasi')
def show_profile(request):

    user_data = UserProfile.objects.get(user=request.user)

    bio = user_data.bio
    bday = user_data.birthday
    phone = user_data.phone
    email = user_data.email
    is_donatur = False
    is_fundraiser = False

    if user_data.role == 'Donatur':
        is_donatur = True

    else:
        is_fundraiser = True

    if bio == None:
        bio = "-"

    if bday == None:
        bday = "-"
    
    else:
        bday = bday.strftime("%Y-%m-%d")

    if phone == None:
        phone = "-"

    if email == None:
        email = "-"

    context = {
        'user' : request.user,
        'picture' : user_data.picture,
        'bio' : bio,
        'role' : user_data.role,
        'saldo' : user_data.saldo,
        'birthday' : bday,
        'phone' : phone,
        'email' : email,
        'is_donatur' : is_donatur,
        'is_fundraiser' : is_fundraiser,
        'form1' : ProfileForm,
        'form2' : TopUpForm,
    }
    
    return render(request, 'profile.html', context)

@login_required(login_url='/autentikasi')
def show_topup(request):

    return render(request, 'topup.html')

def edit_profile(request):
    user = request.user.userprofile
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=user)
        print(form.is_valid())

        if form.is_valid():
            obj = form.save(commit=False)

            if obj.picture:
                obj.save(update_fields=['picture'])

            if obj.bio:
                obj.save(update_fields=['bio'])

            if obj.birthday:
                obj.save(update_fields=['birthday'])

            if obj.email:
                obj.save(update_fields=['email'])

            if obj.phone:
                obj.save(update_fields=['phone'])
            

            return HttpResponse("success")

@csrf_exempt
def edit_profile_flutter(request):
    user = request.user.userprofile
    # profileobj = UserProfile.objects.get(user=request.user)
    form = ProfileForm(request.POST, instance=user)
    if request.POST:
        obj = form.save(commit=False)
        print('ini masuk edit profile')
        if obj.picture:
            obj.save(update_fields=['picture'])

        if obj.bio:
            obj.save(update_fields=['bio'])

        if obj.birthday:
            obj.save(update_fields=['birthday'])

        if obj.email:
            obj.save(update_fields=['email'])

        if obj.phone:
            obj.save(update_fields=['phone'])

        # profileobj.save()

        return JsonResponse({"status": "success"}, status=200)

    return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def edit_saldo(request):
    user = request.user.userprofile
    form = TopUpForm(request.POST, instance=user)
    if request.POST:
        obj = form.save(commit=False)

        if obj.saldo:
            obj.save(update_fields=['saldo'])

        # new_saldo = request.POST['saldo']
        # print(f'new saldo {new_saldo}')
        # user_data = UserProfile.objects.get(user=request.user)
        # print(f'user saldo {user_data.saldo}')

        # if int(new_saldo) > 0:
        #     user_data.saldo += int(new_saldo)

        #     user_data.save()
            
        return JsonResponse({"status": "success"}, status=200)

    return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def edit_saldo_flutter(request):
    user = request.user.userprofile
    if request.POST:
        saldo_tambahan = request.POST.get('saldo')
        user.saldo += int(saldo_tambahan)

        # if obj.saldo:
        #     obj.save(update_fields=['saldo'])

            
        return JsonResponse({"status": "success"}, status=200)

    return JsonResponse({"status": "error"}, status=401)

def show_json(request):
    profileobj = UserProfile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", profileobj), content_type="application/json")

def show_json_flutter(request):
    user_data = UserProfile.objects.get(user=request.user)

    return JsonResponse([{"user":str(request.user), "bio":user_data.bio, "role":user_data.role, "saldo":user_data.saldo, "birthday":user_data.birthday, "email":user_data.email, "phone":user_data.phone}], safe=False)
