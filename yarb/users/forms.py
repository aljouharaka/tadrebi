from django import forms
from . import models

class CreateUser (forms.ModelForm):
    class Meta:
        model = models.User
        fields=['name','info','usertype']
