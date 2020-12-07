from .models import Animal, Equipement
liste_etats = ['affamé', 'fatigué', 'repus', 'endormi']


def nourrir(animal):
    mangeoire = Equipement.objects.get(id_equip="mangeoire")
    if animal.etat == "affamé" and mangeoire.verifie_disponibilite():
        animal.change_lieu(mangeoire)
        animal.change_etat("repus")


def divertir(animal):
    roue = Equipement.objects.get(id_equip="roue")
    if animal.etat == "repus" and roue.verifie_disponibilite():
        animal.change_lieu(roue)
        animal.change_etat("fatigué")


def coucher(animal):
    nid = Equipement.objects.get(id_equip="nid")
    if animal.etat == "fatigué" and nid.verifie_disponibilite():
        animal.change_lieu(nid)
        animal.change_etat("endormi")


def reveiller(animal):
    litiere = Equipement.objects.get(id_equip="litière")
    if animal.etat == "endormi" and litiere.verifie_disponibilite():
        animal.change_lieu(litiere)
        animal.change_etat("affamé")


def action_controleur(animal, action):
    print(animal, action)
    if action == "nourrir":
        nourrir(animal)
    elif action == "divertir":
        divertir(animal)
    elif action == "coucher":
        coucher(animal)
    elif action == "reveiller":
        reveiller(animal)
    else:
        print(f"L'action '{action}' n'existe pas")