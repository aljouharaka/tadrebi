from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index (request):
    return render(request,'SignUp.html')


def req (request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #LogIN
            return redirect('index.html')
    form = UserCreationForm()
    return render(request,'test.html',{'form':form})
