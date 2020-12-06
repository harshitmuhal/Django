from django.shortcuts import render
from main import forms


# Create your views here.
def index(request):
    context={
    'form':forms.my_form,
    }
    response=render(request,'index.html',context=context)
    return response
