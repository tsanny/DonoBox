from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artikel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    title = models.TextField()
    short_description = models.TextField(max_length=60)
    description = models.TextField()
