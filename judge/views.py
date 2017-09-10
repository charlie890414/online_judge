from django.shortcuts import render

# Create your views here.

...
from django.contrib import auth  # 別忘了import auth

...
def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    name = requst.POST.get('name','')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(name=name,email=email, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('singin.html')

def index(request):
    return render_to_response('index.html',locals())
