from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def gm(request):
      return HttpResponse('<h1>GOOD MORNING</h1>')

def ga(request):
      return HttpResponse('<h1>GOOD AFTERNOON</h1>')


