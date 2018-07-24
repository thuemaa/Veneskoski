from django.test import TestCase
from django.urls import reverse, resolve
from datetime import datetime
from soikka.views import home, ajankohtaista
from soikka.models import Ajankohtaista, Valokuva

class AjankohtaistaModelTests(TestCase):

    def test_ajankohtaista_model_creation(self):
        self.assertEquals(1, 1)
        # TO DO: IMPLEMENT TEST

    def test_ajankohtaista_model_change(self):
        pass

    def test_ajankohtaista_model_delete(self):
        pass