from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.utils.translation import ugettext_lazy as _

# Form for creating user
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, label='Sähköposti', required=True, widget=forms.EmailInput())
    class Meta:
        model = User

        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        labels = {
            'username': 'Käyttäjätunnus',
            'first_name': 'Etunimi',
            'last_name': 'Sukunimi',
            'email': 'Sähköposti',
        }

        help_texts = {
            'username': 'anna käytäjä nime',
            'password1': 'juu an kuule sala_sana',
        }

        error_messages = {
            'username': {
                'invalid':   'virheelline syöte',
                'required': 'Anna käyttäjätunnus',
            }
        }

    # change the default password labels and help text
    def __init__(self):
        super(UserCreationForm, self).__init__()
        self.fields['password1'].label = "Salasana"
        self.fields['password2'].label = 'Vahvista salasana'
        self.fields['password1'].help_text = "an kuule salaa sana"
        self.fields['password2'].help_text = "Vahvista salasana"

