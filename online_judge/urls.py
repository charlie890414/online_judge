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
<<<<<<< HEAD
from judge.views import index, signup, signin, logout, rank, collection
=======
from judge.views import index, signup, signin, logout, ranks

from django.conf.urls.static import static
from .settings import STATIC_URL
>>>>>>> 821120d7dd3f77d73bf6911d70d41c5e1aaf190d

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^signup', signup),
    url(r'^signin', signin),
    url(r'^logout', logout),
<<<<<<< HEAD
    url(r'^rank', rank),
    url(r'^rank=(\d+)', rank),
    url(r'^collection', collection)
]
=======
    url(r'^rank=(\d+)', ranks),
]+ static(STATIC_URL, document_root=STATIC_URL)
>>>>>>> 821120d7dd3f77d73bf6911d70d41c5e1aaf190d
