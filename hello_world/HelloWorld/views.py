
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    response=HttpResponse("Hello World")
    return response

def index2(request):
    family={'Harshit','Sakshi','Priyanka','Mom','Dad'}
    developer='harshit'
    context={
        'family':family,
        'developer':developer
    }
    response=render(request,'HelloWorld/index.html',context=context)
    return response
