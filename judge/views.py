from django.shortcuts import render
from django.views.decorators import csrf
from django.shortcuts import redirect
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import member

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        
            print(request.POST)  
            if request.POST['password'] == request.POST['repassword']:      
                new_member = member.objects.create(name=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
                print(new_member)
          
            return redirect('/')
def signin(request):
    return render(request,'signin.html')

def index(request):
    return render(request,'index.html')
