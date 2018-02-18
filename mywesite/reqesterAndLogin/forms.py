from django import forms


class reqForm(forms.ModelForm):
    userName=forms.CharField(max_Length =15,required=true)
    Password=forms.CharField(max_Length =30,required=true)
    email=forms.EmailField()