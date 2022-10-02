from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("",views.home),
    path("sanity/",views.index),
    path("title/",views.title)
]
