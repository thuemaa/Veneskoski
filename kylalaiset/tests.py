from django.test import TestCase, Client
from django.urls import reverse, resolve
from customauth.models import MyUser


class KylalaisetLinkTest(TestCase):

    def SetUp(self):
        # TODO: Fix the login. Tests fail because respons is 302 (redirect) instead of 200
        """set up login for the tests"""
        self.client = Client()
        self.email = 'tuomas.kaappa@gmail.com'
        self.password = 'salasana'
        self.usr = MyUser.objects.create_user(email=self.email, first_name='Tuomas', last_name='Kaappa',
                                         password=self.password)
        self.usr.set_password(self.password)
        self.usr.is_admin = True
        self.usr.is_superuser = True
        self.usr.is_staff = True
        self.usr.save()
        login = self.client.login(username=self.email, password=self.password)
        self.assertEqual(login, True)

    def test_markkinapaikka_status_code(self):
        url = reverse('markkina')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_uusi_markkina_status_code(self):
        url = reverse('uusi_markkina')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_profiili_status_code(self):
        url = reverse('kayttaja')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_omat_tapahtumat_status_code(self):
        url = reverse('omat_tapahtumat')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_omat_ilmoitukset_status_code(self):
        url = reverse('omat_ilmoitukset')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_logout_status_code(self):
        url = reverse('log_out')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
