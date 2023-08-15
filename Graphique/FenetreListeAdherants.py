# -*- coding: utf-8 -*-
from PyQt6.QtCore import (QCoreApplication,QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QGroupBox, QDialog, QTableWidget, QTableWidgetItem)
from Modele.Bibliotheque import Bibliotheque as Bib

class FenetreListeAdherants(QDialog):
    def setupUi(self, Fenetre_liste_adherants):
        if not Fenetre_liste_adherants.objectName():
            Fenetre_liste_adherants.setObjectName(u"Fenetre_liste_adherants")
        Fenetre_liste_adherants.setFixedSize(610, 352)
        self.tableListeAdherent = QTableWidget(Fenetre_liste_adherants)
        if (self.tableListeAdherent.columnCount() < 3):
            self.tableListeAdherent.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableListeAdherent.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableListeAdherent.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableListeAdherent.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableListeAdherent.setObjectName(u"tableListeAdherent")
        self.tableListeAdherent.setGeometry(QRect(50, 60, 511, 251))
        self.tableListeAdherent.setRowCount(0)
        self.tableListeAdherent.horizontalHeader().setCascadingSectionResizes(False)
        self.groupBox = QGroupBox(Fenetre_liste_adherants)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 551, 311))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.raise_()
        self.tableListeAdherent.raise_()
        self.tableListeAdherent.setColumnWidth(0,150)
        self.tableListeAdherent.setColumnWidth(1, 183)
        self.tableListeAdherent.setColumnWidth(2, 160)
        self.retranslateUi(Fenetre_liste_adherants)
        QMetaObject.connectSlotsByName(Fenetre_liste_adherants)
        self.affichier_liste_adherents(self.tableListeAdherent)

    def affichier_liste_adherents(self, tableListeAdherent):
        Bib().afficher_liste_adherent(tableListeAdherent)

    def retranslateUi(self, Fenetre_liste_adherants):
        Fenetre_liste_adherants.setWindowTitle(QCoreApplication.translate("Fenetre_liste_adherants", u"Affichier liste des adhérents", None))
        ___qtablewidgetitem = self.tableListeAdherent.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Fenetre_liste_adherants", u"Num\u00e9ro de l'adh\u00e9rent", None));
        ___qtablewidgetitem1 = self.tableListeAdherent.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Fenetre_liste_adherants", u"Nom de l'adh\u00e9rent", None));
        ___qtablewidgetitem2 = self.tableListeAdherent.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Fenetre_liste_adherants", u"Pr\u00e9nom de l'adh\u00e9rent", None));
        self.groupBox.setTitle(QCoreApplication.translate("Fenetre_liste_adherants", u"Liste des adh\u00e9rents", None))
