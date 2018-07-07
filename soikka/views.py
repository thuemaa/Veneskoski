from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

# Homepage view
def homepage(request):
    return render(request, 'home.html')


# account creation
def sign_up(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

    else:
        form = UserCreationForm()

    return render(request, 'sign_up.html', {'form': form})
