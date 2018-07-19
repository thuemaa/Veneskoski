from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ajankohtaista

# Homepage view
def home(request):
    '''Return the homepage view'''
    # Get the necessary models for main page
    # Get 5 latest ajankohtaista objects by date
    # ajankohtaista = Ajankohtaista.objects.all().order_by('-pvm')[:5]

    return render(request, 'home.html')


def ajankohtaista(request, ak_pk):
    '''Get the ajankohtaista object by primary key and pass it to template'''
    ajank = get_object_or_404(Ajankohtaista, pk=ak_pk)
    return render(request, 'ajankohtaista.html', {'ak': ajank})
