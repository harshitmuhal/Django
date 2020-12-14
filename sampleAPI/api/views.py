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

# class based views
from rest_framework.generics import ListAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView

class ArticleList(ListAPIView):
    serializer_class=serializers.ArticleSerializer
    queryset=models.Article.objects.all() # Compulsary parameter

class ArticleDetail(RetrieveAPIView):
    serializer_class=serializers.ArticleSerializer
    queryset=models.Article.objects.all() # Compulsary parameter

class ArticlesDetailView(RetrieveUpdateAPIView):
    # RetrieveUpdateAPIView : If there is a get request then article will be fetched
    # if request is patch then article will be updated.
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

# class ArticlesDetailView(ListCreateAPIView):
#     # ListCreateAPIView : get request = list of all articles
#     # post request : create a new article with given body
#     queryset = models.Article.objects.all()
#     serializer_class = serializers.ArticleSerializer

# OR

class ArticlesDetailView(ListCreateAPIView):
    serializer_class = serializers.ArticleSerializer

    def get_queryset(self):
        # URls may contain parameters www.domain.com/so_and_so?key=x&key2=y
        # self.request.GET gives us these parameters
        query = {} # To get only those articles in queryset as requested by user
        # for ex - user may request to get only articles with tags : language
        for key, value in self.request.GET.items():
            query["{}__icontains".format(key)] = value
        return models.Article.objects.filter(**query) # unpacking using **
