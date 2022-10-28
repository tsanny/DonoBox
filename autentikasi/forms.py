from django.forms import ModelForm
from userprofile.models import UserProfile

class AccountRoleForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role']

    def __init__(self, *args, **kwargs):
        super(AccountRoleForm, self).__init__(*args, **kwargs)
        self.fields['role'].required = False