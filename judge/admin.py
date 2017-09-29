from django.contrib import admin
from .models import *
# Register your models here.

class showmember(admin.ModelAdmin):
    list_display = ('name','email','AC','AC_problem','choice') # list

class shownew(admin.ModelAdmin):
    list_display = ('title', 'contain') # list

class showsubmission(admin.ModelAdmin):
    list_display = ('id','problem','member','status','lang','code') # list

class showproblem(admin.ModelAdmin):
    list_display = ('title','author','test','ans') # list

admin.site.register(member,showmember)
admin.site.register(new,shownew)
admin.site.register(submission,showsubmission)
admin.site.register(problem,showproblem)