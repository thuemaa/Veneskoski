from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

#Homepage view
def homepage(request):
    return render(request, 'home.html')
