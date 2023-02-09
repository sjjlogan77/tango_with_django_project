from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/rango/about">Rango says hey there partner!</a>')

def about(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/rango/">Rango says here is the about page.')
