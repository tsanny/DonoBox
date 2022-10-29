import json
from django.shortcuts import render
from homepage.forms import FormPertanyaan
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from homepage.models import FrequentlyAskedQuestion
from django.views.decorators.csrf import csrf_exempt

def show_json(request):
    data_pertanyaan = FrequentlyAskedQuestion.objects.all()
    return HttpResponse(serializers.serialize('json', data_pertanyaan), content_type='application/json')

def home(request):
    username = 'anon'
    if request.user.is_authenticated:
        username = request.user

        
    if request.method == 'POST':
        user = username
        pertanyaan = request.POST.get('pertanyaan')
        FrequentlyAskedQuestion.objects.create(user=user, pertanyaan=pertanyaan)
        return JsonResponse({
            'msg': 'Success'
        })
    else:
        pertanyaan_form = FormPertanyaan()
        faqs = FrequentlyAskedQuestion.objects.all()

        for faq in faqs:
            print(faq)
        context = {
            'pertanyaan':'pertanyaan',
            'form' : pertanyaan_form
        }
    return render(request, "homepage.html", context)

@csrf_exempt
def faq_ajax(request):
    if request.method == 'POST':
        user = request.user
        pertanyaan = request.POST.get('pertanyaan')
        FrequentlyAskedQuestion.objects.create(user=user, pertanyaan=pertanyaan)
    return JsonResponse({"faqs": "new question"},status=200)

def list_pertanyaan(request):
    list_pertanyaan = FrequentlyAskedQuestion.objects.all()
    context = {'list_pertanyaan': list_pertanyaan}
    return render(request, 'form_pertanyaan.html', context)
