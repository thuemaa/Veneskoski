from django.urls import path
from . import views
from django.contrib.auth import views as authviews

urlpatterns = [
    path('', views.homepage, name='homepage'),
]