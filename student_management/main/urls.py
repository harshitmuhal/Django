from django.contrib import admin
from django.urls import path,include
from main import views

urlpatterns = [
    path('',views.index.as_view()), #for class based generic views we use as_view
    path('college/<int:pk>',views.collegdetails.as_view(),name='college_details_url'),
    path('college',views.collegelist.as_view()),
    #DetailView work only with pk or slugs
    path('create_college/', views.CollegeCreate.as_view()),
    path('update_college/<int:pk>', views.CollegeUpdate.as_view()),
    path('create_student/', views.StudentCreate.as_view()),
    path('delete_student/<int:pk>', views.StudentDelete.as_view()),
]
