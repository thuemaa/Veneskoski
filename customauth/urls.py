from django.urls import path
from . import views as account_views
from django.contrib.auth import views as auth_views
from .forms import LogInForm

urlpatterns = [
    path('', account_views.log_in, name='log_in'),
    path('signup/', account_views.sign_up, name='sign_up'),
    path('logout/', auth_views.logout, name='log_out'),
]