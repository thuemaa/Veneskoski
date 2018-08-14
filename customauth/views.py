from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LogInForm
from django.contrib.auth import authenticate, login


# function for logging in
def log_in(request):

    if request.method == 'POST':
        form = LogInForm(request.POST)
        email = request.POST.get('email')
        pw = request.POST.get('password')
        user = authenticate(username=email, password=pw)

        if user is not None:

            login(request, user)
            # Redirect to logged in users main page"
            return redirect("kylaindex")

        elif form.is_valid():
            form.add_error(None, "Sähköposti ja salasana ei täsmää!")

        else:
            form.add_error(None, "Sähköposti- ja salasankenttä on täytettävä")

    else:
        form = LogInForm()

    return render(request, 'log_in.html', {'form': form,})


# account creation
def sign_up(request):

    # redirect to another page if logged in

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Create new user here
            new_user = form.save()
            return redirect('home')
    else:
        form = CreateUserForm()

    return render(request, 'sign_up.html', {'form': form})
