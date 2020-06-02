from django.test import SimpleTestCase
from django.urls import reverse, resolve

from mitglieder.views import *

class TestUrls(SimpleTestCase):
    def test_main_screen_url_resolves(self):
        url = reverse('mitglieder:homepage')
        self.assertEqual(resolve(url).func, main_screen)

    def test_mitgliedErstellenView_url_resolves(self):
        url = reverse('mitglieder:erstellenView')
        self.assertEqual(resolve(url).func, mitgliedErstellenView)

    """
        Bearbeiten
    """
    def test_mitgliedBearbeitenView_url_resolves(self):
        url = reverse('mitglieder:bearbeitenView', args="1")
        self.assertEqual(resolve(url).func, mitgliedBearbeitenView)

    def test_mitglied_laden_url_resolves(self):
        url = reverse('mitglieder:mitglied_laden')
        self.assertEqual(resolve(url).func, mitglied_laden)

    def test_speichern_url_resolves(self):
        url = reverse('mitglieder:speichern', args="1")
        self.assertEqual(resolve(url).func, speichern)

    def test_mitglieder_loeschen_url_resolves(self):
        url = reverse('mitglieder:mitglieder_loeschen')
        self.assertEqual(resolve(url).func, mitglieder_loeschen)

    """
        Mitglieder Erstellen View
    """
    def test_erstellen_url_resolves(self):
        url = reverse('mitglieder:erstellen')
        self.assertEqual(resolve(url).func, erstellen)

    def test_bereiche_laden_url_resolves(self):
        url = reverse('mitglieder:bereiche_laden')
        self.assertEqual(resolve(url).func, bereiche_laden)

    def test_aemter_laden_url_resolves(self):
        url = reverse('mitglieder:aemter_laden')
        self.assertEqual(resolve(url).func, aemter_laden)

    def test_aemter_html_laden_url_resolves(self):
        url = reverse('mitglieder:aemter_html_laden')
        self.assertEqual(resolve(url).func, aemter_html_laden)

    def test_email_html_laden_url_resolves(self):
        url = reverse('mitglieder:email_html_laden')
        self.assertEqual(resolve(url).func, email_html_laden)

    def test_amt_loeschen_url_resolves(self):
        url = reverse('mitglieder:amt_loeschen')
        self.assertEqual(resolve(url).func, amt_loeschen)

    def test_email_loeschen_url_resolves(self):
        url = reverse('mitglieder:email_loeschen')
        self.assertEqual(resolve(url).func, email_loeschen)

    """
        Suchen
    """
    def test_suchen_url_resolves(self):
        url = reverse('mitglieder:suchen')
        self.assertEqual(resolve(url).func, suchen)

    """
    Template

    def test_xxxx_url_resolves(self):
        url = reverse('mitglieder:')
        self.assertEqual(resolve(url).func, )
    """
