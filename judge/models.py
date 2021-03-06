import os
from jsonfield import JSONField
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.

class member(models.Model):
    name = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    AC = models.IntegerField(default=0)
    AC_test = JSONField(blank=True)
    AC_problem = models.TextField(default="",blank=True)
    overview = models.CharField(max_length=500, default="",blank=True)
    pphone = models.CharField(blank=True,default="",max_length=10)

    create = models.DateTimeField(auto_now_add=True)
    update = models.IntegerField(default=0)

    lang = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    def get_name(request):
        user = member.objects.get(email=request.session['email'])
        return user.name

    def authenticate(useremail,password):
        user = member.objects.get(email=useremail)
        return check_password(password,user.password)

    def login(request):
        request.session['statue'] = 'login'
        request.session['email'] = request.POST['email']
        return request

    def logout(request):
        del request.session['statue']
        del request.session['email']
        return request
    
    def get_AC(self):
        return str(self.AC_problem).split()

    def save(self, *args, **kwargs):
        self.password=make_password(self.password)
        self.AC = len(self.get_AC())
        super(member, self).save(*args, **kwargs)

class new(models.Model):
    title = models.CharField(max_length=20)
    contain = models.CharField(max_length=500)
    imgUrl = models.CharField(max_length=1000,blank=False,default="https://images.unsplash.com/photo-1484788984921-03950022c9ef?dpr=1&auto=compress,format&fit=crop&w=2004&h=&q=80&cs=tinysrgb&crop=")

    def __str__(self):
        return self.title
def generate_PDF(self, filename):
    url = "static/question/%s/context.pdf" % (self.title.replace(' ','_'))
    try:
        os.remove(url)
    finally:
        return url
def generate_questionfiletest(self, filename):
    url = "static/question/%s/test.txt" % (self.title.replace(' ','_'))
    try:
        os.remove(url)
    finally:
        return url
def generate_questionfileans(self, filename):
    url = "static/question/%s/ans.txt" % (self.title.replace(' ','_'))
    try:
        os.remove(url)
    finally:
        return url
class problem(models.Model):
    title = models.CharField(max_length=30,unique=True)
    author = models.ForeignKey('member',to_field = 'name', on_delete=models.CASCADE)
    PDFcontext = models.FileField(upload_to=generate_PDF,null=True,blank=True)
    context = models.TextField(blank=True)
    samplein = models.TextField(default="(None)")
    sampleout = models.TextField(blank=True)
    test = models.FileField(upload_to=generate_questionfiletest,null=True,blank=True)
    ans = models.FileField(upload_to=generate_questionfileans)
    def __str__(self):
        return self.title

def generate_submissionfilename(self, filename):
    if self.lang == "python3":
        file='py'
    elif self.lang == "c++":
        file='cpp'
    url = "static/submission/%s/%s/%s/code.%s" % (str(self.member.name).replace(' ','_'),self.problem.id,datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"),file)
    try:
        os.remove(url)
    finally:
        return url
class submission(models.Model):
    member = models.ForeignKey('member',to_field = 'name', on_delete=models.CASCADE)
    problem = models.ForeignKey('problem',to_field = 'title', on_delete=models.CASCADE)
    status = models.CharField(max_length=20,default='waiting')
    lang = models.CharField(max_length=15,default='')
    code = models.FileField(upload_to=generate_submissionfilename)
    def __str__(self):
        return str(self.id)
