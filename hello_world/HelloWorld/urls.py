from django.urls import path
from HelloWorld import views

#every urls file in python must contain this variable urlpatterns
#urlpatterns is a list of all the paths that this url path maps to

# every path is mapped to a view
urlpatterns = [
    path('',views.index),
]


# path('',views.index) = In the main urls.py file this url file will be called for path hello/ so empty path here means hello/