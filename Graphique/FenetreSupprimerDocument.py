# -*- coding: utf-8 -*-
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QGroupBox, QLabel, QPushButton, QDialog, QLineEdit)
from Modele import Bibliotheque as Bib

class FenetreSupprimerDocument(QDialog):
    def setupUi(self, Supprimer_Document):
        if not Supprimer_Document.objectName():
             Supprimer_Document.setObjectName(u"Supprimer_Document")
        Supprimer_Document.setFixedSize(400, 300)
        self.numDocumentLine = QLineEdit(Supprimer_Document)
        self.numDocumentLine.setObjectName(u"numDocumentLine")
        self.numDocumentLine.setGeometry(QRect(130, 100, 201, 21))

        self.numDocumentLbl = QLabel(Supprimer_Document)
        self.numDocumentLbl.setObjectName(u"numDocumentLbl")
        self.numDocumentLbl.setGeometry(QRect(50, 100, 60, 16))
        font = QFont()
        font.setPointSize(12)
        self.numDocumentLbl.setFont(font)
        font2 = QFont()
        font2.setPointSize(11)
        self.messageSuppressionDocumentLbl = QLabel(Supprimer_Document)
        self.messageSuppressionDocumentLbl.setObjectName(u"messageSuppressionDocumentLbl")
        self.messageSuppressionDocumentLbl.setGeometry(QRect(40, 120, 321, 71))
        self.messageSuppressionDocumentLbl.setFont(font2)
        self.supprimerDocumentBtn = QPushButton(Supprimer_Document)
        self.supprimerDocumentBtn.setObjectName(u"ajouterDocumentBtn")
        self.supprimerDocumentBtn.setGeometry(QRect(260, 190, 75, 35))
        font1 = QFont()
        font1.setBold(True)
        self.supprimerDocumentBtn.setFont(font1)
        self.groupBoxSupprimerDocument = QGroupBox(Supprimer_Document)
        self.groupBoxSupprimerDocument.setObjectName(u"groupBoxSupprimerDocument")
        self.groupBoxSupprimerDocument.setGeometry(QRect(30, 50, 341, 191))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.groupBoxSupprimerDocument.setFont(font2)
        self.groupBoxSupprimerDocument.raise_()
        self.numDocumentLine.raise_()
        self.numDocumentLbl.raise_()
        self.supprimerDocumentBtn.raise_()
        self.retranslateUi(Supprimer_Document)
        QMetaObject.connectSlotsByName(Supprimer_Document)

    def retranslateUi(self, Supprimer_Document):
        Supprimer_Document.setWindowTitle(QCoreApplication.translate("Supprimer_Document", u"Supprimer un document", None))
        self.numDocumentLbl.setText(QCoreApplication.translate("Supprimer_Document", u"N° ISBN:", None))
        self.messageSuppressionDocumentLbl.setText(QCoreApplication.translate("Supprimer_Document",
                                                                              u"Veuillez saisir le num\u00e9ro ISBN à suprimer!",
                                                                              None))
        self.supprimerDocumentBtn.setText(QCoreApplication.translate("Supprimer_Document", u"Supprimer", None))
        self.supprimerDocumentBtn.clicked.connect(self.supprimer_Document)
        self.groupBoxSupprimerDocument.setTitle(
            QCoreApplication.translate("Supprimer_Document", u"Supprimer un document", None))

    def supprimer_Document(self):
        numero = self.numDocumentLine.text()
        if numero != "":
            bibliotheque = Bib.Bibliotheque()
            bibliotheque.supprimer_document(self, numero)

