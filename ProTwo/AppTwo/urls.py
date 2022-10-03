from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index),
    path("title/",views.title),
    path("help/",views.help),
]
