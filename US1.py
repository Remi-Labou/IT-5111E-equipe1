import csv
from datetime import datetime


# Fonction pour lire les données du fichier CSV
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

def identifier_vehicules_depassement_temps(vehicules):
    vehicules_en_depassement = []
    maintenant = datetime.now()

    for vehicule in vehicules:
        if vehicule["Occupation"] == "oui" and vehicule["Horaire de depart prevu"]:
            horaire_depart_prev = datetime.fromisoformat(vehicule["Horaire de depart prevu"])
            if maintenant > horaire_depart_prev:
                vehicules_en_depassement.append(vehicule)

    return vehicules_en_depassement

def afficher_zones_problematique(vehicules, message):
    if vehicules:
        print(message + ":\n")
        for vehicule in vehicules:
            print(f"  - Plaque : {vehicule['Plaque d'immatriculation']}, "
                  f"Catégorie : {vehicule['Catégorie de véhicule']}, "
                  f"Place : {vehicule['Numéro de place']} "
                  f"(Type: {vehicule['Type de place']})\n"
                  f"Temps de stationnement : {vehicule['Temps de stationnement (h)']}h")
    else:
        print(f"Aucune {message.lower()} détectée.")



def ronde_police(fichier_csv, temps_max_autorise=6):
    print("Démarrage de la ronde de police...\n")
    
    vehicules_gares = lire_donnees_parking(fichier_csv)
    vehicules_mal_gares = identifier_vehicules_mal_gares(vehicules_gares)
    vehicules_depassement_temps = identifier_vehicules_depassement_temps(vehicules_gares, temps_max_autorise)
    afficher_zones_problematique(vehicules_mal_gares, "Zones à vérifier pour des véhicules mal garés")
    afficher_zones_problematique(vehicules_depassement_temps, "Zones à vérifier pour dépassement de temps de stationnement")


# Exécution de la ronde de police en lisant l'état du parking
fichier_csv = "csv_generation.csv"  
ronde_police(fichier_csv, temps_max_autorise=6) 
