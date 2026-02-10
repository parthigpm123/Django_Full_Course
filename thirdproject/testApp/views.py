from django.shortcuts import render
from django.http import HttpResponse
import datetime
from testApp.models import Employee
# Create your views here.

def empDetails(request):
      emp_data = Employee.objects.all()
      emp_dict = {'emp_list':emp_data}
      return render(request, 'testApp/index.html', context=emp_dict)

'''
def display(request):
      date = datetime.datetime.now()
      name = 'parthiban'
      date_dict = {'display_date':date, 'name':name}
      return render(request, 'testApp/index.html',context=date_dict)
'''
