from django.test import TestCase
from django.urls import resolve, reverse
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm, LogInForm
from .models import MyUser
from .views import sign_up, log_in


class SignUpTests(TestCase):

    # test sign up status code
    def test_status_code(self):
        url = reverse('sign_up')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # test sign up page resolve
    def test_signup_resolve(self):
        view = resolve('/kylalaisille/signup/')
        self.assertEquals(view.func, sign_up)

    #test account creation
    def test_signup_account_creation(self):

        usr = MyUser.objects.create(email='testi@kase.com', first_name="Esa", last_name="Pekka",
                                    password="kukuu")
        usr.save()


    # Test user creation form
    def test_signup_form(self):

        data = {'email': 'testi@sapo.onm', 'first_name': 'Testi', 'last_name': 'ukko',
                'password': 'passu123', 'password2': 'passu123'}

        form = CreateUserForm(data=data)
        self.assertTrue(form.is_valid())

    # test for invalid email
    def test_signup_form_fail(self):
        fail_data = {'email': 'testi@sapo.onm', 'first_name': 'Testi', 'last_name': 'ukko',
                    'password': 'passu123', 'password2': 'passu123'}
        fail_data['email'] = 'epakelposposti'
        form = CreateUserForm(data=fail_data)
        self.assertFalse(form.is_valid())

# Tests for logging user in
class LogInTests(TestCase):

    def setUp(self):
        usr = MyUser.objects.create(email='testi@kase.com', first_name="Esa", last_name="Pekka",
                                    password="kukuu")
        usr.save()

    # Test for logging in
    def test_authentication(self):
        usr = MyUser.objects.filter(email='testi@kase.com')[0]
        user = authenticate(email=usr.email, password=usr.password)

        if user is not None:
            if login(user):
                return True

    # Test log in form validity
    def test_log_in_success(self):

        data = {'email': 'testi@kase.com', 'password': 'passu123' }
        form = LogInForm(data=data)
        self.assertTrue(form.is_valid())

    # test for incomplete data and non field error for incomplete data
    def test_log_in_invalid_form(self):

        data = {'email': '', 'password': '123passu'}
        form = LogInForm(data=data)
        response = self.client.post('/kylalaisille/', data)
        self.assertFalse(form.is_valid())
        self.assertFormError(response, 'form', None, "Sähköposti- ja salasankenttä on täytettävä")

    # test non field errors
    def test_log_in_failure(self):

        data = {'email': 'testi@kase.com', 'password': '123passu'}
        response = self.client.post('/kylalaisille/', data)
        self.assertFormError(response, 'form', None, "Sähköposti ja salasana ei täsmää!")
