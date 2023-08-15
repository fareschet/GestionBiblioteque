# -*- coding: utf-8 -*-
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QGroupBox, QLabel, QPushButton, QDialog, QLineEdit)
from Modele import Bibliotheque as Bib

class FenetreSupprimerEmprunt(QDialog):
    def setupUi(self, Supprimer_Emprunt):
        if not Supprimer_Emprunt.objectName():
             Supprimer_Emprunt.setObjectName(u"Supprimer_Emprunt")
        Supprimer_Emprunt.setFixedSize(400, 300)
        self.numEmpruntLine = QLineEdit(Supprimer_Emprunt)
        self.numEmpruntLine.setObjectName(u"numEmpruntLine")
        self.numEmpruntLine.setGeometry(QRect(130, 100, 201, 21))

        self.numEmpruntLbl = QLabel(Supprimer_Emprunt)
        self.numEmpruntLbl.setObjectName(u"numEmpruntLbl")
        self.numEmpruntLbl.setGeometry(QRect(50, 100, 60, 16))
        font = QFont()
        font.setPointSize(12)
        self.numEmpruntLbl.setFont(font)
        font2 = QFont()
        font2.setPointSize(11)
        self.messageSuppressionEmpruntLbl = QLabel(Supprimer_Emprunt)
        self.messageSuppressionEmpruntLbl.setObjectName(u"messageSuppressionEmpruntLbl")
        self.messageSuppressionEmpruntLbl.setGeometry(QRect(40, 120, 321, 71))
        self.messageSuppressionEmpruntLbl.setFont(font2)
        self.supprimerEmpruntBtn = QPushButton(Supprimer_Emprunt)
        self.supprimerEmpruntBtn.setObjectName(u"ajouterEmpruntBtn")
        self.supprimerEmpruntBtn.setGeometry(QRect(260, 190, 75, 35))
        font1 = QFont()
        font1.setBold(True)
        self.supprimerEmpruntBtn.setFont(font1)
        self.groupBoxSupprimerEmprunt = QGroupBox(Supprimer_Emprunt)
        self.groupBoxSupprimerEmprunt.setObjectName(u"groupBoxSupprimerEmprunt")
        self.groupBoxSupprimerEmprunt.setGeometry(QRect(30, 50, 341, 191))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.groupBoxSupprimerEmprunt.setFont(font2)
        self.groupBoxSupprimerEmprunt.raise_()
        self.numEmpruntLine.raise_()
        self.numEmpruntLbl.raise_()
        self.supprimerEmpruntBtn.raise_()
        self.retranslateUi(Supprimer_Emprunt)
        QMetaObject.connectSlotsByName(Supprimer_Emprunt)

    def retranslateUi(self, Supprimer_Emprunt):
        Supprimer_Emprunt.setWindowTitle(QCoreApplication.translate("Supprimer_Emprunt", u"Supprimer un emprunt", None))
        self.numEmpruntLbl.setText(QCoreApplication.translate("Supprimer_Emprunt", u"ISBN:", None))
        self.messageSuppressionEmpruntLbl.setText(QCoreApplication.translate("Supprimer_Emprunt",
                                                                              u"Veuillez saisir le num\u00e9ro ISBN \u00e0 suprimer!",
                                                                              None))
        self.supprimerEmpruntBtn.setText(QCoreApplication.translate("Supprimer_Emprunt", u"Supprimer", None))
        self.supprimerEmpruntBtn.clicked.connect(self.supprimer_Emprunt)
        self.groupBoxSupprimerEmprunt.setTitle(
            QCoreApplication.translate("Supprimer_Emprunt", u"Supprimer un emprunt", None))

    def supprimer_Emprunt(self):
        self.numero= self.numEmpruntLine.text()
        if self.numero != "":
            bibliotheque = Bib.Bibliotheque()
            bibliotheque.supprimer_emprunt(self, self.numero)
