from django.shortcuts import render
from django.http import HttpResponse

from testApp.models import Employee
from . import forms
# Create your views here.

def empDetailsView(request):
      form = forms.EmployeeInfo()
      empInfo = {'form':form}
      return render(request, 'testApp/index.html', context=empInfo)
'''
def display(request):
      date = datetime.datetime.now()
      name = 'parthiban'
      date_dict = {'display_date':date, 'name':name}
      return render(request, 'testApp/index.html',context=date_dict)
'''
