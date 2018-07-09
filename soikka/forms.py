from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.utils.translation import ugettext_lazy as _

# Form for creating user
class SignUpForm(UserCreationForm):

    email_errors = {
        'invalid': 'Epäkelpo säpö',
        'required': 'Syötä sähköposti',
    }

    email = forms.CharField(max_length=254, error_messages=email_errors, label='Sähköposti', required=True, widget=forms.EmailInput())
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
            'username': '',
        }

        error_messages = {
            'username': {
                'invalid':   'virheelline syöte',
                'required': 'Anna käyttäjätunnus',
            },
        }

    # change the default password labels, help text and error messages
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Salasana"
        self.fields['password2'].label = 'Vahvista salasana'
        self.fields['password1'].help_text = "Salasanan on oltava vähintään 8 merkkiä pitkä."
        self.fields['password2'].help_text = "Vahvista salasana"

        self.error_messages = {
            'password_mismatch': 'Salasanat eivät täsmää',
        }
        self.fields['password1'].error_messages = {
                'invalid': "ei kelpaa",
                'required': "an ny joku sala sana",
        }
        self.fields['password2'].error_messages = {
                'invalid': "ei kelpaa",
                'required': "an ny joku sala sana",
        }

