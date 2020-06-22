from django.db import models

from mitglieder.models import MitgliedAmt

class Checkliste(models.Model):
    mitgliedAmt = models.ForeignKey(MitgliedAmt, on_delete=models.CASCADE, null=False)

class Aufgabe(models.Model):
    bezeichnung = models.CharField(max_length=50, null=False)

class ChecklisteAufgabe(models.Model):
    checkliste = models.ForeignKey(Checkliste, on_delete=models.CASCADE, null=False)
    aufgabe = models.ForeignKey(Aufgabe, on_delete=models.CASCADE, null=False)
    abgehakt = models.BooleanField(default=False, null=False)
