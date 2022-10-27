from django import forms

from homepage.models import FrequentlyAskedQuestion

class FormPertanyaan(forms.Form):
    pertanyaan = forms.CharField(widget=forms.Textarea, label="")
    class Meta:
        model = FrequentlyAskedQuestion
        fields = ['pertanyaan']