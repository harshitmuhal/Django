from django.urls import path
from api import views

urlpatterns=[
    path('users/',views.usersapi),
    path('articles/',views.Article_api),
    path('createarticle/',views.createarticle),
]
