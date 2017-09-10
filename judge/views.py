from django.shortcuts import render
from django.views.decorators import csrf
from django.shortcuts import redirect
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth  # 別忘了import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        
        print(request.POST)           
        
        return redirect('/')
def signin(request):
    return render(request,'signin.html')

def index(request):
    return render(request,'index.html')
