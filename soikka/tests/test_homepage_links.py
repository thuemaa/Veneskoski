from django.test import TestCase
from django.urls import reverse, resolve
from datetime import datetime
from soikka.views import home, ajankohtaista, tapahtumat
from soikka.models import Ajankohtaista, Tapahtuma
from customauth.models import MyUser
from kylalaiset.views import kylaindex
'''
TEST:

    LINKS: home, kylalaisille,
    MODELS: Ajankohtaista, Kuva, Tapahtuma, Kesateatteri, Vuokrattavana
'''

class HomePageLinksTests(TestCase):

    def setUp(self):
        """Create models for testing links"""
        usr = MyUser.objects.create_user(email='tuomas.kaappa@gmail.com', first_name='Tuomas', last_name='Kaappa',
                                         password='salasana')
        usr.is_admin = True
        usr.is_superuser = True
        usr.is_staff = True
        usr.save()
        # create 5 ajankohtaista & tapahtuma objects
        for i in range(0, 5):
            Ajankohtaista.objects.create(otsikko='Otsikko '+str(i), teksti='Teksti ' + str(1), pvm=datetime.now(),
                                         kuvaus="blaablaa", tekija=usr)
            Tapahtuma.objects.create(otsikko='Otsikko ' + str(i), teksti='Teksti ' + str(1), pvm=datetime.now(),
                                         kuvaus="blaablaa", tekija=usr)

    def test_homepage_status_code(self):
        """Test status code for homepage"""
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_homepage_view_func(self):
        page = resolve('/')
        self.assertEquals(page.func, home)
    
    def test_anakohtaista_status_code(self):
        for i in range(1, 7):
            url = reverse('ajankohtaista', kwargs={'ak_pk': i})
            response = self.client.get(url)
            if i == 6:
                self.assertEquals(response.status_code, 404)
            else:
                self.assertEquals(response.status_code, 200)

    def test_ajankohtaista_view_func(self):
        for i in range(1, 6):
            page = resolve('/ajankohtaista/' + str(i) + '/')
            self.assertEquals(page.func, ajankohtaista)

    def test_tapahtuma_status_code(self):
        for i in range(1, 7):
            url = reverse('tapahtumat', kwargs={'tapahtuma_pk': i})
            response = self.client.get(url)
            if i == 6:
                self.assertEquals(response.status_code, 404)
            else:
                self.assertEquals(response.status_code, 200)


    def test_tapahtuma_view_func(self):
        for i in range(1, 6):
            page = resolve('/tapahtumat/' + str(i) + '/')
            self.assertEquals(page.func, tapahtumat)

    def test_valokuva_status_code(self):
        url = reverse('valokuvat')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_kylalaiset_view_func(self):
        page = resolve('/kylalaiset/')
        self.assertEquals(page.func, kylaindex)

    def test_kylalaiset_status_code(self):
        """302 for redirecting to login page"""
        url = reverse('kylaindex')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
