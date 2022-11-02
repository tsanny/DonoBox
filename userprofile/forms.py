from django.forms import ModelForm
from.models import UserProfile
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', 'bio', 'birthday', 'email', 'phone']
        widgets = {
            'birthday' : DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False
        self.fields['bio'].required = False
        self.fields['birthday'].required = False
        self.fields['email'].required = False
        self.fields['phone'].required = False

class TopUpForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['saldo']

    
