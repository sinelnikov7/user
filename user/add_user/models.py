from django.db import models


class User(models.Model):

    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# Create your models here.
