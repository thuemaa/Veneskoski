from django import template
from soikka.models import Ajankohtaista, Tapahtuma

register = template.Library()

@register.inclusion_tag('links/aklinks.html')
def show_ak(ajankohtaista):
    ajankohtaista = Ajankohtaista.objects.all().order_by('-pvm')[:5]
    return {'ajankohtaista': ajankohtaista}

@register.inclusion_tag('links/tapahtumalinks.html')
def show_tapahtuma(tapahtuma):
    tapahtumat = Tapahtuma.objects.all().order_by('-pvm')[:5]
    return {'tapahtumat': tapahtumat}
