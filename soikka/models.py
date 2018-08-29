from django.db import models
from customauth.models import MyUser
from datetime import datetime
from tinymce import models as tinymce_models
from filebrowser.fields import FileBrowseField
from filebrowser.sites import FileBrowserSite


class Ajankohtaista(models.Model):
    """Model for ajankohtaista article"""
    otsikko = models.CharField(max_length=200)
    kuvaus = models.TextField(max_length=1000)
    teksti = tinymce_models.HTMLField() 
    pvm = models.DateTimeField(auto_now_add=False, default=datetime.now)
    tekija = models.ForeignKey(MyUser, related_name='user_ajankohtaista', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.otsikko

class Tapahtuma(models.Model):
    """Model for tapahtuma
    TODO: Remove null=True from tekija"""
    otsikko = models.CharField(max_length=200)
    kuvaus = models.TextField(max_length=1000)
    teksti = tinymce_models.HTMLField()
    pvm = models.DateTimeField(auto_now_add=False, default=datetime.now)
    tekija = models.ForeignKey(MyUser, related_name='user_tapahtumat', on_delete=models.CASCADE)    

    def __str__(self):
        return self.otsikko

class TapahtumaOsallistuja(models.Model):
    """Model for tapahtuma (event) attendee"""
    tapahtuma = models.ForeignKey(Tapahtuma, on_delete=models.CASCADE)
    osallistuja = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    ilmottautumis_aika = models.DateTimeField(auto_now_add=True)

class Valokuva(models.Model):
    """model for valokuva, image object"""
    otsikko = models.CharField(max_length=100)
    kuvaus = models.TextField(max_length=1000, default=None)
    # USING FileBrowseField instead
    # kuva = models.ImageField(upload_to='kuvat', default=None)
    kuva = FileBrowseField("Kuva", max_length=3000)
    pvm = models.DateTimeField(auto_now_add=False, default=datetime.now)

    def __str__(self):
        return self.otsikko

class Kesateatteri(models.Model):
    """Model for kesäteatteri main page."""
    otsikko = models.CharField(max_length=100)
    sisalto = tinymce_models.HTMLField()
    paivitetty = models.DateTimeField(auto_now_add=False, default=datetime.now)

    def __str__(self):
        return self.otsikko

class Kesateatteri_naytelma(models.Model):
    """Model for single theater act. Contains info such as starting and ending date, name, organizer"""
    nimi = models.CharField(max_length=100)
    esittaja = models.CharField(max_length=100)
    sisalto = tinymce_models.HTMLField()
    naytos_alku = models.DateField(auto_now_add=False)
    naytos_loppu = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.nimi


class Vuokrattavana(models.Model):
    """model for vuokrattavana. page uses only last object"""
    otsikko = models.CharField(max_length=100)
    sisalto = tinymce_models.HTMLField()
    paivitetty = models.DateField(auto_now=True)
