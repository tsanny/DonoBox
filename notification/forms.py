from django.forms import ModelForm
from userprofile.models import UserProfile
from .models import Notification

class NotificationForms(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'

class SaldoForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['saldo']