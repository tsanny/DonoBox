from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    donatur = 'Donatur'
    fundraiser = 'Fundraiser'
    role_choices = [
        (donatur, 'Donatur'),
        (fundraiser, 'Fundraiser'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='userprofile/images', null=True)
    bio = models.TextField(null=True)
    role = models.CharField(choices=role_choices, max_length=10, default=donatur,)
    saldo = models.BigIntegerField(default=0)