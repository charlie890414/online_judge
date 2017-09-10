from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib import auth  # 別忘了import auth

def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    email = request.POST.get('email', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(email=email, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render(request,'login.html')
def signup(request):
    
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    name = requst.POST.get('name','')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    
    

def index(request):
    return render(request,'index.html')
