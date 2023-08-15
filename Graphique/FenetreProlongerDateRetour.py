# -*- coding: utf-8 -*-
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QGroupBox, QLabel, QPushButton, QDialog, QSpinBox, QLineEdit)
from Modele import Bibliotheque as Bib

class FenetreProlongerDateRetour(QDialog):
    def setupUi(self, prolongerDateRetour):
        if not prolongerDateRetour.objectName():
             prolongerDateRetour.setObjectName(u"prolongerDateRetour")
        prolongerDateRetour.setFixedSize(365, 300)

        self.numEmpruntLine = QLineEdit(prolongerDateRetour)
        self.numEmpruntLine.setObjectName(u"numEmpruntLine")
        self.numEmpruntLine.setGeometry(QRect(180, 100, 120, 21))

        self.ISBNlbl = QLabel(prolongerDateRetour)
        self.ISBNlbl.setObjectName(u"ISBN")
        self.ISBNlbl.setGeometry(QRect(132, 100, 120, 21))
        font = QFont()
        font.setPointSize(12)
        self.ISBNlbl.setFont(font)

        self.nbrJoursLine = QSpinBox(prolongerDateRetour)
        self.nbrJoursLine.setMinimum(1)
        self.nbrJoursLine.setMaximum(7)
        self.nbrJoursLine.setObjectName(u"nbrJoursLine")
        self.nbrJoursLine.setGeometry(QRect(180, 140, 120, 21))

        self.nbrJoursLbl = QLabel(prolongerDateRetour)
        self.nbrJoursLbl.setObjectName(u"nbrJoursLbl")
        self.nbrJoursLbl.setGeometry(QRect(45, 140, 150, 21))
        font = QFont()
        font.setPointSize(12)
        self.nbrJoursLbl.setFont(font)

        font2 = QFont()
        font2.setPointSize(11)
        self.messageProlongerDateRetourLbl = QLabel(prolongerDateRetour)
        self.messageProlongerDateRetourLbl.setObjectName(u"messageProlongerDateRetourLbl")
        self.messageProlongerDateRetourLbl.setGeometry(QRect(48, 167, 321, 71))
        self.messageProlongerDateRetourLbl.setFont(font2)
        self.messageProlongerDateRetourLbl.setVisible(False)

        self.prolongerDateRetourBtn = QPushButton(prolongerDateRetour)
        self.prolongerDateRetourBtn.setObjectName(u"ajouterAdherentBtn")
        self.prolongerDateRetourBtn.setGeometry(QRect(230, 190, 75, 35))

        font1 = QFont()
        font1.setBold(True)
        self.prolongerDateRetourBtn.setFont(font1)
        self.groupBoxProlongerDateRetour = QGroupBox(prolongerDateRetour)
        self.groupBoxProlongerDateRetour.setObjectName(u"groupBoxProlongerDateRetour")
        self.groupBoxProlongerDateRetour.setGeometry(QRect(30, 50, 300, 191))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.groupBoxProlongerDateRetour.setFont(font2)
        self.groupBoxProlongerDateRetour.raise_()
        self.nbrJoursLine.raise_()
        self.nbrJoursLbl.raise_()
        self.prolongerDateRetourBtn.raise_()
        self.retranslateUi(prolongerDateRetour)
        QMetaObject.connectSlotsByName(prolongerDateRetour)
        self.numEmpruntLine.raise_()

    def retranslateUi(self, prolongerDateRetour):
        prolongerDateRetour.setWindowTitle(QCoreApplication.translate("prolongerDateRetour", u"Prolonger date de retour", None))
        self.nbrJoursLbl.setText(QCoreApplication.translate("prolongerDateRetour", u"Nombre de jours:", None))
        self.ISBNlbl.setText(QCoreApplication.translate("ISBN", u"ISBN:", None))
        self.prolongerDateRetourBtn.setText(QCoreApplication.translate("prolongerDateRetour", u"Prolonger", None))
        self.prolongerDateRetourBtn.clicked.connect(self.prolongerDateRetour)
        self.groupBoxProlongerDateRetour.setTitle(
            QCoreApplication.translate("prolongerDateRetour", u"prolonger date de retour", None))

    def prolongerDateRetour(self):
        self.nbr_jour = self.nbrJoursLine.text()
        self.numeroISBN = self.numEmpruntLine.text()
        if self.numeroISBN != "":
            bibliotheque = Bib.Bibliotheque()
            bibliotheque.prolonger_date_retour_livre(self, self.numeroISBN, self.nbr_jour)
