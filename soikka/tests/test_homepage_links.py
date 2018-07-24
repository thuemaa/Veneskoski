from django.test import TestCase
from django.urls import reverse, resolve
from datetime import datetime
from soikka.views import home, ajankohtaista
from soikka.models import Ajankohtaista
'''
TEST:

    LINKS: home, kylalaisille,
    MODELS: Ajankohtaista, Kuva, Tapahtuma, Kesateatteri, Vuokrattavana
'''

class HomePageLinksTests(TestCase):
    
    # create necessary models for link testing
    def setUp(self):
        # create 5 ajankohtaista objects
        for i in range(0, 5):
            Ajankohtaista.objects.create(otsikko='Otsikko '+str(i), teksti='Teksti ' + str(1), pvm=datetime.now())

    def test_homepage_status_code(self):
        """Test status code for homepage"""
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_homepage_view_func(self):
        page = resolve('/')
        self.assertEquals(page.func, home)
    
    def test_anakohtaista_status_codeU(self):
        url = reverse('ajankohtaista', kwargs={'ak_pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_ajankohtaista_view_func(self):
        # ak = Ajankohtaista.objects.all().order_by('-pvm')[:5]
        # ak_pk = ak[0].pk
        page = resolve('/ajankohtaista/1')
        self.assertEquals(page.func, ajankohtaista)
