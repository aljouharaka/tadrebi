from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Req(models.model):
    userName=models.CharField(max_Length =15)
    Password=models.CharField(max_Length =30)
    email=models.EmailField()
    type=models.IntegerField()   
