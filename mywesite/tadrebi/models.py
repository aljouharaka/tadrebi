from django.db import models


class Student(models.Model):
    email = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password =models.CharField(max_length=100)

    def __str__(self):
        return self.email+' - '+self.username
