from django.urls import path
from homepage.views import home, list_pertanyaan
from homepage.views import show_json
from homepage.views import faq_ajax
from homepage.views import list_pertanyaan

app_name = 'homepage'

urlpatterns = [
    path('', home, name='homepage'),
    path('json/', show_json, name='show_json'),
    path('home/', home, name='home'),
    path('faq_ajax/', faq_ajax, name='faq_ajax'),
    path('list_pertanyaan/', list_pertanyaan, name='list_pertanyaan'),
    
]