from django.db import models
from customauth.models import MyUser
from datetime import datetime
from tinymce import models as tinymce_models

class Ajankohtaista(models.Model):
    '''Model for ajankohtaista article'''
    otsikko = models.CharField(max_length=200)
    teksti = tinymce_models.HTMLField() 
    pvm = models.DateTimeField(auto_now_add=False, default=datetime.now)
    
    def __str__(self):
        return self.otsikko
