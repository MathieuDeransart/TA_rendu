from django.conf import settings
from django.db import models


class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.id_equip

    def verifie_disponibilite(self):
        return self.disponibilite == 'libre'

    def cherche_occupant(self):
        return Animal.objects.filter(lieu=self)

    def libere(self):
        self.disponibilite = 'libre'

    def occupe(self):
        self.disponibilite = 'occupe'


liste_etats = ['affamé', 'fatigué', 'repus', 'endormi']

class Animal(models.Model):
    id_animal = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_animal

    def lit_etat(self):
        return self.etat

    def lit_lieu(self):
        return self.lieu

    def change_etat(self, etat):
        print("change etat")
        if etat in liste_etats:
            print("in liste etats")
            self.etat = etat

    def change_lieu(self, lieu):
        print("change lieu")
        if lieu.verifie_disponibilite():
            print("in lieu dispo")
            self.lieu.libere()
            self.lieu = lieu
            if lieu.id_equip != "litière":
                lieu.occupe()

# Create your models here.
