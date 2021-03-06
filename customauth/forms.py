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

class EditUserForm(forms.ModelForm):
    """form for updating user"""

    # instantiate the flag to false
    wrong_password_flag = False

    password_errors = {
        'invalid': 'Salasana ei kelpaa',
        'required': 'Syötä salasana',
    }

    new_password = forms.CharField(label='Uusi salasana', error_messages=password_errors, widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Vahvista salasana', error_messages=password_errors, widget=forms.PasswordInput)
    old_password = forms.CharField(label='Vanha salasana', error_messages=password_errors, widget=forms.PasswordInput)

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

    def set_wrong_password_flag(self):

        # set flag to true if old password does not match
        self.wrong_password_flag = True

    def clean(self):

        cleaned_data = self.cleaned_data

        new_password = cleaned_data.get("new_password")
        new_password2 = cleaned_data.get("new_password2")
        old_password = cleaned_data.get("old_password")

        if new_password and new_password2 and new_password != new_password2:
            self.add_error('new_password2', "Salasanat eivät täsmää!")

        # raise error if flag is set to true
        if self.wrong_password_flag:
            self.add_error('old_password', 'Vanha salasana väärä')

        return super(EditUserForm, self).clean()

    def save(self, commit=True):

        user = super(EditUserForm, self).save(commit=False)

        user.set_password(self.cleaned_data['new_password'])

        if commit:
            user.save()

        return user

class LogInForm(forms.Form):

    password_errors = {
        'invalid': 'Salasana ei kelpaa',
        'required': 'Syötä salasana',
    }

    email_errors = {
        'invalid': 'Sähköpostiosoite ei ole kelvollinen',
        'required': 'Anna säpöosote'
    }

    email = forms.EmailField(label='Sähköposti', error_messages=email_errors)
    password = forms.CharField(label='Salasana', error_messages=password_errors, widget=forms.PasswordInput)
