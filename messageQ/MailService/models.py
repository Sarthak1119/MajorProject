from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class SentMail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.user)

class InboxMail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_user = models.CharField(max_length=100)
    rec_subject = models.CharField(max_length=500)
    message_rec = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.user)

