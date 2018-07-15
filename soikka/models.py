from django.db import models
from customauth.models import MyUser


#
class Ajankohtaista(models.Model):
    otsikko = models.CharField(max_length=200)
    teksti = models.TextField()


    def __str__(self):
        return self.otsikko