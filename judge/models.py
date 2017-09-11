from django.db import models

# Create your models here.

class member(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    AC = models.IntegerField(default=0)