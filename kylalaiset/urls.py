from django.urls import path
from . import views

urlpatterns = [
    path('', views.kylaindex, name='kylaindex'),
    path('profiili/', views.kayttaja, name='kayttaja'),
    path('markkinapaikka/', views.markkina, name='markkina'),
]
