from django.db import models

# Create your models here.

class CompanyDetails(models.Model):
    Name = models.CharField(max_length=100)
    Contact= models.IntegerField()
    Website = models.CharField(max_length=200)
    About = models.CharField(max_length=1000)
    Services = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.Name)


class Messages(models.Model):
    user_check = models.CharField(max_length=1, default='B')
    message = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.user_check)





