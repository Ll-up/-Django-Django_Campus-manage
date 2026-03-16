from django.contrib import admin
from django.urls import include, path
from .views import main_t

urlpatterns = [
    path("", main_t)
]
