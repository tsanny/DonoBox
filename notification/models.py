from dataclasses import field
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"({self.pk}) {self.title} | {self.user.username}"