from django.shortcuts import render
from django.http import HttpResponse

from testApp.models import Employee

# Create your views here.


def cookies_count_view(request):
      count = request.session.get('count',0)
      totalCount = int(count) + 1
      request.session['count'] = totalCount
      print(request.session.get('count'))
      return render(request,'testApp/index.html',{'count':totalCount})

      
      
      






'''
def cookies_count_view(request):
      count = request.COOKIES.get('cookies_count',0)
      totalCount = int(count) + 1
      response = render(request,'testApp/index.html',{'count':totalCount})
      response.set_cookie('cookies_count', totalCount)
      return response

def empDetailsView(request):
      form = forms.EmployeeInfo()
      empInfo = {'form':form}
      return render(request, 'testApp/index.html', context=empInfo)
'''
'''
def display(request):
      date = datetime.datetime.now()
      name = 'parthiban'
      date_dict = {'display_date':date, 'name':name}
      return render(request, 'testApp/index.html',context=date_dict)
'''
