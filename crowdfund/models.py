from django.db import models
from userprofile.models import UserProfile

class Crowdfund(models.Model):
    fundraiser = models.ForeignKey(UserProfile, on_delete = models.CASCADE, blank=True, null=True)
    fundraiser_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    collected = models.PositiveIntegerField()
    target = models.PositiveIntegerField()
    deadline = models.DateTimeField()

class Donation(models.Model):
    donator = models.ForeignKey(UserProfile, on_delete = models.CASCADE, blank=True, null=True)
    donator_name = models.CharField(max_length=150, blank=True, null=True)
    crowdfund = models.ForeignKey(Crowdfund, on_delete = models.CASCADE)
    amount = models.PositiveIntegerField()
    comment = models.TextField(blank=True)