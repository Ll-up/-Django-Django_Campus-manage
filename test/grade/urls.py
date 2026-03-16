from django.contrib import admin
from django.urls import include, path
from .views import Grade_list,Grade_create,Grade_delete

urlpatterns = [
    path("", Grade_list.as_view(),name='grade_list'),
    path("create/", Grade_create.as_view(),name='grade_create'),
    path("<int:pk>/delete/", Grade_delete.as_view(),name='grade_delete'),
]