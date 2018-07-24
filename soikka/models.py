from django.db import models
from customauth.models import MyUser
from datetime import datetime
from tinymce import models as tinymce_models

class Ajankohtaista(models.Model):
    """Model for ajankohtaista article"""
    otsikko = models.CharField(max_length=200)
    teksti = tinymce_models.HTMLField() 
    pvm = models.DateTimeField(auto_now_add=False, default=datetime.now)
    
    def __str__(self):
        return self.otsikko


class Valokuva(models.Model):
    """model for valokuva, image object"""
    otsikko = models.CharField(max_length=100)
    kuvaus = models.TextField(max_length=1000)
    kuva = models.ImageField(upload_to='kuvat', default=None)
    pvm = models.DateTimeField(auto_now_add=False, default=datetime.now)

    def __str__(self):
        return self.otsikko
