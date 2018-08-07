from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ajankohtaista/<int:ak_pk>/', views.ajankohtaista, name='ajankohtaista'),
    path('ajankohtaista/', views.ajankohtaista, name='ajankohtaista'),
    path('tapahtumat/<int:tapahtuma_pk>/', views.tapahtumat, name='tapahtumat'),
    path('tapahtumat/', views.tapahtumat, name='tapahtumat'),
    path('valokuvat/<int:valokuva_pk>/', views.valokuvat, name='valokuvat'),
    path('valokuvat/', views.valokuvat, name='valokuvat'),
]
