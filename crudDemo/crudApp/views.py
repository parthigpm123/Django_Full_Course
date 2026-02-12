from django.shortcuts import render
from django.http import HttpResponse
from crudApp.models import Student

# Create your views here.

def retrieve_view(request):
      student= Student.objects.all()
      return render(request, 'crudApp/index.html', {'student': student})
