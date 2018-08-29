from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Ajankohtaista, Tapahtuma, Valokuva, TapahtumaOsallistuja, Vuokrattavana, Kesateatteri, Kesateatteri_naytelma

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
        kaikki_ajankohtaista = Ajankohtaista.objects.all().order_by('-pvm')
        paginator = Paginator(kaikki_ajankohtaista, 20)
        page = request.GET.get('sivu', 1)
        all_ak = paginator.get_page(page)
        return render(request, 'all_ajankohtaista.html', {'all_ak': all_ak})


def tapahtumat(request, tapahtuma_pk=None):
    """Get the tapahtuma object by primary key and pass it to template
    if no argument, show all tapahtuma objects"""
    if tapahtuma_pk:
        tapahtuma = get_object_or_404(Tapahtuma, pk=tapahtuma_pk)
        # Get all TapahtumaOsallistuja objects for this tapahtuma
        osallistujat = tapahtuma.tapahtumaosallistuja_set.all()

        # instantiate the variable
        user_attending = None
        # check if user is attending the event and set boolean according to result
        if request.user.is_authenticated:
            if osallistujat.filter(osallistuja=request.user).exists():
                user_attending = True
            else:
                user_attending = False

        return render(request, 'tapahtuma.html', {'tapahtuma': tapahtuma,
            'osallistujat': osallistujat, 'user_attending': user_attending})
    else:
        kaikki_tapahtumat = Tapahtuma.objects.all().order_by('-pvm')
        paginator = Paginator(kaikki_tapahtumat, 20)
        page = request.GET.get('sivu', 1)
        all_tapahtuma = paginator.get_page(page)
        otsikko = "Kaikki tapahtumat aikajärjestyksessä"
        return render(request, 'all_tapahtuma.html', {'all_tapahtuma': all_tapahtuma, 'otsikko': otsikko})

@login_required
def tapahtuma_osallistu(request, tapahtuma_pk):
    """add user to attend event
    TODO: create relation tapahtuma_pk and request.user. Check if relation exists before"""
    if not TapahtumaOsallistuja.objects.filter(tapahtuma=tapahtuma_pk, osallistuja=request.user).exists():
        tapahtuma = get_object_or_404(Tapahtuma, pk=tapahtuma_pk)
        uusi_ilmo = TapahtumaOsallistuja.objects.create(tapahtuma=tapahtuma, osallistuja=request.user)
        uusi_ilmo.save()
    return redirect('tapahtumat', tapahtuma_pk=tapahtuma_pk)

@login_required
def tapahtuma_peru(request, tapahtuma_pk):
    if TapahtumaOsallistuja.objects.filter(tapahtuma=tapahtuma_pk, osallistuja=request.user).exists():
        tapahtuma = get_object_or_404(Tapahtuma, pk=tapahtuma_pk)
        TapahtumaOsallistuja.objects.filter(tapahtuma=tapahtuma, osallistuja=request.user).delete()
    return redirect('tapahtumat', tapahtuma_pk=tapahtuma_pk)

def valokuvat(request):
    """Show list of valokuva objects."""
    all_valokuvat = Valokuva.objects.all().order_by('-pvm')
    pagi = Paginator(all_valokuvat, 10)
    page = request.GET.get('sivu')
    valokuvat = pagi.get_page(page)
    return render(request, 'valokuvat.html', {'valokuvat': valokuvat})


def ajax_image(request):
    """return image using ajax"""
    image_pk = request.GET['image_pk']
    valokuva = get_object_or_404(Valokuva, pk=image_pk)
    data = {
        'otsikko': valokuva.otsikko,
        'kuvaus': valokuva.kuvaus,
        'kuva': valokuva.kuva.url
    }
    return JsonResponse(data)


def vuokrattavana(request):
    """get only the latest object"""
    vuokrattavana = Vuokrattavana.objects.last()
    return render(request, 'vuokrattavana.html', {'vuokrattavana': vuokrattavana})

def kesateatteri(request):
    """Get only the latest view"""
    kesateatteri = Kesateatteri.objects.last()
    return render(request, 'kesateatteri.html', {'kesateatteri': kesateatteri})


def kesateatteri_naytelmat(request, naytelma_pk=None):
    """return of a list of all naytelma objects if no args given, or return a single naytelma"""
    if not naytelma_pk:
        """get all naytelma objects orderer by date, paginate them"""
        all_naytelmat = Kesateatteri_naytelma.objects.all().order_by('-naytos_loppu')
        pagi = Paginator(all_naytelmat, 20)
        page = request.GET.get('sivu')
        naytelmat = pagi.get_page(page)
        return render(request, 'all_naytelmat.html', {'naytelmat': naytelmat})

    else:
        naytelma = get_object_or_404(Kesateatteri_naytelma, pk=naytelma_pk)
        return render(request, 'naytelma.html', {'naytelma': naytelma})

