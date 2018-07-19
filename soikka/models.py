from django.db import models
from customauth.models import MyUser
from datetime import datetime


class Ajankohtaista(models.Model):
    '''Model for ajankohtaista article'''
    otsikko = models.CharField(max_length=200)
    teksti = models.TextField(blank=True)
    pvm = models.DateTimeField(auto_now_add=False, default=datetime.now)

    def __str__(self):
        return self.otsikko
