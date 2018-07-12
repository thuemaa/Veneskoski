from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import MyUser


# Form for creating MyUser
class CreateUserForm(forms.ModelForm):

    password_errors = {
        'invalid': 'Salasana ei kelpaa',
        'required': 'Syötä salasana',
    }

    password = forms.CharField(label='Salasana', error_messages=password_errors, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Vahvista salasana', error_messages=password_errors, widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name')

        labels = {
            'username': 'Käyttäjätunnus',
            'first_name': 'Etunimi',
            'last_name': 'Sukunimi',
            'email': 'Sähköposti',
        }

        help_texts = {
            'password1': '',
        }

        error_messages = {
            'email': {
                'invalid': 'Sähköpostiosoite ei ole kelvollinen',
                'required': 'Syötä sähköpostiosoite',
            },
            'first_name': {
                'invalid': 'Nimi ei kelpaa',
                'required': 'Syötä etunimi',
            },
            'last_name': {
                'invalid': 'Nimi ei kelpaa',
                'required': 'Syötä etunimi',
            }
        }

    def clean(self):

        cleaned_data = self.cleaned_data

        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error('password2', "Salasanat eivät täsmää!")

        return super(CreateUserForm, self).clean()

    def save(self, commit=True):

        user = super(CreateUserForm, self).save(commit=False)

        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class LogInForm(forms.ModelForm):

    password_errors = {
        'invalid': 'Salasana ei kelpaa',
        'required': 'Väärä salasana',
    }

    password = forms.CharField(label='Salasana', error_messages=password_errors, widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email',)

        labels = {
            'email': 'Sähköposti',
            'password': 'Salasana',
        }
