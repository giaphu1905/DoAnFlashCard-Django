from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "user"

urlpatterns = [
    path('profile/', views.profile_user, name='hoso'),
]