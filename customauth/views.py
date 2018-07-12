from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LogInForm
from .models import MyUser
# Create your views here.


def log_in(request):

    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})


# account creation
def sign_up(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Create new user here
            new_user = form.save()
            return redirect('homepage')
    else:
        form = CreateUserForm()

    return render(request, 'sign_up.html', {'form': form})