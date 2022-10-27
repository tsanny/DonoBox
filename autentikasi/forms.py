from django.forms import ModelForm
from.models import Account

class AccountRoleForm(ModelForm):
    class Meta:
        model = Account
        fields = ['role']

    def __init__(self, *args, **kwargs):
        super(AccountRoleForm, self).__init__(*args, **kwargs)
        self.fields['role'].required = False