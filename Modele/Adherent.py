# -*- coding: utf-8 -*-

class Adherent:

    def __init__(self, numero, nom, prenom):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom

    def get_numero_adherent(self):
        return self.__numero

    def get_nom_adherent(self):
        return self.__nom

    def get_prenom_adherent(self):
        return self.__prenom

