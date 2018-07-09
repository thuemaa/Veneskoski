from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Homepage view
def homepage(request):
    return render(request, 'home.html')


# account creation
def sign_up(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            return redirect('homepage')
    else:
        form = SignUpForm()

    return render(request, 'sign_up.html', {'form': form})
