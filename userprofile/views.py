import os
from django.shortcuts import render
from userprofile.models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from userprofile.forms import *



# Create your views here.
def show_profile(request):

    user_data = UserProfile.objects.get(user=request.user)

    bday = user_data.birthday
    phone = user_data.phone
    email = user_data.email

    if bday == None:
        bday = "-"

    if phone == None:
        phone = "-"

    if email == None:
        email = "-"

    context = {
        'user' : request.user,
        'picture' : user_data.picture,
        'bio' : user_data.bio,
        'role' : user_data.role,
        'saldo' : user_data.saldo,
        'birthday' : bday,
        'phone' : phone,
        'email' : email,
        'form1' : ProfileForm,
        'form2' : TopUpForm,
    }
    
    return render(request, 'profile.html', context)

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
    
    

def edit_saldo(request):
    user = request.user.userprofile
    if request.POST:
        new_saldo = request.POST['saldo']
        print(f'new saldo {new_saldo}')
        user_data = UserProfile.objects.get(user=request.user)
        print(f'user saldo {user_data.saldo}')

        user_data.saldo += int(new_saldo)

        user_data.save()
            
        return HttpResponseRedirect('/profile')
            # if obj.saldo:
            #     obj.save(update_fields=['saldo'])

            

def show_json(request):
    profileobj = UserProfile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", profileobj), content_type="application/json")
