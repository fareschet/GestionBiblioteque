# -*- coding: utf-8 -*-
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QDialog, QGroupBox, QLabel, QLineEdit, QListWidget, QListWidgetItem, QPushButton, QSpinBox)
from Modele import Bibliotheque as Bib
import datetime

class FenetreAjouterDocument(QDialog):
    def setupUi(self, Ajouter_document):
        if not Ajouter_document.objectName():
            Ajouter_document.setObjectName(u"Ajouter_document")
        Ajouter_document.setFixedSize(640, 395)
        self.AjouterDocument = QGroupBox(Ajouter_document)
        self.AjouterDocument.setObjectName(u"AjouterDocument")
        self.AjouterDocument.setGeometry(QRect(70, 60, 501, 271))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)

        self.AjouterDocument.setFont(font)
        self.AjouterDocumentTitrelbl = QLabel(self.AjouterDocument)
        self.AjouterDocumentTitrelbl.setObjectName(u"AjouterDocumentTitrelbl")
        self.AjouterDocumentTitrelbl.setGeometry(QRect(160, 80, 111, 16))

        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.AjouterDocumentTitrelbl.setFont(font1)

        self.AjouterDocumentDeuxiemelbl = QLabel(self.AjouterDocument)
        self.AjouterDocumentDeuxiemelbl.setObjectName(u"AjouterDocumentDeuxiemelbl")
        self.AjouterDocumentDeuxiemelbl.setGeometry(QRect(160, 120, 101, 16))
        self.AjouterDocumentDeuxiemelbl.setFont(font1)

        self.AjouterDocumentTroisiemelbl = QLabel(self.AjouterDocument)
        self.AjouterDocumentTroisiemelbl.setObjectName(u"AjouterDocumentTroisiemelbl")
        self.AjouterDocumentTroisiemelbl.setGeometry(QRect(160, 160, 111, 16))
        self.AjouterDocumentTroisiemelbl.setFont(font1)

        self.Ajouter_document_pushButton = QPushButton(self.AjouterDocument)
        self.Ajouter_document_pushButton.setObjectName(u"Ajouter_document_pushButton")
        self.Ajouter_document_pushButton.setGeometry(QRect(350, 210, 101, 31))
        self.Ajouter_document_pushButton.setFont(font1)
        self.Ajouter_document_pushButton.clicked.connect(self.ajouter_document)

        self.AjouterDocumentTitrelineEdit = QLineEdit(self.AjouterDocument)
        self.AjouterDocumentTitrelineEdit.setObjectName(u"AjouterDocumentTitrelineEdit")
        self.AjouterDocumentTitrelineEdit.setGeometry(QRect(270, 80, 181, 21))

        self.AjouterDocumentDeuxiemelineEdit = QLineEdit(self.AjouterDocument)
        self.AjouterDocumentDeuxiemelineEdit.setObjectName(u"AjouterDocumentDeuxiemelineEdit")
        self.AjouterDocumentDeuxiemelineEdit.setGeometry(QRect(270, 120, 181, 21))

        self.AjouterDocumentDeuxiemeSpin = QSpinBox(self.AjouterDocument)
        self.AjouterDocumentDeuxiemeSpin.setMinimum(1900)
        self.AjouterDocumentDeuxiemeSpin.setMaximum(datetime.datetime.now().year)
        self.AjouterDocumentDeuxiemeSpin.setObjectName(u"AjouterDocumentDeuxiemelineSpin")
        self.AjouterDocumentDeuxiemeSpin.setGeometry(QRect(270, 120, 181, 21))
        self.AjouterDocumentDeuxiemeSpin.setVisible(False)

        self.AjouterDocumentTroisiemelineEdit = QLineEdit(self.AjouterDocument)
        self.AjouterDocumentTroisiemelineEdit.setObjectName(u"AjouterDocumentTroisiemelineEdit")
        self.AjouterDocumentTroisiemelineEdit.setGeometry(QRect(270, 160, 181, 21))

        self.AjouterDocumentlist = QListWidget(self.AjouterDocument)
        QListWidgetItem(self.AjouterDocumentlist)
        QListWidgetItem(self.AjouterDocumentlist)
        QListWidgetItem(self.AjouterDocumentlist)
        QListWidgetItem(self.AjouterDocumentlist)
        QListWidgetItem(self.AjouterDocumentlist)
        self.AjouterDocumentlist.itemClicked.connect(self.afficher_option_ajout_document)

        self.AjouterDocumentlist.setObjectName(u"AjouterDocumentlist")
        self.AjouterDocumentlist.setGeometry(QRect(270, 30, 181, 31))
        self.AjouterDocumentlist.setFont(font1)

        self.label_6 = QLabel(self.AjouterDocument)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(25, 30, 230, 31))
        self.label_6.setFont(font1)

        self.ajouter_document_5_lbl = QLabel(self.AjouterDocument)
        self.ajouter_document_5_lbl.setObjectName(u"ajouter_document_5_lbl")
        self.ajouter_document_5_lbl.setGeometry(QRect(50, 200, 250, 25))
        self.ajouter_document_5_lbl.setFont(font1)

        self.ajouter_document_3_lbl = QLabel(self.AjouterDocument)
        self.ajouter_document_3_lbl.setObjectName(u"ajouter_document_3_lbl")
        self.ajouter_document_3_lbl.setGeometry(QRect(50, 160, 250, 25))
        self.ajouter_document_3_lbl.setFont(font1)

        self.ajouter_document_4_lbl = QLabel(self.AjouterDocument)
        self.ajouter_document_4_lbl.setObjectName(u"ajouter_document_4_lbl")
        self.ajouter_document_4_lbl.setGeometry(QRect(50, 230, 280, 25))
        self.ajouter_document_4_lbl.setFont(font1)

        self.ajouter_document_2_lbl = QLabel(self.AjouterDocument)
        self.ajouter_document_2_lbl.setObjectName(u"ajouter_document_2_lbl")
        self.ajouter_document_2_lbl.setGeometry(QRect(50, 120, 250, 25))
        self.ajouter_document_2_lbl.setFont(font1)

        self.ajouter_document_titre_lbl = QLabel(self.AjouterDocument)
        self.ajouter_document_titre_lbl.setObjectName(u"ajouter_document_titre_lbl")
        self.ajouter_document_titre_lbl.setGeometry(QRect(50, 80, 250, 25))
        self.ajouter_document_titre_lbl.setFont(font1)

        self.retranslateUi(Ajouter_document)
        QMetaObject.connectSlotsByName(Ajouter_document)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Ajouter_document", u"Ajouter un document", None))
        self.AjouterDocument.setTitle(QCoreApplication.translate("Ajouter_document", u"Ajouter un document", None))
        self.AjouterDocumentTitrelbl.setText(QCoreApplication.translate("Ajouter_document", u"TextLabel", None))
        self.AjouterDocumentDeuxiemelbl.setText(QCoreApplication.translate("Ajouter_document", u"TextLabel", None))
        self.AjouterDocumentTroisiemelbl.setText(QCoreApplication.translate("Ajouter_document", u"TextLabel", None))
        self.Ajouter_document_pushButton.setText(QCoreApplication.translate("Ajouter_document", u"Ajouter", None))

        __sortingEnabled = self.AjouterDocumentlist.isSortingEnabled()
        self.AjouterDocumentlist.setSortingEnabled(False)
        ___qlistwidgetitem = self.AjouterDocumentlist.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Ajouter_document", u"Choisir...", None));
        ___qlistwidgetitem1 = self.AjouterDocumentlist.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Ajouter_document", u"Journal", None));
        ___qlistwidgetitem2 = self.AjouterDocumentlist.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Ajouter_document", u"Livre", None));
        ___qlistwidgetitem3 = self.AjouterDocumentlist.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Ajouter_document", u"Dictionnaire", None));
        ___qlistwidgetitem4 = self.AjouterDocumentlist.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Ajouter_document", u"Bande dessinee", None));
        self.AjouterDocumentlist.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(QCoreApplication.translate("Ajouter_document", u"Cliquer sur le type du document:", None))
        self.ajouter_document_5_lbl.setText(QCoreApplication.translate("Ajouter_document", u"TextLabel_5", None))
        self.ajouter_document_3_lbl.setText(QCoreApplication.translate("Ajouter_document", u"TextLabel_3", None))
        self.ajouter_document_2_lbl.setText(QCoreApplication.translate("Ajouter_document", u"TextLabel_2", None))
        self.ajouter_document_4_lbl.setText(QCoreApplication.translate("Ajouter_document", u"TextLabel_4", None))
        self.ajouter_document_titre_lbl.setText(
            QCoreApplication.translate("Ajouter_document", u"TextLabel_titre", None))
        self.cacher_option_ajout_document_gauche()
        self.cacher_option_ajout_document_droit()

    def cacher_option_ajout_document_gauche(self):
        self.ajouter_document_titre_lbl.setVisible(False)
        self.ajouter_document_2_lbl.setVisible(False)
        self.ajouter_document_3_lbl.setVisible(False)
        self.ajouter_document_5_lbl.setVisible(False)
        self.ajouter_document_4_lbl.setVisible(False)

    def cacher_option_ajout_document_droit(self):
        self.AjouterDocumentTitrelbl.setVisible(False)
        self.AjouterDocumentDeuxiemelbl.setVisible(False)
        self.AjouterDocumentTroisiemelbl.setVisible(False)
        self.AjouterDocumentTitrelineEdit.setVisible(False)
        self.AjouterDocumentDeuxiemelineEdit.setVisible(False)
        self.AjouterDocumentDeuxiemeSpin.setVisible(False)
        self.AjouterDocumentTroisiemelineEdit.setVisible(False)
        self.Ajouter_document_pushButton.setVisible(False)

    def afficher_option_ajout_document(self):
        choix = self.AjouterDocumentlist.currentItem().text()
        self.AjouterDocumentDeuxiemeSpin.setVisible(False)
        if choix == "Journal":
            self.cacher_option_ajout_document_gauche()
            self.AjouterDocumentDeuxiemeSpin.setVisible(True)
            self.AjouterDocumentDeuxiemelineEdit.setVisible(False)
            self.AjouterDocumentTitrelbl.setVisible(True)
            self.AjouterDocumentTitrelbl.setText("Titre:")
            self.AjouterDocumentDeuxiemelbl.setVisible(True)
            self.AjouterDocumentDeuxiemelbl.setText("Année:")
            self.AjouterDocumentTitrelineEdit.setVisible(True)
            self.Ajouter_document_pushButton.setVisible(True)
            self.Ajouter_document_pushButton.setGeometry(QRect(350, 160, 101, 31))
            self.AjouterDocumentTroisiemelbl.setVisible(False)
            self.AjouterDocumentTroisiemelineEdit.setVisible(False)

        elif choix == "Livre":
            self.cacher_option_ajout_document_gauche()
            self.AjouterDocumentTitrelbl.setVisible(True)
            self.AjouterDocumentTitrelbl.setText("Titre:")
            self.AjouterDocumentDeuxiemelbl.setVisible(True)
            self.AjouterDocumentDeuxiemelbl.setText("Auteur:")
            self.AjouterDocumentTitrelineEdit.setVisible(True)
            self.AjouterDocumentDeuxiemelineEdit.setVisible(True)
            self.Ajouter_document_pushButton.setVisible(True)
            self.Ajouter_document_pushButton.setGeometry(QRect(350, 160, 101, 31))
            self.AjouterDocumentTroisiemelbl.setVisible(False)
            self.AjouterDocumentTroisiemelineEdit.setVisible(False)

        elif choix == "Dictionnaire":
            self.cacher_option_ajout_document_gauche()
            self.AjouterDocumentTitrelbl.setVisible(True)
            self.AjouterDocumentTitrelbl.setText("Titre:")
            self.AjouterDocumentDeuxiemelbl.setVisible(True)
            self.AjouterDocumentDeuxiemelbl.setText("Auteur:")
            self.AjouterDocumentTitrelineEdit.setVisible(True)
            self.AjouterDocumentDeuxiemelineEdit.setVisible(True)
            self.Ajouter_document_pushButton.setVisible(True)
            self.Ajouter_document_pushButton.setGeometry(QRect(350, 160, 101, 31))
            self.AjouterDocumentTroisiemelbl.setVisible(False)
            self.AjouterDocumentTroisiemelineEdit.setVisible(False)

        elif choix == "Bande dessinee":
            self.cacher_option_ajout_document_gauche()
            self.AjouterDocumentTitrelbl.setVisible(True)
            self.AjouterDocumentTitrelbl.setText("Titre:")
            self.AjouterDocumentDeuxiemelbl.setVisible(True)
            self.AjouterDocumentDeuxiemelbl.setText("Auteur:")
            self.AjouterDocumentTroisiemelbl.setVisible(True)
            self.AjouterDocumentTroisiemelbl.setText("Dessinateur:")
            self.AjouterDocumentTitrelineEdit.setVisible(True)
            self.AjouterDocumentDeuxiemelineEdit.setVisible(True)
            self.AjouterDocumentTroisiemelineEdit.setVisible(True)
            self.Ajouter_document_pushButton.setVisible(True)
            self.Ajouter_document_pushButton.setGeometry(QRect(350, 200, 101, 31))

        elif choix == "Choisir...":
            self.cacher_option_ajout_document_droit()
            self.cacher_option_ajout_document_gauche()
          
        return choix

    def ajouter_document(self):
        choix = self.afficher_option_ajout_document()
        if choix == "Bande dessinee":
            if self.AjouterDocumentTitrelineEdit.text() != "" and self.AjouterDocumentDeuxiemelineEdit.text() != "" and self.AjouterDocumentTroisiemelineEdit.text() != "":
                contenu1 = self.AjouterDocumentTitrelineEdit.text()
                contenu2 = self.AjouterDocumentDeuxiemelineEdit.text()
                contenu3 = self.AjouterDocumentTroisiemelineEdit.text()
                bib = Bib.Bibliotheque()
                bib.ajouter_document(self, contenu1, contenu2, contenu3, choix)

        else:
            if choix == "Journal":
                if self.AjouterDocumentTitrelineEdit.text() != "" and self.AjouterDocumentDeuxiemeSpin.text() != "":
                    contenu1 = self.AjouterDocumentTitrelineEdit.text()
                    contenu2 = self.AjouterDocumentDeuxiemeSpin.text()
                    bib = Bib.Bibliotheque()
                    contenu3 = ""
                    bib.ajouter_document(self, contenu1, contenu2, contenu3, choix)
            else:
                if choix in ["Livre", "Dictionnaire"]:
                    if self.AjouterDocumentTitrelineEdit.text() != "" and self.AjouterDocumentDeuxiemelineEdit.text() != "":
                        contenu2 = self.AjouterDocumentDeuxiemelineEdit.text()
                        contenu1 = self.AjouterDocumentTitrelineEdit.text()
                        bib = Bib.Bibliotheque()
                        contenu3 = ""
                        bib.ajouter_document(self, contenu1, contenu2, contenu3, choix)

    def reinitialiser_data(self):
        self.AjouterDocumentTitrelineEdit.clear()
        self.AjouterDocumentDeuxiemelineEdit.clear()
        self.AjouterDocumentTroisiemelineEdit.clear()
        self.ajouter_document_titre_lbl.setVisible(True)
        self.ajouter_document_2_lbl.setVisible(True)
        self.ajouter_document_3_lbl.setVisible(True)
        self.ajouter_document_5_lbl.setVisible(True)
