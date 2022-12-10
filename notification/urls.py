from django.urls import path
from .views import *

app_name = "notification"

urlpatterns = [
    path('', show_notification, name='show_notification'),
    path('json/', notification_json, name='notification_json'),
    path('json-flutter/', notification_json_flutter, name='notification_json'),
    path('ajax-tambah-saldo', ajax_tambah_saldo, name='ajax-tambah-saldo'),
]