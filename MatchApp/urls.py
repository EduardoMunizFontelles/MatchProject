from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path, include

from MatchApp import views

urlpatterns = [
       path('', views.home, name='home'),
]