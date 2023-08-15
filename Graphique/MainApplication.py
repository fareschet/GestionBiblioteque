from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy, QDialog,
    QStatusBar, QTabWidget, QWidget, QLineEdit)
from Graphique.FenetreAjouterAdherent import FenetreAjouterAdherent
from Graphique.FenetreSupprimerAdherent import FenetreSupprimerAdherent
from Graphique.FenetreListeAdherants import FenetreListeAdherants
from Graphique.FenetreAjouterDocument import FenetreAjouterDocument
from Graphique.FenetreSupprimerDocument import FenetreSupprimerDocument
from Graphique.FenetreAfficherListeDocument import FenetreAfficherListeDocument
from Graphique.FenetreAjouteEmprunt import FenetreAjouterEmprunt
from Graphique.FenetreSupprimerEmprunt import FenetreSupprimerEmprunt
from Graphique.FenetreProlongerDateRetour import FenetreProlongerDateRetour
from Graphique.FenetreListeEmprunt import FenetreListeEmprunt
from Modele.Bibliotheque import Bibliotheque as Bib
import sys
import os
class PagePrincipale(QMainWindow):

    font = QFont()
    font.setPointSize(12)
    font.setBold(False)

    font2 = QFont()
    font2.setPointSize(11)
    font2.setBold(False)

    font3 = QFont()
    font3.setPointSize(12)
    font3.setBold(True)

    icon = QIcon()
    icon1 = QIcon()
    icon2 = QIcon()
    icon3 = QIcon()
    icon4 = QIcon()

    def setupUi(self, page_principale):
        user = os.getlogin()
        if not page_principale.objectName():
            page_principale.setObjectName(u"page_principale")
        page_principale.setFixedSize(525, 530)
        self.icon.addFile("./icones/stylo.png", QSize())
        self.icon1.addFile("./icones/poubelle.png", QSize())
        self.icon2.addFile("./icones/liste.png", QSize())
        self.icon3.addFile("./icones/agrandir.png", QSize())
        self.icon4.addFile("./icones/save.png", QSize())
        self.afficher_page_principale(page_principale)
        self.gerer_adherent(page_principale)
        self.gerer_document(page_principale)
        self.gerer_emprunt(page_principale)
        self.enregistrer_modifications_affichage(page_principale)

    def afficher_page_principale(self, page_principale):
        self.centralwidget = QWidget(page_principale)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(True)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gestionDocumentLabel = QTabWidget(self.centralwidget)
        self.gestionDocumentLabel.setObjectName(u"gestionDocumentLabel")
        self.gestionDocumentLabel.setAutoFillBackground(True)
        self.gestionDocumentLabel.setTabBarAutoHide(False)

    def gerer_adherent(self, page_principale):
        self.GestionAdherentsMenu = QWidget()
        self.GestionAdherentsMenu.setObjectName(u"GestionAdherentsMenu")
        self.GestionAdherentsMenu.setToolTipDuration(-1)
        self.GestionAdherentsMenu.setAutoFillBackground(False)
        self.GestionAdherentsMenu.setStyleSheet(u"")

        self.ajouterAdherentLbl = QLabel(self.GestionAdherentsMenu)
        self.ajouterAdherentLbl.setObjectName(u"ajouterAdherentLbl")
        self.ajouterAdherentLbl.setGeometry(QRect(120, 205, 161, 21))
        self.ajouterAdherentLbl.setFont(self.font)

        self.supprimerAdherentLbl = QLabel(self.GestionAdherentsMenu)
        self.supprimerAdherentLbl.setObjectName(u"supprimerAdherentLbl")
        self.supprimerAdherentLbl.setGeometry(QRect(130, 241, 151, 51))
        self.supprimerAdherentLbl.setFont(self.font)

        self.groupBox = QGroupBox(self.GestionAdherentsMenu)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 160, 401, 200))
        self.groupBox.setFont(self.font3)

        self.AjouterAdherentBtn = QPushButton(self.groupBox)
        self.AjouterAdherentBtn.setObjectName(u"ajouterAdherentBtn")
        self.AjouterAdherentBtn.setGeometry(QRect(260, 40, 41, 31))
        self.AjouterAdherentBtn.clicked.connect(self.afficher_fenetre_ajouter_adherent)
        self.AjouterAdherentBtn.setFont(self.font2)
        self.AjouterAdherentBtn.setIcon(self.icon)

        self.SupprimerAdherentBtn = QPushButton(self.groupBox)
        self.SupprimerAdherentBtn.setObjectName(u"SupprimerAdherentBtn")
        self.SupprimerAdherentBtn.setGeometry(QRect(260, 90, 41, 31))
        self.SupprimerAdherentBtn.clicked.connect(self.afficher_fenetre_Supprimer_adherent)
        self.SupprimerAdherentBtn.setFont(self.font2)
        self.SupprimerAdherentBtn.setIcon(self.icon1)

        self.AfficherListeAdherentBtn = QPushButton(self.groupBox)
        self.AfficherListeAdherentBtn.setObjectName(u"AfficherListeAdherentBtn")
        self.AfficherListeAdherentBtn.setGeometry(QRect(260, 140, 41, 31))
        self.AfficherListeAdherentBtn.setFont(self.font2)
        self.AfficherListeAdherentBtn.clicked.connect(self.afficher_fenetre_Liste_adherent)
        self.AfficherListeAdherentBtn.setIcon(self.icon2)

        self.afficherListeadherentsLbl = QLabel(self.groupBox)
        self.afficherListeadherentsLbl.setObjectName(u"afficherListeadherentsLbl")
        self.afficherListeadherentsLbl.setGeometry(QRect(30, 120, 201, 71))
        self.afficherListeadherentsLbl.setFont(self.font)

        self.gestionDocumentLabel.addTab(self.GestionAdherentsMenu, "")
        self.groupBox.raise_()
        self.ajouterAdherentLbl.raise_()
        self.supprimerAdherentLbl.raise_()

        #self.enregistrer_modifications_affichage()

    def gerer_document(self, page_principale):
        self.GestionDocumentsMenu = QWidget()
        self.GestionDocumentsMenu.setObjectName(u"GestionDocumentsMenu")
        self.groupBox_2 = QGroupBox(self.GestionDocumentsMenu)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(50, 160, 401, 221))
        self.groupBox_2.setFont(self.font3)

        self.AjouterDocumentBtn = QPushButton(self.groupBox_2)
        self.AjouterDocumentBtn.clicked.connect(self.afficher_fenetre_ajouter_document)
        self.AjouterDocumentBtn.setObjectName(u"AjouterDocumentBtn")
        self.AjouterDocumentBtn.setGeometry(QRect(260, 40, 41, 31))
        self.AjouterDocumentBtn.setFont(self.font2)
        self.AjouterDocumentBtn.setIcon(self.icon)

        self.SupprimerDocumentBtn = QPushButton(self.groupBox_2)
        self.SupprimerDocumentBtn.setObjectName(u"SupprimerDocumentBtn")
        self.SupprimerDocumentBtn.clicked.connect(self.afficher_fenetre_supprimer_document)
        self.SupprimerDocumentBtn.setGeometry(QRect(260, 90, 41, 31))
        self.SupprimerDocumentBtn.setFont(self.font2)
        self.SupprimerDocumentBtn.setIcon(self.icon1)

        self.AfficherListeDocumentBtn = QPushButton(self.groupBox_2)
        self.AfficherListeDocumentBtn.setObjectName(u"AfficherListeDocumentBtn")
        self.AfficherListeDocumentBtn.clicked.connect(self.afficher_fenetre_liste_document)
        self.AfficherListeDocumentBtn.setGeometry(QRect(260, 140, 41, 31))
        self.AfficherListeDocumentBtn.setFont(self.font2)
        self.AfficherListeDocumentBtn.setIcon(self.icon2)

        self.supprimerDocumentLbl = QLabel(self.groupBox_2)
        self.supprimerDocumentLbl.setObjectName(u"supprimerDocumentLbl")
        self.supprimerDocumentLbl.setGeometry(QRect(60, 80, 181, 51))
        self.supprimerDocumentLbl.setFont(self.font)

        self.afficherListeDocumentsLbl = QLabel(self.groupBox_2)
        self.afficherListeDocumentsLbl.setObjectName(u"afficherListeDocumentsLbl")
        self.afficherListeDocumentsLbl.setGeometry(QRect(30, 120, 241, 71))
        self.afficherListeDocumentsLbl.setFont(self.font)

        self.ajouterDocumentLbl = QLabel(self.groupBox_2)
        self.ajouterDocumentLbl.setObjectName(u"ajouterDocumentLbl")
        self.ajouterDocumentLbl.setGeometry(QRect(50, 40, 191, 21))
        self.ajouterDocumentLbl.setFont(self.font)
        self.gestionDocumentLabel.addTab(self.GestionDocumentsMenu, "")



    def gerer_emprunt(self, page_principale):
        self.GestionEmpruntsMenu = QWidget()
        self.GestionEmpruntsMenu.setObjectName(u"GestionEmpruntsMenu")
        self.groupBox_3 = QGroupBox(self.GestionEmpruntsMenu)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(50, 160, 401, 261))
        self.groupBox_3.setFont(self.font3)

        self.AjouterEmpruntBtn = QPushButton(self.groupBox_3)
        self.AjouterEmpruntBtn.setObjectName(u"AjouterEmpruntBtn")
        self.AjouterEmpruntBtn.clicked.connect(self.afficher_fenetre_ajouter_emprunt)
        self.AjouterEmpruntBtn.setGeometry(QRect(260, 50, 41, 31))
        self.AjouterEmpruntBtn.setFont(self.font2)
        self.AjouterEmpruntBtn.setIcon(self.icon)

        self.SupprimerEmpruntBtn = QPushButton(self.groupBox_3)
        self.SupprimerEmpruntBtn.setObjectName(u"SupprimerEmpruntBtn")
        self.SupprimerEmpruntBtn.setGeometry(QRect(260, 100, 41, 31))
        self.SupprimerEmpruntBtn.clicked.connect(self.afficher_fenetre_Supprimer_emprunt)
        self.SupprimerEmpruntBtn.setFont(self.font2)
        self.SupprimerEmpruntBtn.setIcon(self.icon1)

        self.AfficherListeEmprunt = QPushButton(self.groupBox_3)
        self.AfficherListeEmprunt.setObjectName(u"AfficherListeEmprunt")
        self.AfficherListeEmprunt.clicked.connect(self.afficher_fenetre_Liste_emprunt)
        self.AfficherListeEmprunt.setGeometry(QRect(260, 200, 41, 31))
        self.AfficherListeEmprunt.setFont(self.font2)
        self.AfficherListeEmprunt.setIcon(self.icon2)

        self.supprimerEmpruntLbl = QLabel(self.groupBox_3)
        self.supprimerEmpruntLbl.setObjectName(u"supprimerEmpruntLbl")
        self.supprimerEmpruntLbl.setGeometry(QRect(60, 90, 181, 51))
        self.supprimerEmpruntLbl.setFont(self.font)

        self.afficherListeEmpruntLbl = QLabel(self.groupBox_3)
        self.afficherListeEmpruntLbl.setObjectName(u"afficherListeEmpruntLbl")
        self.afficherListeEmpruntLbl.setGeometry(QRect(30, 180, 241, 71))
        self.afficherListeEmpruntLbl.setFont(self.font)

        self.ajouterEmpruntLbl = QLabel(self.groupBox_3)
        self.ajouterEmpruntLbl.setObjectName(u"ajouterEmpruntLbl")
        self.ajouterEmpruntLbl.setGeometry(QRect(50, 50, 191, 21))
        self.ajouterEmpruntLbl.setFont(self.font)

        self.prolongerdateRetourLbl = QLabel(self.groupBox_3)
        self.prolongerdateRetourLbl.setObjectName(u"prolongerdateRetourLbl")
        self.prolongerdateRetourLbl.setGeometry(QRect(40, 130, 241, 71))
        self.prolongerdateRetourLbl.setFont(self.font)

        self.ProlongerDateEmpruntBtn = QPushButton(self.groupBox_3)
        self.ProlongerDateEmpruntBtn.setObjectName(u"ProlongerDateEmpruntBtn")
        self.ProlongerDateEmpruntBtn.setGeometry(QRect(260, 150, 41, 31))
        self.ProlongerDateEmpruntBtn.clicked.connect(self.afficher_fenetre_Prolonger_date_retour)
        self.ProlongerDateEmpruntBtn.setFont(self.font2)
        self.ProlongerDateEmpruntBtn.setIcon(self.icon3)
        self.gestionDocumentLabel.addTab(self.GestionEmpruntsMenu, "")

        self.horizontalLayout.addWidget(self.gestionDocumentLabel)
        page_principale.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(page_principale)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 22))
        page_principale.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(page_principale)
        self.statusbar.setObjectName(u"statusbar")

        page_principale.setStatusBar(self.statusbar)
        self.retranslateUi(page_principale)
        self.gestionDocumentLabel.setCurrentIndex(2)
        QMetaObject.connectSlotsByName(page_principale)

    def retranslateUi(self, PagePrincipale):
        PagePrincipale.setWindowTitle(QCoreApplication.translate("page_principale", u"Gestion de bibliothèque", None))
        self.GestionAdherentsMenu.setToolTip(QCoreApplication.translate("page_principale", u"", None))
        self.ajouterAdherentLbl.setText(QCoreApplication.translate("page_principale", u"     Ajouter adh\u00e9rent:", None))
        self.supprimerAdherentLbl.setText(QCoreApplication.translate("page_principale", u"Suppimer adh\u00e9rent:", None))

        self.groupBox.setTitle(QCoreApplication.translate("page_principale", u"Gestion des adh\u00e9rents", None))
        self.AjouterAdherentBtn.setText("")
        self.SupprimerAdherentBtn.setText("")
        self.AfficherListeAdherentBtn.setText("")

        self.afficherListeadherentsLbl.setText(QCoreApplication.translate("page_principale", u"Afficher liste des adh\u00e9rents:", None))
        self.gestionDocumentLabel.setTabText(self.gestionDocumentLabel.indexOf(self.GestionAdherentsMenu), QCoreApplication.translate("page_principale", u"Gestion des adh\u00e9rents", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("page_principale", u"Gestion des documents", None))
        self.AjouterDocumentBtn.setText("")
        self.SupprimerDocumentBtn.setText("")
        self.AfficherListeDocumentBtn.setText("")

        self.supprimerDocumentLbl.setText(QCoreApplication.translate("page_principale", u"Suppimer un document:", None))
        self.afficherListeDocumentsLbl.setText(QCoreApplication.translate("page_principale", u"Afficher liste des documents:", None))
        self.ajouterDocumentLbl.setText(QCoreApplication.translate("page_principale", u"     Ajouter un document:", None))
        self.gestionDocumentLabel.setTabText(self.gestionDocumentLabel.indexOf(self.GestionDocumentsMenu), QCoreApplication.translate("page_principale", u"Gestion des documents", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("page_principale", u"Gestion des emprunts", None))
        self.AjouterEmpruntBtn.setText("")
        self.SupprimerEmpruntBtn.setText("")
        self.AfficherListeEmprunt.setText("")
        self.ProlongerDateEmpruntBtn.setText("")
        self.supprimerEmpruntLbl.setText(QCoreApplication.translate("page_principale", u"Suppimer un emprunt:", None))
        self.afficherListeEmpruntLbl.setText(QCoreApplication.translate("page_principale", u"Afficher liste des emprunts:", None))
        self.ajouterEmpruntLbl.setText(QCoreApplication.translate("page_principale", u"     Ajouter un emprunt:", None))
        self.prolongerdateRetourLbl.setText(QCoreApplication.translate("page_principale", u"Prolonger date emprunt:", None))
        self.gestionDocumentLabel.setTabText(self.gestionDocumentLabel.indexOf(self.GestionEmpruntsMenu), QCoreApplication.translate("page_principale", u"Gestion des emprunts", None))

    def afficher_fenetre_ajouter_adherent(self):
        self.setEnabled(False)
        self.fenetre = QDialog()
        self.ui = FenetreAjouterAdherent(self)
        self.ui.setupUi(self.fenetre)
        self.fenetre.exec()
        self.setEnabled(True)
        self.activateWindow()

    def afficher_fenetre_Supprimer_adherent(self):
        self.setEnabled(False)
        self.fenetre = QDialog()
        self.ui = FenetreSupprimerAdherent()
        self.ui.setupUi(self.fenetre)
        self.fenetre.exec()
        self.setEnabled(True)
        self.activateWindow()

    def afficher_fenetre_Liste_adherent(self):
        self.setEnabled(False)
        self.fenetre = QDialog()
        self.ui = FenetreListeAdherants()
        self.ui.setupUi(self.fenetre)
        self.fenetre.exec()
        self.setEnabled(True)
        self.activateWindow()

    def afficher_fenetre_ajouter_document(self):
        self.setEnabled(False)
        self.fenetre = QDialog()
        self.ui = FenetreAjouterDocument(self)
        self.ui.setupUi(self.fenetre)
        self.fenetre.exec()
        self.setEnabled(True)
        self.activateWindow()

    def afficher_fenetre_supprimer_document(self):
        self.setEnabled(False)
        self.fenetre = QDialog()
        self.ui = FenetreSupprimerDocument(self)
        self.ui.setupUi(self.fenetre)
        self.fenetre.exec()
        self.setEnabled(True)
        self.activateWindow()

    def afficher_fenetre_liste_document(self):
        self.setEnabled(False)
        self.fenetre = QDialog()
        self.ui = FenetreAfficherListeDocument(self)
        self.ui.setupUi(self.fenetre)
        self.fenetre.exec()
        self.setEnabled(True)
        self.activateWindow()

    def afficher_fenetre_ajouter_emprunt(self):
        self.setEnabled(False)
        self.fenetre = QDialog()
        self.ui = FenetreAjouterEmprunt()
        self.ui.setupUi(self.fenetre)
        self.fenetre.exec()
        self.setEnabled(True)
        self.activateWindow()

    def afficher_fenetre_Supprimer_emprunt(self):
        self.setEnabled(False)
        self.fenetre = QDialog()
        self.ui = FenetreSupprimerEmprunt()
        self.ui.setupUi(self.fenetre)
        self.fenetre.exec()
        self.setEnabled(True)
        self.activateWindow()

    def afficher_fenetre_Prolonger_date_retour(self):
        self.setEnabled(False)
        self.fenetre = QDialog()
        self.ui = FenetreProlongerDateRetour()
        self.ui.setupUi(self.fenetre)
        self.fenetre.exec()
        self.setEnabled(True)
        self.activateWindow()

    def afficher_fenetre_Liste_emprunt(self):
        self.setEnabled(False)
        self.fenetre = QDialog()
        self.ui = FenetreListeEmprunt()
        self.ui.setupUi(self.fenetre)
        self.fenetre.exec()
        self.setEnabled(True)
        self.activateWindow()

    def enregistrer_modifications_affichage(self, page_principale):
        self.groupBox_enregistrer = QGroupBox(page_principale)
        self.groupBox_enregistrer.setTitle("Enregistrer les modifications")
        self.groupBox_enregistrer.setObjectName(u"groupBox_enregistrer")
        self.groupBox_enregistrer.setGeometry(QRect(59, 65, 401, 100))
        self.groupBox_enregistrer.setFont(self.font3)

        self.EnregistrerModificationLbl = QLabel(self.groupBox_enregistrer)
        self.EnregistrerModificationLbl.setObjectName(u"enregistrerBtnLbl")
        self.EnregistrerModificationLbl.setGeometry(QRect(12, 40, 212, 21))
        self.EnregistrerModificationLbl.setFont(self.font)
        self.EnregistrerModificationLbl.setText("Enregistrer les modifications:")

        self.EnregistrerModificationBtn = QPushButton(self.groupBox_enregistrer)
        self.EnregistrerModificationBtn .setObjectName(u"enregistrerBtn")
        self.EnregistrerModificationBtn .setGeometry(QRect(260, 40, 41, 31))
        self.EnregistrerModificationBtn .clicked.connect(self.enregistrer_modifications)
        self.EnregistrerModificationBtn .setFont(self.font2)
        self.EnregistrerModificationBtn .setIcon(self.icon4)

    def enregistrer_modifications(self):
        Bib().enregistrer_modification_document()
        Bib().enregistrer_modification_adherant()
        Bib().enregistrer_modification_emprunt()






