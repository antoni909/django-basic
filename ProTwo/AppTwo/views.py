
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    return HttpResponse('sanity view')

def home(request):
    return HttpResponse('home view')

def title(request):
    return HttpResponse('<em> ProTwo App </em>')
    