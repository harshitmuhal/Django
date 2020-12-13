from django.db import models

# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        self.name

class Article(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=200)
    description=models.TextField()
    body=models.TextField()
    tags = models.ManyToManyField('Tag', blank = True)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now_add = True)
    favourited = models.BooleanField()
    favouriteCount = models.IntegerField(default = 0)

    def __str__(self):
        self.title
