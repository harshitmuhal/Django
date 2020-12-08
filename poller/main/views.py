from django.shortcuts import render
from django.views.generic import ListView, DetailView
from main import models


# Create your views here.
class index(ListView):
    model=models.question
    template_name = 'main/index.html'

class question_detail(DetailView):
    model=models.question
    template_name='main/question.html'
