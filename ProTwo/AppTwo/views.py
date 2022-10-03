
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    dic = {'insert_me':"from views.py index fn"}
    return render(request,'AppTwo/index.html',context=dic)

def title(request):
    return HttpResponse('<em> ProTwo App </em>')

def help(request):
    dic = { 'help_me': 'from views.py help fn' }
    return render(request, 'AppTwo/help.html',context=dic)
