from django.urls import path
from api import views

urlpatterns=[
    path('users/',views.usersapi),
    # path('articles/',views.Article_api),
    path('articles/',views.ArticleList.as_view()),
    path('articles/<int:pk>',views.ArticleDetail.as_view()),
    path('createarticle/',views.createarticle),
]
