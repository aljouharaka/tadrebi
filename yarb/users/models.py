
from django.db import models

# Create your models here.
STATUS_CHOICES = (
    (1, ("student ")),
    (2, ("organization")),
    (3, (" Committee")),
)


class User (models.Model):
    name=models.CharField(max_length=100)
    info=models.TextField()
    usertype=models.IntegerField(choices=STATUS_CHOICES, default=1)


#python manage.py makemigration
#python manage.py migrate

def __str__(self):# if i retrive it will not retrive as User:user but will get as name as i want :)
    return self.name
