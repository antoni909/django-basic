from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index),
    path("pages/",views.pages),
    path("users/",views.users),
    path("title/",views.title),
    path("help/",views.help),
]
