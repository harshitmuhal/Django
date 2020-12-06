from django.urls import path,include
from main import views

urlpatterns = [
    path('',views.index),
    path('student',views.student_print),
    path('add_student',views.add_student)
]
