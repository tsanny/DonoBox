from django.urls import path
from autentikasi.views import login_user, logout_user, register

app_name = 'autentikasi'

urlpatterns = [
    path('register/', register, name='register'),
    path('', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]