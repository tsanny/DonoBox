from django.forms import ModelForm
from.models import UserProfile

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', 'bio']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False
        self.fields['bio'].required = False

class TopUpForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['saldo']

    
