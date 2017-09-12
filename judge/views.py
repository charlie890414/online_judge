from django.shortcuts import render
from django.views.decorators import csrf
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from .models import member, news

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
            print(request.POST)
            if request.POST['password'] != request.POST['repassword']:
                return render(request,'signup.html',{"email": request.POST['email'],"name": request.POST['name'],"error": "password are not the same "})
            try :
                new_member = member.objects.create(name=request.POST['name'],email=request.POST['email'],password=make_password(request.POST['password']))
                print(new_member)
                return redirect('/signin')
            except:
                return render(request,'signup.html',{"email": request.POST['email'],"name": request.POST['name'],"error": "your email or name have been used"})
def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    elif request.method == 'POST':
        try:
            member.authenticate(request.POST['email'],request.POST['password'])
            member.login(request)
            return redirect('/')
        except:
            return render(request,'signin.html',{"error":"Sorry, your email or password is not correct."})
def logout(request):
    member.logout(request)
    return redirect('/')

def index(request):
    new = news.objects.all()
    try:
        if request.session['statue'] == 'login':
            return render(request,'index.html',{'login':True,'name':member.get_name(request)})
    except:
        return render(request,'index.html', locals())
