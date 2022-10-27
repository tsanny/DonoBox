from django.db import models

# Create your models here.
class FrequentlyAskedQuestion(models.Model):
    user = models.CharField(max_length=40,blank=True, null=True)
    pertanyaan = models.TextField()