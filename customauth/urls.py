from django.urls import path
from . import views as account_views
from django.contrib.auth import views as auth_views
from .forms import LogInForm

urlpatterns = [
    path('edit_user/', account_views.edit_user, name='edit_user'),
    path('login/', account_views.log_in, name='log_in'),
    path('logout/', auth_views.LogoutView.as_view(), name='log_out'),
    path('signup/', account_views.sign_up, name='sign_up'),
    path('logout/', auth_views.logout, name='log_out'),
]


# path('', auth_views.LoginView.as_view(template_name='log_in.html'), name='log_in')
