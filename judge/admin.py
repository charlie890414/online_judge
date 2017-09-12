from django.contrib import admin
from .models import member
# Register your models here.

class showmember(admin.ModelAdmin):
    list_display = ('name','email', 'AC') # list
 
admin.site.register(member,showmember)