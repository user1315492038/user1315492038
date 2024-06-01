from django.urls import path
from django.contrib import admin
from student import views

urlpatterns = [
    path('index/',views.index),
    path('login/',views.login),
    path('register/',views.register),
    path('logout/',views.logout)
]