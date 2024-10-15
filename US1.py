import csv

def lire_donnees_parking(fichier_csv):
    vehicules_gares = []
    
    with open(fichier_csv, mode='r', newline='', encoding='utf-8') as fichier:
        reader = csv.DictReader(fichier)
        
        for row in reader:
            vehicules_gares.append(row)
    
    return vehicules_gares

def identifier_vehicules_mal_gares(vehicules):
    vehicules_mal_gares = []
    
    for vehicule in vehicules:
        categorie = vehicule["Catégorie de véhicule"]
        type_place = vehicule["Type de place"]
    
        if not type_place.endswith(categorie):
            vehicules_mal_gares.append(vehicule)
    
    return vehicules_mal_gares

def afficher_zones_problematique(vehicules_mal_gares):
    if vehicules_mal_gares:
        print("Zones à vérifier pour des véhicules mal garés :\n")
        for vehicule in vehicules_mal_gares:
            print(f"  - Plaque : {vehicule['Plaque d\'immatriculation']}, Catégorie : {vehicule['Catégorie de véhicule']}, Place : {vehicule['Numéro de place']} (Type: {vehicule['Type de place']})")
    else:
        print("Aucune zone problématique détectée.")


def ronde_police(fichier_csv):
    print("Démarrage de la ronde de police...\n")
    
    vehicules_gares = lire_donnees_parking(fichier_csv)
    vehicules_mal_gares = identifier_vehicules_mal_gares(vehicules_gares)
    afficher_zones_problematique(vehicules_mal_gares)


fichier_csv = "vehicules_gare.csv"       
ronde_police(fichier_csv)
