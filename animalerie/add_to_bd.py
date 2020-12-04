import json
from animalerie.models import Animal, Equipement

with open('équipement copie.json', "r") as f:
    equipement_dict = json.load(f)
    for id_equip in equipement_dict:
        disponibilite = equipement_dict[id_equip]["DISPONIBILITÉ"]
        Equipement.objects.create(id_equip=id_equip, disponibilite=disponibilite)

animal_data = 'animal copie.json'
with open(animal_data, "r") as f:
    animal_dict = json.load(f)
    for id_animal in animal_dict:
        etat = animal_dict[id_animal]["ETAT"]
        type = animal_dict[id_animal]["TYPE"]
        race = animal_dict[id_animal]["RACE"]
        lieu = Equipement.objects.get(id_equip=animal_dict[id_animal]["LIEU"])
        Animal.objects.create(id_animal=id_animal, etat=etat, type=type, race=race, lieu=lieu)
