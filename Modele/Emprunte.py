# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

class Emprunte:

    def __init__(self, numero_etudiant, ISBN_livre, dateEmprunt, dateRetour):
        self.__numero_etudiant = numero_etudiant
        self.__ISBN_livre = ISBN_livre
        self.__dateEmprunt = datetime.strptime(dateEmprunt, '%Y-%m-%d')
        self.__dateRetour = datetime.strptime(dateRetour, '%Y-%m-%d')

    def get_dateEmprunt(self):
        return self.__dateEmprunt.strftime('%Y-%m-%d')

    def get_dateRetour(self):
        return self.__dateRetour.strftime('%Y-%m-%d')

    def prolongerDateRetour(self, jours_prolongation):
        # Prolonger la date de retour en ajoutant le nombre de jours de prolongation
        nouvelle_date_retour = self.__dateRetour + timedelta(days=int(jours_prolongation))
        # Mettre à jour la date de retour empruntée
        self.__dateRetour = nouvelle_date_retour

    def get_numero_adherant(self):
        return self.__numero_etudiant

    def get_ISBN_livre(self):
        return self.__ISBN_livre



