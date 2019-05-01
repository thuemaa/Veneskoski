from django import forms
from filebrowser.base import FileObject
from .models import Markkina

class MarkkinaForm(forms.ModelForm):


    class Meta:
        model = Markkina
        # fields = '__all__'
        fields = ['otsikko', 'ilmoitustyyppi', 'teksti', 'kuva']

        error_messages = {
            'otsikko': {
                'invalid': 'Virheellinen otsikko',
                'required': 'Anna ilmoitukselle otsikko',
            },
            'ilmoitustyyppi': {
                'invalid': 'Syöte ei kelpaa',
                'required': 'Valitse ilmoitustyyppi',
            },
            'teksti': {
                'invalid': 'Liian pitkä teksti',
                'required': 'Kirjoita lyhyt kuvaus ilmoituksesta',
            },
            'kuva': {
                'invalid_image': 'Virheellinen kuvatiedosto.',
                'required': ''
            }
        }