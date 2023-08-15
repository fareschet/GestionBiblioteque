# -*- coding: utf-8 -*-
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QGroupBox, QLabel, QPushButton, QDialog, QLineEdit)
from Modele import Bibliotheque as Bib

class FenetreAjouterAdherent(QDialog):
    def setupUi(self, Ajouter_Adherent):
        if not Ajouter_Adherent.objectName():
             Ajouter_Adherent.setObjectName(u"Ajouter_Adherent")
        Ajouter_Adherent.resize(400, 300)

        self.nomAdherentLine = QLineEdit(Ajouter_Adherent)
        self.nomAdherentLine.setObjectName(u"nbrJoursLine")
        self.nomAdherentLine.setGeometry(QRect(130, 90, 201, 21))

        self.prenomAdherentLine = QLineEdit(Ajouter_Adherent)
        self.prenomAdherentLine.setObjectName(u"prenomAdherentLine")
        self.prenomAdherentLine.setGeometry(QRect(130, 130, 201, 21))

        self.nomAdherentLbl = QLabel(Ajouter_Adherent)
        self.nomAdherentLbl.setObjectName(u"nbrJoursLbl")
        self.nomAdherentLbl.setGeometry(QRect(50, 90, 49, 25))
        font = QFont()
        font.setPointSize(12)
        self.nomAdherentLbl.setFont(font)

        self.prenomAdherentLbl = QLabel(Ajouter_Adherent)
        self.prenomAdherentLbl.setObjectName(u"prenomAdherentLbl")
        self.prenomAdherentLbl.setGeometry(QRect(50, 130, 60, 25))
        self.prenomAdherentLbl.setFont(font)

        self.numAdherentLbl = QLabel(Ajouter_Adherent)
        self.numAdherentLbl.setObjectName(u"nbrJoursLbl")
        self.numAdherentLbl.setGeometry(QRect(50, 170, 60, 25))
        self.numAdherentLbl.setFont(font)

        self.msgAdherentLbl = QLabel(Ajouter_Adherent)
        self.msgAdherentLbl.setObjectName(u"msgAdherentLbl")
        self.msgAdherentLbl.setGeometry(QRect(50, 200, 250, 25))
        self.msgAdherentLbl.setFont(font)

        self.ajouterAdherentBtn = QPushButton(Ajouter_Adherent)
        self.ajouterAdherentBtn.setObjectName(u"ajouterAdherentBtn")
        self.ajouterAdherentBtn.setGeometry(QRect(260, 190, 75, 35))
        font1 = QFont()
        font1.setBold(True)
        self.ajouterAdherentBtn.setFont(font1)
        self.groupBoxAjouterAdhrent = QGroupBox(Ajouter_Adherent)
        self.groupBoxAjouterAdhrent.setObjectName(u"groupBoxAjouterAdhrent")
        self.groupBoxAjouterAdhrent.setGeometry(QRect(30, 50, 341, 191))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.groupBoxAjouterAdhrent.setFont(font2)
        self.groupBoxAjouterAdhrent.raise_()
        self.nomAdherentLine.raise_()
        self.prenomAdherentLine.raise_()
        self.nomAdherentLbl.raise_()
        self.prenomAdherentLbl.raise_()
        self.ajouterAdherentBtn.raise_()
        self.retranslateUi(Ajouter_Adherent)
        QMetaObject.connectSlotsByName(Ajouter_Adherent)

    def retranslateUi(self, Ajouter_Adherent):
        Ajouter_Adherent.setWindowTitle(QCoreApplication.translate("Ajouter_Adherent", u"Ajouter adhérent", None))
        self.numAdherentLbl.setText(QCoreApplication.translate("Ajouter_Adherent", u"Num\u00e9ro:", None))
        self.nomAdherentLbl.setText(QCoreApplication.translate("Ajouter_Adherent", u"Nom:", None))
        self.prenomAdherentLbl.setText(QCoreApplication.translate("Ajouter_Adherent", u"Pr\u00e9nom:", None))
        self.msgAdherentLbl.setText(QCoreApplication.translate("Ajouter_Adherent", u"<b>l'adhérent a bien été enregistré!</b>", None))
        self.ajouterAdherentBtn.setText(QCoreApplication.translate("Ajouter_Adherent", u"Ajouter", None))
        self.ajouterAdherentBtn.clicked.connect(self.ajouter_donnees_adherent)
        self.groupBoxAjouterAdhrent.setTitle(
        QCoreApplication.translate("Ajouter_Adherent", u"Ajouter un adh\u00e9rent", None))
        self.numAdherentLbl.setVisible(False)
        self.msgAdherentLbl.setVisible(False)

    def ajouter_donnees_adherent(self):
        self.nom = self.nomAdherentLine.text()
        self.prenom = self.prenomAdherentLine.text()
        if self.nom != "" and self.prenom != "":
            self.sender()
            bibliotheque = Bib.Bibliotheque()
            bibliotheque.ajouterAdherant(self, self.nom, self.prenom)

