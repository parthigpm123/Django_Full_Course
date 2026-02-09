from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def display(request):
      date = datetime.datetime.now()
      date_dict = {'display_date':date}
      return render(request, 'testApp/index.html',context=date_dict)

