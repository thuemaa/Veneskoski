from django.db import models
from customauth.models import MyUser
from django.core.files.base import ContentFile
from PIL import Image as PIL_Image
from io import BytesIO
import os

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
    kuva = models.ImageField(upload_to='markkina/kuvat', default="emptymarket.jpg")
    thumbnail = models.ImageField(upload_to='markkina/thumbnail', blank=True)
    teksti = models.TextField()
    pvm = models.DateTimeField(auto_now_add=True)
    ilmoittaja = models.ForeignKey(MyUser, related_name='user_markkina', on_delete=models.CASCADE)

    def __str__(self):
        return self.otsikko

    # custom save, required for thumbnail
    def save(self, *args, **kwargs):

        '''TODO later on: check if no img in post
        if self.kuva.default:
            self.thumbnail = self.kuva
            super(Markkina, self).save(*args, **kwargs)
        '''

        if not self.create_thumbnail():
            raise Exception('error creating thumbnail.')

        super(Markkina, self).save(*args, **kwargs)

    def create_thumbnail(self):
        img = PIL_Image.open(self.kuva)

        # max 300px
        size = (300, 300)

        # Set thumbail filename
        t_name, t_ext = os.path.splitext(self.kuva.name)
        thumbnail_filename = t_name + '_t' + t_ext

        img.thumbnail(size, PIL_Image.ANTIALIAS)
        temp_thumb = BytesIO()

        if t_ext in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif t_ext == '.gif':
                FTYPE = 'GIF'
        elif t_ext == '.png':
                FTYPE = 'PNG'
        else:
           return False

        img.save(temp_thumb, FTYPE)

        temp_thumb.seek(0)
        self.thumbnail.save(thumbnail_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True
