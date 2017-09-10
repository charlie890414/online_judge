from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth  # 別忘了import auth
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/signin/')
    else:
        form = UserCreationForm()

    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')
    return render(request , 'signup.html')

def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    name = requst.POST.get('name','')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username = name, password = password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('signin.html', RequestContext(request, locals()))
