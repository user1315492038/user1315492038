from django.urls import path
from django.contrib import admin
from . import views

app_name = 'student'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('index/',views.index),
    path('login/',views.login),
    path('register/',views.register),
    path('logout/',views.logout)
]