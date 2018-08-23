from django import forms
from filebrowser.base import FileObject
from .models import Markkina

class MarkkinaForm(forms.ModelForm):


    class Meta:
        model = Markkina
        # fields = '__all__'
        fields = ['otsikko', 'ilmoitustyyppi', 'teksti', 'kuva']
