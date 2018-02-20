from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

STATUS_CHOICES = (
    (1, ("student ")),
    (2, ("organization")),
    (3, (" Committee")),
)
class RegisterForm (UserCreationForm):
    username = forms.CharField(
        max_length=30,
        help_text='')
    password1 = forms.CharField(widget=forms.PasswordInput,help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput,help_text='')
    email=forms.EmailField(required=True)
    usertype=forms.ChoiceField(
                               choices = STATUS_CHOICES,
                                label="type ",
                                initial=1,
                                widget=forms.Select(),
                                required=True
                                )
class Meta:
    model =User
    fields=('username','email','password1','password2','usertype')

def __init__(self, *args, **kwargs):
    super(RegisterForm, self).__init__(*args, **kwargs)
    self.fields['myfield'].widget.attrs.update({'class' : 'tab-content-inner activel'})

def save(self,commit=True):
    user=super (RegisterForm,self).save (commit=False)
    user.email=self.cleaned_data['email']
    user.usertype=self.cleaned_data['usertype']
    if commit:
        user.save()
    return user
