from django.shortcuts import render
from django.views.decorators import csrf
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from .models import member

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':        
            print(request.POST)  
            if request.POST['password'] != request.POST['repassword']:    
                return render(request,'signup.html',{"email": request.POST['email'],"name": request.POST['name'],"error": "password are not the same "})
            new_member = member.objects.create(name=request.POST['name'],email=request.POST['email'],password=make_password(request.POST['password']))
            print(new_member)          
            return redirect('/')
def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    elif request.method == 'POST':   
        if member.authenticate(request.POST['email'],request.POST['password']):
            member.login(request)
            return redirect('/')
        else:
            return render(request,'signin.html') 
def logout(request):
    member.logout(request)
    return redirect('/')

def index(request):
    try:
        if request.session['statue'] == 'login':
            return render(request,'index.html',{'login':True})
    except:
        return render(request,'index.html')
