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

def author(request,pk):
    author = get_object_or_404(models.Author, pk = pk)
    context = {
        "author": author
    }
    return render(request, 'main/author.html', context)

def create_article(request):
    authors = models.Author.objects.all()
    context = {
    "authors": authors
    }

    if request.method == "POST":
        article_data = {
            "title": request.POST['title'],
            "content": request.POST['content']
        }
        # HttpRequest.POST
        # A dictionary-like object containing all given HTTP POST parameters, providing that the
        # request contains form data. If you need to access raw or non-form data posted in the
        # request, access this through the HttpRequest.body attribute instead.POST does not include
        # file-upload information.

        # HttpRequest.FILES
        # A dictionary-like object containing all uploaded files. Each key in FILES is the name from the
        # <input type="file" name="">. Each value in FILES is an UploadedFile. FILES will only contain
        # data if the request method was POST and the <form> that posted to the request had
        # enctype="multipart/form-data". Otherwise, FILES will be a blank dictionary-like object.

        article = models.Article.objects.create(**article_data)
        author = models.Author.objects.filter(pk = request.POST['author'])
        article.authors.set(author)
        context["success"] = True

    return render(request, 'main/create_article.html', context)
