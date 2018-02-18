from django.shortcuts import render
from.forms import  UserLogInForm


def login_View(request):
    form= UserLogInForm(request.POST or None)
    if form,is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")


    return render(request,"form.html",{"form":form})

    
def logout_View(request):
    return render(request,"form.html",{})


    
def register_View(request):
    return render(request,"form.html",{})
# Create your views here.
