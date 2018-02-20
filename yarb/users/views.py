from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User #from .models import name of table .. to import table of database (model)
from django.contrib.auth.decorators import login_required #to protect page from unsignin people
from .import forms
# Create your views here.
def user_profile (request):
    return render (request,'users/user.html')

@login_required(login_url="/accounts/login/")#this protected from unsigned people
def user_create (request):
    if request.method =='POST':
        form = forms.CreateUser(request.POST,request.FILES)#request.FILES if there are files
        if form.is_valid():
            #save user to DB
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect ('users:profile')

    else:
        form = forms.CreateUser()
    return render (request,'users/user_create.html',{'form':form})
