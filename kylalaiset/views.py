from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from customauth.models import MyUser
import customauth.views as auth_views


def kylaindex(request):
    '''index for kylalaiset app, redirect to login if not logged in'''
    if not request.user.is_authenticated:
        #return HttpResponse("ei loganu sisää")
        return redirect(auth_views.log_in)
    else:
        return render(request, 'kylalaisetindex.html')

@login_required
def kayttaja(request):
    """User profile page"""
    kayttaja = request.user
    #kayttaja = get_object_or_404(MyUser, pk=user_pk)
    #kokonimi = kayttaja.first_name + " " + kayttaja.last_name
    return render(request, 'profiili.html', {'user': kayttaja})
    #return HttpResponse(kokonimi)
