from django.db import models
from customauth.models import MyUser
from filebrowser.fields import FileBrowseField


class Markkina(models.Model):
    """Model for markkinapaikka object"""

    MYYNTI = 'myynti'
    OSTO = 'osto'
    ANTO = 'anto'
    VUOKRA = 'vuokra'

    ILMOITUSTYYPPI_VALINNAT = (
        (MYYNTI, 'Myydään'),
        (OSTO, 'Ostetaan'),
        (ANTO, 'Annetaan'),
        (VUOKRA, 'Vuokrataan'),
    )

    otsikko = models.CharField(max_length=100)
    ilmoitustyyppi = models.CharField(max_length=6, choices=ILMOITUSTYYPPI_VALINNAT, default=MYYNTI)
    kuva = FileBrowseField("ilmoitus_kuva", max_length=2560)
    teksti = models.TextField()
    pvm = models.DateTimeField(auto_now_add=True)
    ilmoittaja = models.ForeignKey(MyUser, related_name='user_markkina', on_delete=models.CASCADE)

    def __str__(self):
        return self.otsikko