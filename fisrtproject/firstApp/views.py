from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wish(request):
      message = '<h6>GOOD MORNING</h6>'
      return HttpResponse(message)