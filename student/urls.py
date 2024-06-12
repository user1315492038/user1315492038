from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from student import views

urlpatterns = [
    path('index/',views.index),
    path('details/',views.details),
    path('login/',views.login),
    path('logout/',views.logout),
    path('register/',views.register),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)