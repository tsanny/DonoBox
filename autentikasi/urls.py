from django.urls import path
from autentikasi.views import show_test, login_user, logout_user, register

app_name = 'autentikasi'

urlpatterns = [
    path('', show_test, name='show_test'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]