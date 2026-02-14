from django.shortcuts import render, redirect
from django.http import HttpResponse
from crudApp.models import Student
from crudApp.forms import StudentForm

# Create your views here.

def retrieve_view(request):
      student= Student.objects.all()
      return render(request, 'crudApp/index.html', {'student': student})

def create_view(request):
      form = StudentForm()
      if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                  form.save()  
                  return redirect('/student')
      return render(request, 'crudApp/create.html', {'form': form})


def Delete_view(request, id):
      student= Student.objects.get(id=id)
      student.delete()
      return redirect('/student')
      
