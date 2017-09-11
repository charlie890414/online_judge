from django.shortcuts import render
from django.views.decorators import csrf
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import member

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html')

def signin(request):
    if request.user.is_authenticated():
        return render(request, 'signin.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login (request, user)
        return redirect('/')
    else:
        return render(request, 'signin.html')

def index(request):
    return render(request,'index.html')


def signout(request):
    auth.logout(request)
    return redirect('/')


"""if request.method == 'GET':
    return render(request,'signup.html')
elif request.method == 'POST':
        print(request.POST)
        if request.POST['password'] == request.POST['repassword']:
            new_member = member.objects.create(name=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            print(new_member)
            return redirect('/')"""
