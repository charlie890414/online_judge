from django.shortcuts import render
from django.views.decorators import csrf
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files import File
import os
import time
import requests
import json


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        if request.POST['password'] != request.POST['repassword']:
            return render(request, 'signup.html', {"email": request.POST['email'], "name": request.POST['name'], "error": "password are not the same "})
        try:
            new_member = member.objects.create(
                name=request.POST['name'], email=request.POST['email'], password=make_password(request.POST['password']))
            print(new_member)
            return redirect('/signin')
        except:
            return render(request, 'signup.html', {"email": request.POST['email'], "name": request.POST['name'], "error": "your email or name have been used"})


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        try:
            member.authenticate(
                request.POST['email'], request.POST['password'])
            member.login(request)
            return redirect('/')
        except:
            return render(request, 'signin.html', {"error": "Sorry, your email or password is not correct."})


def logout(request):
    member.logout(request)
    return redirect('/')


def index(request):
    news = new.objects.all()
    try:
        first = news[0]
    except:
        first = ''
    try:
        if request.session['statue'] == 'login':
            return render(request, 'index.html', {'login': True, 'name': member.get_name(request), 'news': news, 'first': first})
    except:
        return render(request, 'index.html', locals())


def paginate(request, pg, user_list):
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    if(user_list is not None):
        try:
            users = paginator.page(int(pg))
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return users
    else:
        users = None
        return users


def ranks(request, rank):
    user_list = member.objects.order_by('-AC', 'update')
    users = paginate(request, rank, user_list)
    h = 'rank'
    print(h)
    try:
        if request.session['statue'] == 'login':
            return render(request, 'rank.html', {'login': True, 'name': member.get_name(request), 'paginator': users, 'users': users, 'h': h})
    except:
        return render(request, 'rank.html', {'paginator': users, 'h': h, 'users': users})


def profiles(request, profile):
    user = member.objects.get(name=str(profile))

    try:
        if request.session['statue'] == 'login':
            return render(request, 'profiles.html', {'login': True, 'name': member.get_name(request), 'user': user})
    except:
        return render(request, 'profiles.html', locals())


def collection(request, collection):
    user_list = problem.objects.all()  # 這是題目
    users = paginate(request, collection, user_list)
    h = 'collection'
    if request.method == 'GET':

        problems = problem.objects.all()
        print(problems)
        try:
            if request.session['statue'] == 'login':
                print(member.objects.get(
                    email=request.session['email']).get_AC())
                results = [int(i) for i in member.objects.get(
                    email=request.session['email']).get_AC()]
                return render(request, 'collection.html', {'login': True, 'name': member.get_name(request), 'problems': users, 'paginator': users, 'h': h, 'user_AC': results})
        except:
            return render(request, 'collection.html', locals())


def mypro(request):
    user = member.objects.get(email=str(request.session['email']))
    try:
        if request.session['statue'] == 'login':
            return render(request, 'submit.html', {'login': True, 'name': member.get_name(request), 'user': user})
    except:
        return render(request, 'index.html', locals())


def submits(request):
    user = member.objects.filter(email=request.session['email'])
    users = member.objects.get(email=request.session['email'])
    if request.method == 'POST':
        try:
            print(request.POST)
            user.update(overview=str(request.POST['overview']))
            if(request.POST['pphone'] != None):
                user.update(pphone=str(request.POST['pphone']))
            else:
                user.update(pphone=' ')

            languages = request.POST.getlist('language')
            gender = request.POST.get('Gender')
            user.update(gender=gender)
            user.update(lang="  ".join(languages))
            print(languages)
            return redirect('/myprofile')

        except:
            return render(request, 'signin.html', {"error": "Sorry, your email or password is not correct."})
    elif request.method == 'GET':
        try:
            return redirect('/myprofile')
        except:
            return render(request, 'signin.html', {"error": "Sorry, your email or password is not correct."})


def status(request, status):
    obj = submission.objects.all().order_by('id').reverse()
    users = paginate(request, status, obj)
    h = 'status'
    try:
        if request.session['statue'] == 'login':
            return render(request, 'status.html', {'login': True, "submission": users, 'name': member.get_name(request), 'paginator': users, 'h': h})
    except:
        return render(request, 'status.html', {"submission": users, 'paginator': users, 'h': h})


def info(request):
    try:
        if request.session['statue'] == 'login':
            return render(request, 'info.html', {'login': True, 'name': member.get_name(request)})
    except:
        return render(request, 'info.html')


def prob(request, pid):
    if request.method == 'POST':
        if request.FILES:
            print(request.FILES)
            newsubmit = submission.objects.create(member=member.objects.get(email=request.session['email']), problem=problem.objects.get(
                id=pid), lang=request.POST['lang'], code=request.FILES['file'])
        elif request.POST['editor']:
            print(request.POST['editor'])
            name = '%s' % (time.time())
            file = open(name, 'w+')
            for line in request.POST['editor'].splitlines():
                file.write(line+'\n')
            newsubmit = submission.objects.create(member=member.objects.get(
                email=request.session['email']), problem=problem.objects.get(id=pid), lang=request.POST['lang'], code=File(file))
            file.close()
            os.remove(name)
        return redirect('/status=1')
    if request.method == 'GET':
        prob = problem.objects.get(id=pid)
        url = "http://6792c71c0e98.ngrok.io/"
        try:
            if request.session['statue'] == 'login':
                return render(request, 'problem.html', {'login': True, 'name': member.get_name(request), 'problem': prob, 'url':url})

        except:
            return render(request, 'problem.html', {'problem': prob, 'url':url})


def showsubmission(request, pid):
    submit = submission.objects.get(id=pid)
    place = os.path.join(os.getcwd(), os.path.dirname(
        str(submit.code).replace('/', '\\')))
    lang = submit.lang
    
    try:
        error = open(place+"\\err.txt").read()
    except:
        error = ''
    try:
        code = open(place+"\\code.py").read()
    except:
        try:
            code = open(place+"\\code.cpp").read()
        except:
            code = ''
    try:
        if request.session['statue'] == 'login':
            return render(request, 'submission.html', {'login': True, 'name': member.get_name(request), 'error': error, 'code': code, 'lang': lang})

    except:
        return render(request, 'submission.html', {'error': error, 'code': code, 'lang': lang})
