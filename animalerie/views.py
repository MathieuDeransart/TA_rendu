from django.shortcuts import render, get_object_or_404
from .models import Animal, Equipement
from .forms import ChoixControleur
from .controler import action_controleur

def animal_list(request):
    animaux = Animal.objects.all()
    equipements = Equipement.objects.all()
    if request.GET:
        id_animal = request.GET['animal']
        action = request.GET['action']
        animal = Animal.objects.get(id_animal=id_animal)
        action_controleur(animal, action)
    return render(request, "animalerie/animal_list.html", {"animaux": animaux, "equipements": equipements, "choix_controleur": ChoixControleur()})


def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    return render(request, "animalerie/animal_detail.html", {"animal": animal})

# Create your views here.
