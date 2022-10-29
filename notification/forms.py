from django.forms import ModelForm
from userprofile.models import UserProfile

class SaldoForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['saldo']