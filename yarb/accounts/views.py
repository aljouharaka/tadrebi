from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import RegisterForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render (request,'accounts/home.html')

@login_required(login_url="/accounts/login/")
def profile (request):
    return render (request,'accounts/profile.html')


def signup_view (request):
    if request.method == 'POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            user =form.save()
            #log the user in
            login(request,user)
            return redirect('accounts:profile') #'app:name'
    else:
        form= RegisterForm()
    return render (request,'accounts/signup.html',{'form':form})


def login_view (request):
    if request.method == 'POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user =form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('accounts:profile') #'app:name'


    else:
        form = AuthenticationForm()
    return render  (request,'accounts/login.html',{'form':form})



def logout_view (request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:home') #'app:name'
