
from datetime import date
from pydoc_data.topics import topics
from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse 
from .models import Topic, WebPage, Page, User

# Create your views here.

def index(request):
    dic = {'insert_me':"from views.py index fn"}
    return render(request,'AppTwo/index.html',context=dic)

def users(request):
    user_list = User.objects.order_by('lastN')
    user_dic = {'users':user_list}
    print('***',user_dic)
    return render(request,'Apptwo/users.html',context=user_dic)

def pages(request):
    page_list = Page.objects.order_by('title')
    page_dic = {'pages':page_list}
    return render(request,'AppTwo/pages.html',context=page_dic)

def title(request):
    return HttpResponse('<em> ProTwo App </em>')

def help(request):
    dic = { 'help_me': 'from views.py help fn' }
    return render(request, 'AppTwo/help.html',context=dic)
