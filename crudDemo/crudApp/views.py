from django.shortcuts import render
from django.http import HttpResponse
from crudApp.models import Student
from crudApp.forms import StudentForm

# Create your views here.

def retrieve_view(request):
      student= Student.objects.all()
      return render(request, 'crudApp/index.html', {'student': student})

def create_view(request):
      form = StudentForm()
      return render(request, 'crudApp/create.html', {'form': form})
