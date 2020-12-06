from django.contrib import admin
from django.urls import path,include
from main import views
urlpatterns = [
    path('',views.index,name='main_page'),
    path('article/<int:pk>',views.article,name='get_article'),
]


# To capture a value from the URL, use angle brackets.
# Captured values can optionally include a converter type. For example, use <int:name> to
# capture an integer parameter. If a converter isn’t included, any string, excluding a / character,
# is matched.
