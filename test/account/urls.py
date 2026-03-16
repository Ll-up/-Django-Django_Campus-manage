from django.contrib import admin
from django.urls import path
from .views import main_l, login_view, register_view, logout_view

urlpatterns = [
    path("", main_l, name='login'),
    path("login/", login_view, name='login_view'),
    path("register/", register_view, name='register'),
    path("logout/", logout_view, name='logout'),
]
