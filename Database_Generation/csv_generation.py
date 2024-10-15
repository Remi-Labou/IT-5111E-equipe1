import csv
import random
import string
import datetime

# Types de places
types_places = ["moto", "voiture", "camion","handicape"]

# Générer une plaque d'immatriculation aléatoire
def generer_plaque():
    lettres = ''.join(random.choices(string.ascii_uppercase, k=2))
    chiffres = ''.join(random.choices(string.digits, k=4))
    return f"{lettres}-{chiffres}"

# Générer les informations d'un véhicule garé
def generer_donnees_vehicule(place):

    if(place < 20):
        type_place = types_places[3]
    elif(place < 120):
        type_place = types_places[1]
    elif(place < 160):
        type_place = types_places[2]
    else :
        type_place = types_places[0]

    occupe=random.choice(["oui", "non"])
    if(occupe == "oui"):
        type_vehicule= types_places[random.randint(0, 3)]
        plaque = generer_plaque()
        temps_paye = datetime.timedelta(random.randint(0, 1),random.randint(0, 23),random.randint(0, 59),random.randint(0, 59))
        prix= random.choice([1.4,3.8,7.3])
        horaire_debut=datetime.datetime(2024,10,1,random.randint(0, 23),random.randint(0, 59),random.randint(0, 59),0)
        horaire_fin=horaire_debut + temps_paye
    else:
        type_vehicule= None
        temps_paye =  None
        prix= None
        horaire_debut= None
        horaire_fin= None
        plaque = None


    return {
        "Numero de place":place,
        "Type de place":type_place,
        "Occupation":occupe,
        "Plaque d'immatriculation":plaque,
        "Categorie de véhicule": type_vehicule,
        "Temps paye": temps_paye,
        "Prix paye":prix,
        "Horaire d'arrive":horaire_debut,
        "Horaire de depart prevu":horaire_fin,
    }

# Générer un CSV avec des véhicules aléatoires
def generer_csv(nombre_vehicules, fichier_csv):
    # Nom des colonnes
    colonnes = [
        "Numero de place",
        "Type de place",
        "Occupation",
        "Plaque d'immatriculation",
        "Categorie de véhicule",
        "Temps paye",
        "Prix paye",
        "Horaire d'arrive",
        "Horaire de depart prevu"
    ]

    # Générer des données et les écrire dans le fichier CSV
    with open(fichier_csv, mode='w', newline='', encoding='utf-8') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()  # Écrire l'en-tête du CSV

        for _ in range(nombre_vehicules):
            donnees_vehicule = generer_donnees_vehicule(_)
            writer.writerow(donnees_vehicule)

# Exemple d'utilisation pour générer un fichier CSV avec 100 véhicules
generer_csv(200, "vehicules_gare.csv")