from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def time(request):
      
      return HttpResponse('<h1>TIME : ' + str(datetime.datetime.now()) + '</h1>')