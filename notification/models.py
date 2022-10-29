from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    timesince = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"({self.pk}) {self.title} | {self.user.username}"

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.time

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                self.timesince = str(seconds) +  "second ago"
            
            else:
                self.timesince = str(seconds) + " seconds ago"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                self.timesince = str(minutes) + " minute ago"
            
            else:
                self.timesince = str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                self.timesince = str(hours) + " hour ago"

            else:
                self.timesince = str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                self.timesince = str(days) + " day ago"

            else:
                self.timesince = str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                self.timesince = str(months) + " month ago"

            else:
                self.timesince = str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                self.timesince = str(years) + " year ago"

            else:
                self.timesince = str(years) + " years ago"