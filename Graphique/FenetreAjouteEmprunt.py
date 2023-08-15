# -*- coding: utf-8 -*-
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QGroupBox, QLabel, QPushButton, QDialog, QLineEdit, QDateEdit)
from Modele import Bibliotheque as Bib

class FenetreAjouterEmprunt(QDialog):
    def setupUi(self, Ajouter_Emprunt):
        if not Ajouter_Emprunt.objectName():
             Ajouter_Emprunt.setObjectName(u"Ajouter_Emprunt")
        Ajouter_Emprunt.setFixedSize(400, 320)

        self.numAdherentEmpruntLine = QLineEdit(Ajouter_Emprunt)
        self.numAdherentEmpruntLine.setObjectName(u"numAdherentEmpruntLine")
        self.numAdherentEmpruntLine.setGeometry(QRect(200, 95, 150, 21))

        self.numAdherentEmpruntLbl = QLabel(Ajouter_Emprunt)
        self.numAdherentEmpruntLbl.setObjectName(u"numAdherentEmpruntLbl")
        self.numAdherentEmpruntLbl.setGeometry(QRect(50, 90, 150, 25))
        font = QFont()
        font.setPointSize(12)
        self.numAdherentEmpruntLbl.setFont(font)

        self.ISBNEmpruntLine = QLineEdit(Ajouter_Emprunt)
        self.ISBNEmpruntLine.setObjectName(u"ISBNEmpruntLine")
        self.ISBNEmpruntLine.setGeometry(QRect(200, 130, 150, 21))

        self.ISBNEmpruntLbl = QLabel(Ajouter_Emprunt)
        self.ISBNEmpruntLbl.setObjectName(u"ISBNEmpruntLbl")
        self.ISBNEmpruntLbl.setGeometry(QRect(50, 130, 60, 25))
        self.ISBNEmpruntLbl.setFont(font)

        self.dateRetourEmpruntLine = QDateEdit(Ajouter_Emprunt)
        self.dateRetourEmpruntLine.setObjectName(u"ISBNEmpruntLine")
        self.dateRetourEmpruntLine.setGeometry(QRect(200, 165, 150, 21))

        self.dateRetourEmprunt_Lbl = QLabel(Ajouter_Emprunt)
        self.dateRetourEmprunt_Lbl.setObjectName(u"dateRetourEmprunt_Lbl")
        self.dateRetourEmprunt_Lbl.setGeometry(QRect(50, 165, 150, 25))
        self.dateRetourEmprunt_Lbl.setFont(font)

        self.msgEmpruntLbl = QLabel(Ajouter_Emprunt)
        self.msgEmpruntLbl.setObjectName(u"msgEmpruntLbl")
        self.msgEmpruntLbl.setGeometry(QRect(50, 215, 250, 25))
        self.msgEmpruntLbl.setFont(font)
        self.msgEmpruntLbl.setText("hello")

        self.ajouterEmpruntBtn = QPushButton(Ajouter_Emprunt)
        self.ajouterEmpruntBtn.setObjectName(u"ajouterEmpruntBtn")
        self.ajouterEmpruntBtn.setGeometry(QRect(275, 210, 75, 35))

        font1 = QFont()
        font1.setBold(True)
        self.ajouterEmpruntBtn.setFont(font1)
        self.groupBoxAjouterEmprunt = QGroupBox(Ajouter_Emprunt)
        self.groupBoxAjouterEmprunt.setObjectName(u"groupBoxAjouterEmprunt")
        self.groupBoxAjouterEmprunt.setGeometry(QRect(30, 30, 341, 250))

        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.groupBoxAjouterEmprunt.setFont(font2)
        self.groupBoxAjouterEmprunt.raise_()
        self.numAdherentEmpruntLine.raise_()
        self.ISBNEmpruntLine.raise_()
        self.numAdherentEmpruntLbl.raise_()
        self.ISBNEmpruntLbl.raise_()
        self.ajouterEmpruntBtn.raise_()
        self.dateRetourEmpruntLine.raise_()
        self.retranslateUi(Ajouter_Emprunt)
        QMetaObject.connectSlotsByName(Ajouter_Emprunt)

    def retranslateUi(self, Ajouter_Emprunt):
        Ajouter_Emprunt.setWindowTitle(QCoreApplication.translate("Ajouter_Emprunt", u"Ajouter Emprunt", None))
        self.dateRetourEmprunt_Lbl.setText(QCoreApplication.translate("Ajouter_Emprunt", u"Date de retour:", None))
        self.numAdherentEmpruntLbl.setText(QCoreApplication.translate("Ajouter_Emprunt", u"Numéro adhérent:", None))
        self.ISBNEmpruntLbl.setText(QCoreApplication.translate("Ajouter_Emprunt", u"ISBN:", None))
        self.ajouterEmpruntBtn.setText(QCoreApplication.translate("Ajouter_Emprunt", u"Ajouter", None))
        self.ajouterEmpruntBtn.clicked.connect(self.ajouter_donnees_Emprunt)
        self.groupBoxAjouterEmprunt.setTitle(
        QCoreApplication.translate("Ajouter_Emprunt", u"Ajouter un Emprunt", None))
        self.msgEmpruntLbl.setVisible(False)

    def ajouter_donnees_Emprunt(self):
        numAdherent= self.numAdherentEmpruntLine.text()
        ISBN = self.ISBNEmpruntLine.text()
        dateRetourEmprunt = self.dateRetourEmpruntLine.text()
        Bib.Bibliotheque().ajouter_emprunt(self, numAdherent, ISBN, dateRetourEmprunt)




