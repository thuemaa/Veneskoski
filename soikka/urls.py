from django.urls import path
from . import views
from django.contrib.auth import views as authviews

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup', views.sign_up, name='sign_up'),
]