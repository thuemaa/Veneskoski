from django.urls import path
from . import views

urlpatterns = [
    path('', views.kylaindex, name='kylaindex'),
    path('profiili/ilmoitukset/', views.omat_ilmoitukset, name='omat_ilmoitukset'),
    path('profiili/tapahtumat/', views.omat_tapahtumat, name='omat_tapahtumat'),
    path('profiili/', views.kayttaja, name='kayttaja'),
    path('markkinapaikka/uusi/', views.uusi_markkina, name='uusi_markkina'),
    path('markkinapaikka/<int:ilmoitus_pk>/', views.markkina, name='markkina'),
    path('markkinapaikka/', views.markkina, name='markkina'),
]
