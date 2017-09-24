from django.shortcuts import render
from django.views.decorators import csrf
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from .models import member, new
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    news = new.objects.all()
    try:
        if request.session['statue'] == 'login':
            return render(request,'index.html',{'login':True,'name':member.get_name(request)})
    except:
        return render(request,'index.html', locals())

def ranks(request, rank):
    user_list = member.objects.order_by('AC').reverse()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    if(user_list is not None):
        try:
            users = paginator.page(int(rank))
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)

        try:
            if request.session['statue'] == 'login':
                return render(request, 'rank.html', {'users' :users, 'login':True,'name':member.get_name(request)})

        except:
            return render(request,'rank.html', locals())
    else:
        try:
            if request.session['statue'] == 'login':
                return render(request, 'rank.html', {'users' :users, 'login':True,'name':member.get_name(request), 'error' :'Has No User'})

        except:
            return render(request,'rank.html', {'login':True,'name':member.get_name(request), 'error' :'Has No User'})


def profiles(request, profile):
    user = member.objects.get(name=str(profile))

    try:
        if request.session['statue'] == 'login':
            return render(request,'profiles.html',{'login':True,'name':member.get_name(request), 'user':user})
    except:
        return render(request, 'profiles.html', locals())
    
def collection(request):
    if request.method == 'GET':
        try:
            if request.session['statue'] == 'login':
                return render(request,'collection.html',{'login':True,'name':member.get_name(request)})
        except:
            return render(request,'collection.html', locals())

def mypro(request):
    user = member.objects.get(email=str(request.session['email']))
    try:
        if request.session['statue'] == 'login':
            return render(request,'submit.html',{'login':True,'name':member.get_name(request),'user':user})
    except:
        return render(request, 'index.html', locals())

def submits(request):
    user = member.objects.filter(email=request.session['email'])
    users = member.objects.get(email=request.session['email'])
    if request.method == 'POST':
        try:
            print(request.POST)
            user.update(overview=str(request.POST['overview']))
            user.update(pphone=str(request.POST['pphone']))
            return redirect('/myprofile') 
            
        except:
            return render(request,'signin.html',{"error":"Sorry, your email or password is not correct."})
    elif request.method == 'GET':
        try:
            return redirect('/myprofile')
        except:
            return render(request,'signin.html',{"error":"Sorry, your email or password is not correct."})