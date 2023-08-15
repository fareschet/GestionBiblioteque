# -*- coding: utf-8 -*-
import os
import random
import string
import Modele.Adherent as Adh
import Modele.Document as Doc
from datetime import datetime
import Modele.Emprunte as Emp

def recuperer_date_aujourdhui():
    return datetime.today().strftime("%Y-%m-%d")

def afficher_menu_principale():
    pass

def generer_isbn(): #https://pynative.com/python-generate-random-string/
    prefix = ''.join(str(random.randint(0, 9)) for _ in range(3))
    identifier = random.randint(0, 9)
    suffix = ''.join(str(random.randint(0, 9)) for _ in range(4))
    return f"{prefix}-{identifier}-{suffix}"

def generer_numero_aderent(): #https://pynative.com/python-generate-random-string/
    lettres_majuscules = string.ascii_uppercase
    chiffres = string.digits
    prefixe = ''.join(random.choice(lettres_majuscules) for _ in range(3))
    suffixe = ''.join(random.choice(chiffres) for _ in range(3))
    numero_alphanumerique = prefixe + suffixe
    return numero_alphanumerique

def recuperer_liste_adherents():
    liste_adherents = []
    if os.path.exists(os.getcwd() +"/Modele/sauvegardeDonnees/adherents.txt"):
        with open(os.getcwd() +"/Modele/sauvegardeDonnees/adherents.txt", "r") as fichier:
            contenu = fichier.readline()
            while contenu != "":
                data = contenu.split(";")
                numero = data[0]
                nom = data[1]
                prenom = data[2].replace("\n", "")
                adherent = Adh.Adherent(numero, nom, prenom)
                liste_adherents.append(adherent)
                contenu = fichier.readline()
    return liste_adherents

def recuperer_liste_documents():
    liste_documents = {
        "Journal": [],
        "Dictionnaire": [],
        "Livre": [],
        "Bande dessinee": []
    }
    if os.path.exists(os.getcwd() +"/Modele/sauvegardeDonnees/documents.txt"):
        with open(os.getcwd() +"/Modele/sauvegardeDonnees/documents.txt", "r") as fichier:
            contenu = fichier.readline()
            while contenu != "":
                data = contenu.split(";")
                ISBN = data[0]
                type_document = data[1]
                titre = data[2]
                document = Doc.Document(ISBN, titre)
                if type_document == "Journal":
                    date_parution = data[3].replace("\n", "")
                    journal = Doc.Journal(document, date_parution)
                    liste_documents["Journal"].append(journal)
                elif type_document == "Dictionnaire":
                    auteur = data[3].replace("\n", "")
                    volume = Doc.Volume(document, auteur)
                    dictionnaire = Doc.Dictionnaire(volume)
                    liste_documents["Dictionnaire"].append(dictionnaire)
                elif type_document == "Livre":
                    auteur = data[3]
                    disponible = data[4].replace("\n", "")
                    volume = Doc.Volume(document, auteur)
                    livre = Doc.Livre(volume, disponible)
                    liste_documents["Livre"].append(livre)
                elif type_document == "Bonde dessinee":
                    auteur = data[3]
                    dessinateur = data[4].replace("\n", "")
                    volume = Doc.Volume(document, auteur)
                    bonde_dessinee = Doc.BD(volume, dessinateur)
                    liste_documents["Bande dessinee"].append(bonde_dessinee)
                contenu = fichier.readline()
    return liste_documents

def recuperer_liste_emprunt():
    liste_emprunt = []
    if os.path.exists(os.getcwd() +"/Modele/sauvegardeDonnees/emprunts.txt"):
        with open(os.getcwd() +"/Modele/sauvegardeDonnees/emprunts.txt", "r") as fichier:
            contenu = fichier.readline()
            while contenu != "":
                data = contenu.split(";")
                numero_adherant = data[0]
                ISBN = data[1]
                date_emprunt = data[2]
                date_retour = data[3].replace("\n", "")
                emprunt = Emp.Emprunte(numero_adherant, ISBN, date_emprunt, date_retour)
                liste_emprunt.append(emprunt)
                contenu = fichier.readline()
    return liste_emprunt