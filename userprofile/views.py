import os
from django.shortcuts import render
from userprofile.models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from userprofile.forms import *

# Create your views here.
def show_profile(request):
    user_data = UserProfile.objects.get(user=request.user)

    context = {
        'user' : request.user,
        'picture' : user_data.picture,
        'bio' : user_data.bio,
        'role' : user_data.role,
        'form' : ProfileForm
    }
    
    return render(request, 'profile.html', context)

def edit_profile(request):
    user = request.user.userprofile
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            # form.save()
            obj = form.save(commit=False)

            if obj.picture:
                obj.save(update_fields=['picture'])

            if obj.bio:
                obj.save(update_fields=['bio'])

    return HttpResponseRedirect('/profile')
