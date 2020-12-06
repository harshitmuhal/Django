from django.shortcuts import render
from main import forms
from main import models
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    context={
    'form':forms.my_form,
    }
    response=render(request,'index.html',context=context)
    return response

def student_print(request):
    students=models.student.objects.all()
    context={
    'students':students,
    }
    return render(request,'students.html',context=context)

def add_student(request):
    studentform = forms.student_form()
    if request.method == "POST":
        studentform = forms.student_form(request.POST)
    if studentform.is_valid(): #call the is_valid() method to run validation and return a boolean
                               # designating whether the data was valid. It runs validation checks
      student = studentform.save()
      return HttpResponseRedirect('/student')
    context={
    'studentform':studentform,
    }
    return render(request,'addstudent.html',context=context)
