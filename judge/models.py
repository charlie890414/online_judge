from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.


class member(models.Model):
    name = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    AC = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def authenticate(useremail,password):
        user = member.objects.get(email=useremail)
        return check_password(password,user.password)

    def login(request):
        request.session['statue'] = 'login'
        return request

    def logout(request):
        del request.session['statue'] 
        return request