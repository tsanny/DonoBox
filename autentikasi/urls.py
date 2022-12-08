from django.urls import path
from autentikasi.views import login_user, logout_user, register, loginFlutter, registerFlutter

app_name = 'autentikasi'

urlpatterns = [
    path('register/', register, name='register'),
    path('', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('login_apk/', loginFlutter, name='login_apk'),
    path('reg_apk/', registerFlutter, name='reg_apk'),
]