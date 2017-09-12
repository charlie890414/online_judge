from django.contrib import admin
from .models import member, news
# Register your models here.

class showmember(admin.ModelAdmin):
    list_display = ('name','email', 'AC') # list

class shownews(admin.ModelAdmin):
    list_display = ('title', 'contain') # list

admin.site.register(member,showmember)
admin.site.register(news,shownews)
