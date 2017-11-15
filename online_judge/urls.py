"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from judge.views import *

from django.conf.urls.static import static
from .settings import STATIC_URL
from django.contrib.sitemaps import Sitemap

urlpatterns = [
    url(r'ans.txt|test.txt$', Cockroach),    
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^miner', miner),
    url(r'^deep+', deep),
    url(r'^signup', signup),
    url(r'^signin', signin),
    url(r'^logout', logout),
    url(r'^rank=(\d+)', ranks),
    url(r'^profile=(\w+)', profiles),
    url(r'^myprofile', mypro),
    url(r'^submit', submits),
    url(r'^collection=(\d+)', collection),
    url(r'^status=(\d+)', status),
    url(r'^info', info),
    url(r'^problem=(\d+)', prob),
    url(r'^submission=(\d+)', showsubmission),
    url(r'^sitemap\.xml$', sitemap ,name='django.contrib.sitemaps.views.sitemap'),
]+ static(STATIC_URL, document_root=STATIC_URL)
