from django.urls import path
from api import views

urlpatterns=[
    path('students/',views.StudentList.as_view()),
    path("students/<int:pk>", views.StudentDetailView.as_view()),
    path("deleteStudent/<int:pk>", views.StudentDeleteView.as_view()),
]
