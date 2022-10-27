from django.db import models
from django.contrib.auth.models import User
from email.policy import default

# Create your models here.
class Account(models.Model):
    donatur = 'Donatur'
    fundraiser = 'Fundraiser'
    role_choices = [
        (donatur, 'Donatur'),
        (fundraiser, 'Fundraiser'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.IntegerField(default=0)

    role = models.CharField(choices=role_choices, max_length=10, default=donatur,)

    def __str__(self):
        return self.user.username