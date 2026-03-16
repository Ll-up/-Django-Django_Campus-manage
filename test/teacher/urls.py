from django.contrib import admin
from django.urls import include, path
from .views import Teacher_list,Teacher_create,Teacher_delete,Teacher_update,TeacherList

urlpatterns = [
    path("", Teacher_list.as_view(),name='teacher_list'),
    path("create/", Teacher_create.as_view(),name='teacher_create'),
    path("<int:pk>/update/", Teacher_update.as_view(),name='teacher_update'),
    path("<int:pk>/delete/", Teacher_delete.as_view(),name='teacher_delete'),
    path("api/", TeacherList.as_view(),name='TeacherList'),
    path('api/<int:pk>/', TeacherList.as_view()),
]