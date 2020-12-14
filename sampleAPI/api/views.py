from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from api import serializers
from api import models
# without the decorator by sending users it is treated as html response but while
# making api most common is json response and to return json response we use this decorator

# Because of this decorator the view will treat the request as a json api response

# If this decorator is not here request is of type HttpResponse and even with HttpResponse(json.dumps(users))
# Output sent to the client will be an HttpResponse (check using postman)

# Not every python object is serialosable for example: if you pass a class object in Response Function
# then it will not be serialisable.

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

@api_view()
def usersapi2(request):

    users=[
        {
        'name': 'harshit',
        'language': 'python'
        },
        {
        'name': 'jatin',
        'language': 'c++'
        }
    ]

    return Response(users)

@api_view()
def usersapi(request):
    student1=Student('Harshit',1)
    student2=Student('Sakshi',2)
    student3=Student('Priyanka',3)
    # users will be serialised to json object automatically
    response=serializers.StudentSerializer([student1,student2,student3],many=True) #many=true tells that list of students is there
    return Response(response.data)

@api_view()
def Article_api(request):
    articles=models.Article.objects.all()
    response=serializers.ArticleSerializer(articles,many=True)
    return Response(response.data)

@api_view(['POST']) #List contains all types of requests that the view will support
def createarticle(request):
    #Took json data in request
    body=json.loads(request.body) # de-serialising json data using json library into a python dictionary
    # Now when deserializing data, we can call .save() to return an object instance, based on the validated data.
    response=serializers.ArticleSerializer(body,many=False)
    if response.is_valid():
        article_instance=response.save()
        # Calling .save() will either create a new instance, or update an existing instance, depending on if an
        # existing instance was passed when instantiating the serializer class.
        response=serializers.ArticleSerializer(article_instance) #response from newly saved article instead of user input response
        return Response(response.body)

    return Response(response.errors)
