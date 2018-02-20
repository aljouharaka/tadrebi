from django import forms
from . import models

class Create (forms.ModelForm):
    class Meta:
        model = models.User
        fields=['username','usertype','email','password1','password2']

        
