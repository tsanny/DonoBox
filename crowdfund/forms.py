from .models import Crowdfund, Donation
from django.forms import ModelForm

class CrowdfundForm(ModelForm):
    class Meta:
        model = Crowdfund
        fields = ["title", "description", "target", "deadline"]

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ["amount", "comment"]