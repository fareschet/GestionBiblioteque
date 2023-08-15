# -*- coding: utf-8 -*-
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QGroupBox, QLabel, QPushButton, QDialog, QLineEdit)
from Modele import Bibliotheque as Bib

class FenetreSupprimerAdherent(QDialog):
    def setupUi(self, Supprimer_Adherent):
        if not Supprimer_Adherent.objectName():
             Supprimer_Adherent.setObjectName(u"Supprimer_Adherent")
        Supprimer_Adherent.setFixedSize(400, 300)
        self.numAdherentLine = QLineEdit(Supprimer_Adherent)
        self.numAdherentLine.setObjectName(u"nbrJoursLine")
        self.numAdherentLine.setGeometry(QRect(130, 100, 201, 21))

        self.numAdherentLbl = QLabel(Supprimer_Adherent)
        self.numAdherentLbl.setObjectName(u"nbrJoursLbl")
        self.numAdherentLbl.setGeometry(QRect(50, 100, 60, 16))
        font = QFont()
        font.setPointSize(12)
        self.numAdherentLbl.setFont(font)
        font2 = QFont()
        font2.setPointSize(11)
        self.messageSuppressionAdherentLbl = QLabel(Supprimer_Adherent)
        self.messageSuppressionAdherentLbl.setObjectName(u"messageSuppressionAdherentLbl")
        self.messageSuppressionAdherentLbl.setGeometry(QRect(40, 120, 321, 71))
        self.messageSuppressionAdherentLbl.setFont(font2)
        self.supprimerAdherentBtn = QPushButton(Supprimer_Adherent)
        self.supprimerAdherentBtn.setObjectName(u"ajouterAdherentBtn")
        self.supprimerAdherentBtn.setGeometry(QRect(260, 190, 75, 35))
        font1 = QFont()
        font1.setBold(True)
        self.supprimerAdherentBtn.setFont(font1)
        self.groupBoxSupprimerAdhrent = QGroupBox(Supprimer_Adherent)
        self.groupBoxSupprimerAdhrent.setObjectName(u"groupBoxProlongerDateRetour")
        self.groupBoxSupprimerAdhrent.setGeometry(QRect(30, 50, 341, 191))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.groupBoxSupprimerAdhrent.setFont(font2)
        self.groupBoxSupprimerAdhrent.raise_()
        self.numAdherentLine.raise_()
        self.numAdherentLbl.raise_()
        self.supprimerAdherentBtn.raise_()
        self.retranslateUi(Supprimer_Adherent)
        QMetaObject.connectSlotsByName(Supprimer_Adherent)

    def retranslateUi(self, Supprimer_Adherent):
        Supprimer_Adherent.setWindowTitle(QCoreApplication.translate("Supprimer_Adherent", u"Supprimer un adhérent", None))
        self.numAdherentLbl.setText(QCoreApplication.translate("Supprimer_Adherent", u"Numéro:", None))
        self.messageSuppressionAdherentLbl.setText(QCoreApplication.translate("Supprimer_Adherent",
                                                                              u"Veuillez saisir le num\u00e9ro \u00e9tudiant \u00e0 suprimer!",
                                                                              None))
        self.supprimerAdherentBtn.setText(QCoreApplication.translate("Supprimer_Adherent", u"Supprimer", None))
        self.supprimerAdherentBtn.clicked.connect(self.supprimer_adherent)
        self.groupBoxSupprimerAdhrent.setTitle(
            QCoreApplication.translate("Supprimer_Adherent", u"Supprimer un adh\u00e9rent", None))

    def supprimer_adherent(self):
        self.numero= self.numAdherentLine.text()
        if self.numero != "":
            bibliotheque = Bib.Bibliotheque()
            bibliotheque.supprimerAdherant(self, self.numero)
