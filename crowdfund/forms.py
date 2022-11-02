from .models import Crowdfund, Donation
from datetime import datetime
from django.forms import ModelForm
from pytz import timezone

class CrowdfundForm(ModelForm):
    class Meta:
        model = Crowdfund
        fields = ["title", "description", "target", "deadline"]

    def clean(self):
        cleaned = super().clean()
        title = cleaned.get("title")
        description = cleaned.get("description")
        target = cleaned.get("target")
        deadline = cleaned.get("deadline")
        if (title != None) and (description != None) and (target != None) and (deadline != None):
            if len(title) < 1 or len(title) > 50:
                self.add_error("title", "Judul harus di antara 1 dan 50 karakter.")
            if len(description) > 1000:
                self.add_error("description", "Deskripsi harus tidak lebih dari 1000 karakter.")
            if target < 1 or target > 1000000000:
                self.add_error("target", "Target dana harus di antara 1 dan 1000000000.")
            if deadline < datetime.now().replace(tzinfo=timezone("UTC")):
                self.add_error("deadline", "Batas waktu harus tidak kurang dari saat ini.")

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ["amount", "comment"]

    def clean(self):
        cleaned = super().clean()
        amount = cleaned.get("amount")
        comment = cleaned.get("comment")
        if (amount != None) and (comment != None):
            if amount < 1 or amount > 1000000000:
                self.add_error("amount", "Jumlah donasi harus di antara 1 dan jumlah saldo.")
            if len(comment) > 1000:
                self.add_error("comment", "Komentar harus tidak lebih dari 1000 karakter.")
