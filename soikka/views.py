from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Ajankohtaista

# Homepage view
def home(request):
    return render(request, 'home.html')


def ajankohtaista(request):
    ak = Ajankohtaista.objects.last()
    return render(request, 'ajankohtaista.html', {'ak': ak})
