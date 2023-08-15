# -*- coding: utf-8 -*-
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QGroupBox, QDialog, QTableWidget, QTableWidgetItem)
from Modele.Bibliotheque import Bibliotheque as Bib

class FenetreListeEmprunt(QDialog):
    def setupUi(self, Fenetre_liste_Emprunt):
        if not Fenetre_liste_Emprunt.objectName():
            Fenetre_liste_Emprunt.setObjectName(u"Fenetre_liste_Emprunt")
        Fenetre_liste_Emprunt.setFixedSize(900, 352)
        self.tableListeEmprunt = QTableWidget(Fenetre_liste_Emprunt)
        if (self.tableListeEmprunt.columnCount() < 7):
            self.tableListeEmprunt.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableListeEmprunt.setHorizontalHeaderItem(0, __qtablewidgetitem)

        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableListeEmprunt.setHorizontalHeaderItem(1, __qtablewidgetitem1)

        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableListeEmprunt.setHorizontalHeaderItem(2, __qtablewidgetitem2)

        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableListeEmprunt.setHorizontalHeaderItem(3, __qtablewidgetitem3)

        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableListeEmprunt.setHorizontalHeaderItem(4, __qtablewidgetitem4)

        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableListeEmprunt.setHorizontalHeaderItem(5, __qtablewidgetitem5)

        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableListeEmprunt.setHorizontalHeaderItem(6, __qtablewidgetitem6)

        self.tableListeEmprunt.setObjectName(u"tableListeEmprunt")
        self.tableListeEmprunt.setGeometry(QRect(50, 60, 800, 251))
        self.tableListeEmprunt.setRowCount(0)
        self.tableListeEmprunt.horizontalHeader().setCascadingSectionResizes(False)
        self.groupBox = QGroupBox(Fenetre_liste_Emprunt)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 840, 311))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.raise_()
        self.tableListeEmprunt.raise_()
        self.tableListeEmprunt.setColumnWidth(0, 150)
        self.tableListeEmprunt.setColumnWidth(1, 150)
        self.tableListeEmprunt.setColumnWidth(2, 150)
        self.tableListeEmprunt.setColumnWidth(3, 150)
        self.tableListeEmprunt.setColumnWidth(4, 150)
        self.tableListeEmprunt.setColumnWidth(5, 150)
        self.tableListeEmprunt.setColumnWidth(6, 150)
        self.retranslateUi(Fenetre_liste_Emprunt)
        QMetaObject.connectSlotsByName(Fenetre_liste_Emprunt)
        self.affichier_liste_Emprunts(self.tableListeEmprunt)

    def retranslateUi(self, Fenetre_liste_Emprunt):

        Fenetre_liste_Emprunt.setWindowTitle(QCoreApplication.translate("Fenetre_liste_Emprunt", u"Affichier liste des emprunts", None))
        ___qtablewidgetitem = self.tableListeEmprunt.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText("Num\u00e9ro de l'adh\u00e9rent")

        ___qtablewidgetitem1 = self.tableListeEmprunt.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText("Nom de l'adh\u00e9rent")

        ___qtablewidgetitem2 = self.tableListeEmprunt.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText("Pr\u00e9nom de l'adh\u00e9rent")

        ___qtablewidgetitem3 = self.tableListeEmprunt.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText("ISBN")

        ___qtablewidgetitem4 = self.tableListeEmprunt.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText("Titre du livre")

        ___qtablewidgetitem5 = self.tableListeEmprunt.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText("Date emprunt")

        ___qtablewidgetitem6 = self.tableListeEmprunt.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText("Date de retour")

        self.groupBox.setTitle(QCoreApplication.translate("Fenetre_liste_Emprunt", u"Liste des emprunts", None))

    def affichier_liste_Emprunts(self, tableListeEmprunt):
        Bib().afficher_liste_emprunt(tableListeEmprunt)