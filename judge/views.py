from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth  # 別忘了import auth
from django.contrib.auth.forms import UserCreationForm

def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    email = request.POST.get('email', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(email=email, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request,'login.html')
#def post_signup(request):
def index(request):
    return render(request,'index.html')
