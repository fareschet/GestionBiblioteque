# -*- coding: utf-8 -*-
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QCheckBox, QDialog, QGroupBox, QLabel, QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem)
from Modele import Bibliotheque as Bib

class FenetreAfficherListeDocument(QDialog):
    def setupUi(self, ListeDocument):
        if not ListeDocument.objectName():
            ListeDocument.setObjectName(u"ListeDocument")
        ListeDocument.setFixedSize(661, 466)
        self.ListeDocumentgroupBox = QGroupBox(ListeDocument)
        self.ListeDocumentgroupBox.setObjectName(u"groupBox")
        self.ListeDocumentgroupBox.setGeometry(QRect(50, 30, 581, 385))
        font0 = QFont()
        font0.setPointSize(12)
        font0.setBold(True)
        self.ListeDocumentgroupBox.setFont(font0)

        self.ListeDocumentlistWidget = QListWidget(self.ListeDocumentgroupBox)
        self.ListeDocumentlistWidget.setObjectName(u"listWidget")
        self.ListeDocumentlistWidget.setGeometry(QRect(300, 35, 211, 27))
        self.ListeDocumentlistWidget.setStyleSheet("font-size: 15px; font-weight: normal;")
        QListWidgetItem(self.ListeDocumentlistWidget)
        QListWidgetItem(self.ListeDocumentlistWidget)
        QListWidgetItem(self.ListeDocumentlistWidget)
        QListWidgetItem(self.ListeDocumentlistWidget)
        QListWidgetItem(self.ListeDocumentlistWidget)
        self.ListeDocumentlistWidget.itemClicked.connect(self.afficher_option_liste_document)

        self.ListeDocumentlabel = QLabel(self.ListeDocumentgroupBox)
        self.ListeDocumentlabel.setObjectName(u"label")
        self.ListeDocumentlabel.setGeometry(QRect(10, 30, 301, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.ListeDocumentlabel.setFont(font1)

        self.ListeDocumenttableWidget = QTableWidget(self.ListeDocumentgroupBox)
        if (self.ListeDocumenttableWidget.columnCount() < 4):
            self.ListeDocumenttableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.ListeDocumenttableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ListeDocumenttableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ListeDocumenttableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ListeDocumenttableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.ListeDocumenttableWidget.raise_()
        self.ListeDocumenttableWidget.setObjectName(u"ListeDocumenttableWidget")
        self.ListeDocumenttableWidget.setGeometry(QRect(30, 150, 521, 201))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        self.ListeDocumenttableWidget.setStyleSheet("font-size: 12px; font-weight: normal;")

        self.ListeDocumentLivresDisponibles = QLabel(self.ListeDocumentgroupBox)
        self.ListeDocumentLivresDisponibles.setObjectName(u"label_2")
        self.ListeDocumentLivresDisponibles.setGeometry(QRect(30, 75, 221, 21))
        self.ListeDocumentLivresDisponibles.setFont(font2)

        self.ListeDocumentLivresEmpruntes = QLabel(self.ListeDocumentgroupBox)
        self.ListeDocumentLivresEmpruntes.setObjectName(u"label_3")
        self.ListeDocumentLivresEmpruntes.setGeometry(QRect(30, 100, 201, 31))
        self.ListeDocumentLivresEmpruntes.setFont(font2)

        self.ListeDocumentcheckBox = QCheckBox(self.ListeDocumentgroupBox)
        self.ListeDocumentcheckBox.setObjectName(u"checkBox")
        self.ListeDocumentcheckBox.setGeometry(QRect(250, 80, 75, 20))
        self.ListeDocumentcheckBox.setFont(font2)
        self.ListeDocumentcheckBox.setTristate(False)


        self.ListeDocumentcheckBox_2 = QCheckBox(self.ListeDocumentgroupBox)
        self.ListeDocumentcheckBox_2.setObjectName(u"checkBox_2")
        self.ListeDocumentcheckBox_2.setGeometry(QRect(250, 110, 75, 20))

        self.retranslateUi(ListeDocument)

        self.cacher_autre_option()

        QMetaObject.connectSlotsByName(ListeDocument)

    def retranslateUi(self, ListeDocument):
        ListeDocument.setWindowTitle(QCoreApplication.translate("ListeDocument", u"Afficher la liste des documents", None))
        self.ListeDocumentgroupBox.setTitle(QCoreApplication.translate("ListeDocument", u"Afficher la liste des documents", None))
        self.ListeDocumentlabel.setText(QCoreApplication.translate("ListeDocument", u"Choisir le type de document \u00e0 afficher:", None))
        self.afficher_liste_journal()
        self.ListeDocumentLivresDisponibles.setText(QCoreApplication.translate("ListeDocument", u"Afficher les  livres disponibles:", None))
        self.ListeDocumentLivresEmpruntes.setText(QCoreApplication.translate("ListeDocument", u"Afficher les livres emprunt\u00e9s:", None))
        self.ListeDocumentcheckBox.setText("")
        self.ListeDocumentcheckBox_2.setText("")
        self.ListeDocumentlistWidget.setSortingEnabled(False)

        __sortingEnabled = self.ListeDocumentlistWidget.isSortingEnabled()
        ___qlistwidgetitem = self.ListeDocumentlistWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("listWidget", u"Choisir...", None));
        ___qlistwidgetitem1 = self.ListeDocumentlistWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("listWidget", u"Journal", None));
        ___qlistwidgetitem2 = self.ListeDocumentlistWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("listWidget", u"Livre", None));
        ___qlistwidgetitem3 = self.ListeDocumentlistWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("listWidget", u"Dictionnaire", None));
        ___qlistwidgetitem4 = self.ListeDocumentlistWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("listWidget", u"Bande dessinee", None));
        self.ListeDocumentlistWidget.setSortingEnabled(__sortingEnabled)

    def afficher_liste_journal(self):
        self.ListeDocumentLivresEmpruntes.setVisible(False)
        self.ListeDocumentLivresDisponibles.setVisible(False)
        self.ListeDocumenttableWidget.setVisible(True)
        self.ListeDocumentcheckBox.setVisible(False)
        self.ListeDocumentcheckBox_2.setVisible(False)
        ___qtablewidgetitem = self.ListeDocumenttableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ListeDocument", u"ISBN", None));
        ___qtablewidgetitem1 = self.ListeDocumenttableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ListeDocument", u"Titre", None));
        ___qtablewidgetitem2 = self.ListeDocumenttableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ListeDocument", u"Date \u00e9dition", None));
        self.ListeDocumenttableWidget.setColumnWidth(0, 150)
        self.ListeDocumenttableWidget.setColumnWidth(1, 230)
        self.ListeDocumenttableWidget.setColumnWidth(2, 150)
        self.ListeDocumenttableWidget.setColumnWidth(3, 0)
        self.ListeDocumenttableWidget.setGeometry(QRect(30, 100, 521, 250))


    def afficher_liste_livre(self):
        self.ListeDocumentLivresEmpruntes.setVisible(True)
        self.ListeDocumentLivresDisponibles.setVisible(True)
        self.ListeDocumenttableWidget.setVisible(True)
        self.ListeDocumentcheckBox.setVisible(True)
        self.ListeDocumentcheckBox_2.setVisible(True)
        self.ListeDocumenttableWidget.setGeometry(QRect(30, 150, 521, 201))
        self.ListeDocumenttableWidget.setColumnWidth(0, 150)
        self.ListeDocumenttableWidget.setColumnWidth(1, 230)
        self.ListeDocumenttableWidget.setColumnWidth(2, 150)
        self.ListeDocumenttableWidget.setColumnWidth(3, 0)
        ___qtablewidgetitem = self.ListeDocumenttableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ListeDocument", u"ISBN", None));
        ___qtablewidgetitem1 = self.ListeDocumenttableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ListeDocument", u"Titre", None));
        ___qtablewidgetitem2 = self.ListeDocumenttableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ListeDocument", u"Auteur", None));
        ___qtablewidgetitem2 = self.ListeDocumenttableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ListeDocument", u"Disponibilité", None));
        self.ListeDocumenttableWidget.setColumnWidth(0, 150)
        self.ListeDocumenttableWidget.setColumnWidth(1, 150)
        self.ListeDocumenttableWidget.setColumnWidth(2, 150)
        self.ListeDocumenttableWidget.setColumnWidth(3, 150)

    def afficher_liste_dictionnaire(self):
        self.ListeDocumentLivresEmpruntes.setVisible(False)
        self.ListeDocumentLivresDisponibles.setVisible(False)
        self.ListeDocumenttableWidget.setVisible(True)
        self.ListeDocumentcheckBox.setVisible(False)
        self.ListeDocumentcheckBox_2.setVisible(False)
        self.ListeDocumenttableWidget.setGeometry(QRect(30, 100, 521, 250))
        ___qtablewidgetitem = self.ListeDocumenttableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ListeDocument", u"ISBN", None));
        ___qtablewidgetitem1 = self.ListeDocumenttableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ListeDocument", u"Titre", None));
        ___qtablewidgetitem2 = self.ListeDocumenttableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ListeDocument", u"Auteur", None));
        self.ListeDocumenttableWidget.setColumnWidth(0, 150)
        self.ListeDocumenttableWidget.setColumnWidth(1, 230)
        self.ListeDocumenttableWidget.setColumnWidth(2, 150)
        self.ListeDocumenttableWidget.setColumnWidth(3, 0)


    def afficher_liste_bande_dessinee(self):
        self.ListeDocumentLivresEmpruntes.setVisible(False)
        self.ListeDocumentLivresDisponibles.setVisible(False)
        self.ListeDocumenttableWidget.setVisible(True)
        self.ListeDocumentcheckBox.setVisible(False)
        self.ListeDocumentcheckBox_2.setVisible(False)
        self.ListeDocumenttableWidget.setGeometry(QRect(30, 100, 521, 250))
        ___qtablewidgetitem = self.ListeDocumenttableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ListeDocument", u"ISBN", None));
        ___qtablewidgetitem1 = self.ListeDocumenttableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ListeDocument", u"Titre", None));
        ___qtablewidgetitem2 = self.ListeDocumenttableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ListeDocument", u"Auteur", None));
        ___qtablewidgetitem2 = self.ListeDocumenttableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ListeDocument", u"Dessinateur", None));
        self.ListeDocumenttableWidget.setColumnWidth(0, 150)
        self.ListeDocumenttableWidget.setColumnWidth(1, 150)
        self.ListeDocumenttableWidget.setColumnWidth(2, 150)
        self.ListeDocumenttableWidget.setColumnWidth(3, 150)

    def afficher_option_liste_document(self):
        choix = self.ListeDocumentlistWidget.currentItem().text()
        if choix == "Journal":
            self.ListeDocumenttableWidget.clearContents()
            self.afficher_liste_journal()
            Bib.Bibliotheque().afficher_liste_document(self, self.ListeDocumenttableWidget, choix)

        elif choix == "Livre":
            self.ListeDocumenttableWidget.clearContents()
            self.afficher_liste_livre()
            self.ListeDocumentcheckBox.clicked.connect(self.verifier_case_cochee_livre_disponible)
            self.ListeDocumentcheckBox_2.clicked.connect(self.verifier_case_cochee_livre_non_disponible)
            Bib.Bibliotheque().afficher_liste_document(self, self.ListeDocumenttableWidget, choix)

        elif choix == "Dictionnaire":
            self.ListeDocumenttableWidget.clearContents()
            self.afficher_liste_dictionnaire()
            Bib.Bibliotheque().afficher_liste_document(self, self.ListeDocumenttableWidget, choix)

        elif choix == "Bande dessinee":
            self.ListeDocumenttableWidget.clearContents()
            self.afficher_liste_bande_dessinee()
            Bib.Bibliotheque().afficher_liste_document(self, self.ListeDocumenttableWidget, choix)

        elif choix == "Choisir...":
            self.ListeDocumenttableWidget.clearContents()
            self.cacher_autre_option()

        return choix

    def cacher_autre_option(self):
        self.ListeDocumentLivresEmpruntes.setVisible(False)
        self.ListeDocumentLivresDisponibles.setVisible(False)
        self.ListeDocumenttableWidget.setVisible(False)
        self.ListeDocumentcheckBox.setVisible(False)
        self.ListeDocumentcheckBox_2.setVisible(False)

    def verifier_case_cochee_livre_disponible(self):
        choix = "Livre"
        if self.ListeDocumentcheckBox.isChecked():
            self.ListeDocumentcheckBox_2.setChecked(False)
            Bib.Bibliotheque().afficher_liste_document(self, self.ListeDocumenttableWidget, choix)
        else:
            Bib.Bibliotheque().afficher_liste_document(self, self.ListeDocumenttableWidget, choix)


    def verifier_case_cochee_livre_non_disponible(self):
        choix = "Livre"
        if self.ListeDocumentcheckBox_2.isChecked():
            self.ListeDocumentcheckBox.setChecked(False)
            Bib.Bibliotheque().afficher_liste_document(self, self.ListeDocumenttableWidget, choix)
        else:
            Bib.Bibliotheque().afficher_liste_document(self, self.ListeDocumenttableWidget, choix)


