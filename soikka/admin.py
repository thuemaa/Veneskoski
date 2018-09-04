import os
from django.contrib import admin
from .models import Ajankohtaista, Valokuva, Tapahtuma, Kesateatteri, Kesateatteri_naytelma, TapahtumaOsallistuja, Vuokrattavana , Yhdistykset

class CustomAdmin(admin.ModelAdmin):
    """NOT IN USE. Change the second path to tinymce_setup config later for adjusting theme and view"""
    class Media:
        js = [os.path.join('/static', 'tiny_mce/tiny_mce.js'),
              os.path.join('/static', 'js/tinymce_setup.js')]


admin.site.register(Ajankohtaista)
admin.site.register(Valokuva)
admin.site.register(Tapahtuma)
admin.site.register(Kesateatteri)
admin.site.register(Kesateatteri_naytelma)
admin.site.register(TapahtumaOsallistuja)
admin.site.register(Vuokrattavana)
admin.site.register(Yhdistykset)
