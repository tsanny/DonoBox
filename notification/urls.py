from django.urls import path
from .views import *

app_name = "notification"

urlpatterns = [
    path('', show_notification, name='show_notification'),
    path('json/', notification_json, name='notification_json'),
]