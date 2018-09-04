from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ajankohtaista/<int:ak_pk>/', views.ajankohtaista, name='ajankohtaista'),
    path('ajankohtaista/', views.ajankohtaista, name='ajankohtaista'),
    path('kesateatteri/naytelmat/<int:naytelma_pk>/', views.kesateatteri_naytelmat, name='naytelmat'),
    path('kesateatteri/naytelmat/', views.kesateatteri_naytelmat, name='naytelmat'),
    path('kesateatteri/', views.kesateatteri, name='kesateatteri'),
    path('tapahtumat/<int:tapahtuma_pk>/ilmottaudu/', views.tapahtuma_osallistu, name='tapahtuma_osallistu'),
    path('tapahtumat/<int:tapahtuma_pk>/peru/', views.tapahtuma_peru, name='tapahtuma_peru'),
    path('tapahtumat/<int:tapahtuma_pk>/', views.tapahtumat, name='tapahtumat'),
    path('tapahtumat/', views.tapahtumat, name='tapahtumat'),
    path('valokuvat/<int:valokuva_pk>/', views.valokuvat, name='valokuvat'),
    path('valokuvat/', views.valokuvat, name='valokuvat'),
    path('vuokrattavana/', views.vuokrattavana, name='vuokrattavana'),
    path('yhdistykset/', views.yhdistykset, name='yhdistykset'),
    path('ajax/image/', views.ajax_image, name='ajax_image'),
]
