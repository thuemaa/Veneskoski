from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ajankohtaista, Tapahtuma

# Homepage view
def home(request):
    '''Return the homepage view'''
    # Get the necessary models for main page
    # Get 5 latest ajankohtaista objects by date
    # ajankohtaista = Ajankohtaista.objects.all().order_by('-pvm')[:5]

    return render(request, 'home.html')


def ajankohtaista(request, ak_pk=None):
    """Get the ajankohtaista object by primary key and pass it to template
    If no argument, show all ajakohtaista objects"""
    if ak_pk:
        ajank = get_object_or_404(Ajankohtaista, pk=ak_pk)
        return render(request, 'ajankohtaista.html', {'ak': ajank})
    else:
        all_ak = Ajankohtaista.objects.all().order_by('-pvm')
        return render(request, 'all_ajankohtaista.html', {'all_ak': all_ak})


def tapahtumat(request, tapahtuma_pk=None):
    """Get the tapahtuma object by primary key and pass it to template
    if no argument, show all tapahtuma objects"""
    if tapahtuma_pk:
        tapahtuma = get_object_or_404(Tapahtuma, pk=tapahtuma_pk)
        return render(request, 'tapahtuma.html', {'tapahtuma': tapahtuma})
    else:
        all_tapahtuma = Tapahtuma.objects.all().order_by('-pvm')
        return render(request, 'all_tapahtuma.html', {'all_tapahtuma': all_tapahtuma})