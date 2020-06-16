from django.test import TestCase
from mitglieder.models import *
from aemter.models import *

class TestModels(TestCase):

    def setUp(self):
        self.referat1 = Organisationseinheit.objects.create(
            bezeichnung = "myreferat"
        )

        self.unterbereich1 = Unterbereich.objects.create(
            bezeichnung = "myunterbereich",
            organisationseinheit = self.referat1
        )

        self.amt1 = Funktion.objects.create(
            bezeichnung = "myamt1",
            workload = 4,
            max_members = 5,
            organisationseinheit = self.referat1,
            unterbereich = self.unterbereich1
        )

        self.amt2 = Funktion.objects.create(
            bezeichnung = "myamt2",
            workload = 4,
            max_members = 5,
            organisationseinheit = self.referat1,
            unterbereich = None
        )

    def test_Referat_toString(self):
        self.assertEqual(
            self.referat1.__str__(),
            "myreferat")

    def test_Unterbereich_toString(self):
        self.assertEqual(
            self.unterbereich1.__str__(),
            "myunterbereich (Organisationseinheit myreferat)")

    def test_Amt1_toString(self):
        self.assertEqual(
            self.amt1.__str__(),
            "myamt1 myunterbereich (Organisationseinheit myreferat)")

    def test_Amt2_toString(self):
        self.assertEqual(
            self.amt2.__str__(),
            "myamt2 myreferat")
