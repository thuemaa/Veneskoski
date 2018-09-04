from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from customauth.models import MyUser
import customauth.views as auth_views
from .models import Markkina
from .forms import MarkkinaForm
from soikka.models import Tapahtuma, TapahtumaOsallistuja

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

@login_required
def markkina(request, ilmoitus_pk=None):
    """get all markkina objects or a single one if arg"""
    if ilmoitus_pk:
        ilmoitus = get_object_or_404(Markkina, pk=ilmoitus_pk)
        return render(request, 'markkina.html', {'ilmoitus': ilmoitus})

    kaikki_ilmoitukset = Markkina.objects.all().order_by('-pk')
    return render(request, 'all_markkina.html', {'kaikki_ilmoitukset': kaikki_ilmoitukset})

@login_required
def uusi_markkina(request):
    """form page for markkina object"""
    if request.method == 'POST':
        form = MarkkinaForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.ilmoittaja = request.user
            image.save()

            return redirect('markkina')
    else:
        form = MarkkinaForm()

    return render(request, 'uusi_markkina.html', {'form': form})

@login_required
def omat_ilmoitukset(request):
    """view all user markkina objects"""
    ilmoittaja = request.user
    kaikki_ilmoitukset = Markkina.objects.filter(ilmoittaja=ilmoittaja)
    return render(request, 'all_markkina.html', {'kaikki_ilmoitukset': kaikki_ilmoitukset})

@login_required
def omat_tapahtumat(request):
    """get all tapahtuma objects user is attending"""
    # Get all primary keys of Tapahtuma objects user is attending.
    all_tapahtuma_pks = TapahtumaOsallistuja.objects.values_list('tapahtuma', flat=True).filter(osallistuja=request.user)
    # get all tapahtuma objects by pk's
    kaikki_tapahtumat = Tapahtuma.objects.filter(pk__in=all_tapahtuma_pks)
    # paginate them
    paginator = Paginator(kaikki_tapahtumat, 20)
    page = request.GET.get('sivu', 1)
    all_tapahtuma = paginator.get_page(page)
    # use same template as all_tapahtuma
    # set the header
    otsikko = "Tapahtumat johon olet ilmottautunut"
    return render(request, 'all_tapahtuma.html', {'all_tapahtuma': all_tapahtuma, 'otsikko': otsikko})
