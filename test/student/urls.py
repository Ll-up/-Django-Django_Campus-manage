from django.contrib import admin
from django.urls import  path
from .views import Student_list,Student_create,Student_update,Student_delete

urlpatterns = [
    path("", Student_list.as_view(),name='student_list'), 
    path("create/", Student_create.as_view(),name='student_create'),
    path("<int:pk>/update/", Student_update.as_view(),name='student_update'),
    path("<int:pk>/delete/", Student_delete.as_view(),name='student_delete'),
]