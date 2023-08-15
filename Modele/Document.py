# -*- coding: utf-8 -*-

class Document:

    def __init__(self, ISBN, titre):
        self.__ISBN = ISBN
        self.__titre = titre

    def get_titre(self):
        return self.__titre

    def get_ISBN(self):
        return self.__ISBN

class Journal(Document):

    def __init__(self, document, date_parution):
        super().__init__(document.get_ISBN(), document.get_titre())
        self.__dateParution = date_parution
        self.__type = "Journal"

    def get_type(self):
        return self.__type

    def get_date(self):
        return self.__dateParution

class Volume(Document):

    def __init__(self, document, auteur):
        super().__init__(document.get_ISBN(), document.get_titre())
        self.__auteur = auteur

    def get_auteur(self):
        return self.__auteur

class Dictionnaire(Volume):

    def __init__(self, volume):
        super().__init__(volume, volume.get_auteur())
        self.__type = "Dictionnaire"

    def get_type(self):
        return self.__type

class BD(Volume):

    def __init__(self, volume, dessinateur):
        super().__init__(volume, volume.get_auteur())
        self.__dessinateur = dessinateur
        self.__type = "Bonde dessinee"

    def get_dessinateur(self):
        return self.__dessinateur

    def get_type(self):
        return self.__type

class Livre(Volume):

    def __init__(self, volume, disponible):
        super().__init__(volume, volume.get_auteur())
        self.__disponible = disponible
        self.__type = "Livre"

    def get_type(self):
        return self.__type

    def set_disponibilite(self, etat):
        self.__disponible = etat

    def get_empruntable(self):
        return self.__disponible


