from django.shortcuts import render,get_object_or_404
from django.http import Http404
from main import models
# Create your views here.

def index(request):
    latest_articles=models.Article.objects.all().order_by('-createdAt')[:10] # - sign means descending order
    context={
    'latest_articles':latest_articles,
    }
    resp=render(request,'main/index.html',context=context)
    return resp

def article(request,pk):
    # try:
    #     #pk in django is an indentifier we use for primary key of the models
    #     art=models.Article.objects.get(pk=pk)
    # except:
    #     raise Http404()
    # OR
    art=get_object_or_404(models.Article, pk = pk)
    context={
    'article':art,
    }
    return render(request,'main/article.html',context=context)
