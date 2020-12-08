from django.urls import path
from main import views

urlpatterns=[
    path('',views.index.as_view(),name='question_page'),
    path('question/<slug>',views.question_detail.as_view(),name='question'),
]
