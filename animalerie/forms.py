from django import forms
from animalerie.models import Animal, Equipement

"""
https://www.geeksforgeeks.org/choicefield-django-forms/
"""

choix_animal = list()
for animal in Animal.objects.all():
    choix_animal.append((animal.id_animal, animal.id_animal))

choix_action = [
    ("nourrir", "Nourrir"),
    ("divertir", "Divertir"),
    ("coucher", "Coucher"),
    ("reveiller", "réveiller"),
]


class ChoixControleur(forms.Form):
    animal = forms.ChoiceField(choices=choix_animal)
    action = forms.ChoiceField(choices=choix_action)
