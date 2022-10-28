from .models import Crowdfund, Donation
from datetime import datetime
from django.forms import ModelForm

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
        if len(title) > 50:
            self.add_error("title", "Judul harus kurang dari 50 karakter.")
        if len(description) > 1000:
            self.add_error("description", "Informasi harus kurang dari 1000 karakter.")
        if target < 1 or target > 1000000000:
            self.add_error("target", "Target dana harus di antara 1 dan 1000000000.")
        if deadline < datetime.now():
            self.add_error("deadline", "Tanggal dan waktu batas harus di masa depan.")

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ["amount", "comment"]

    def clean(self):
        cleaned = super().clean()
        amount = cleaned.get("amount")
        comment = cleaned.get("comment")
        if amount < 1 or amount > 1000000000:
            self.add_error("amount", "Jumlah donasi harus di antara 1 dan 1000000000.")
        if len(comment) > 1000:
            self.add_error("comment", "Komentar harus kurang dari 1000 karakter.")
