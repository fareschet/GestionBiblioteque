# -*- coding: utf-8 -*-
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtWidgets import QTableWidgetItem
import os
import Modele.Adherent as Adh
import Modele.Document as Doc
from datetime import datetime
import Modele.Emprunte as Emp
import Modele.gestionBibliotheque as gest

class Bibliotheque:
    if gest.recuperer_liste_adherents() != None:
        __liste_Adherents = gest.recuperer_liste_adherents()
    else:
        __liste_Adherents = []

    if gest.recuperer_liste_documents() != None:
        __documents = gest.recuperer_liste_documents()
        __liste_journal = __documents["Journal"]
        __liste_dictionnaire = __documents["Dictionnaire"]
        __liste_livres = __documents["Livre"]
        __liste_bondeDessinee = __documents["Bande dessinee"]
    else:
        __liste_journal = []
        __liste_dictionnaire = []
        __liste_livres = []
        __liste_bondeDessinee = []

    if gest.recuperer_liste_emprunt() != None:
        __listeEmprunt = gest.recuperer_liste_emprunt()
    else:
        __listeEmprunt = []

    def get_liste_adherants(self):
        return self.__liste_Adherents

    def get_liste_livres(self):
        return self.__liste_livres

    def get_liste_emprunts(self):
        return self.__listeEmprunt

    def ajouterAdherant(self, Ajouter_Adherent, Ajouter_Adherent_nom, Ajouter_Adherent_prenom):
        self.nom = Ajouter_Adherent_nom
        self.prenom = Ajouter_Adherent_prenom
        self.numero = gest.generer_numero_aderent()

        if self.nom.isalpha() and self.prenom.isalpha():


            self.adherant = Adh.Adherent(self.numero, self.nom, self.prenom)
            Bibliotheque.__liste_Adherents.append(self.adherant)
            Ajouter_Adherent.numAdherentLbl.setVisible(True)
            self.numAdherent = "Numéro: <b>" + self.numero + "</b>"
            self.nomAdherent = "Nom: <b>" + self.nom + "</b>"
            self.prenomAdherent = "Prénom: <b>" + self.prenom + "</b>"
            Ajouter_Adherent.numAdherentLbl.setVisible(True)
            Ajouter_Adherent.numAdherentLbl.setText(self.numAdherent)
            Ajouter_Adherent.nomAdherentLbl.setText(self.nomAdherent)
            Ajouter_Adherent.prenomAdherentLbl.setText(self.prenomAdherent)
            Ajouter_Adherent.msgAdherentLbl.setVisible(True)
            Ajouter_Adherent.msgAdherentLbl.setText("l'adhérent a bien été enregistré!")
            Ajouter_Adherent.msgAdherentLbl.setStyleSheet("color: green;")
            Ajouter_Adherent.nomAdherentLine.setVisible(False)
            Ajouter_Adherent.prenomAdherentLine.setVisible(False)
            Ajouter_Adherent.ajouterAdherentBtn.setVisible(False)
            Ajouter_Adherent.nomAdherentLbl.setGeometry(QRect(50, 90, 250, 25))
            Ajouter_Adherent.prenomAdherentLbl.setGeometry(QRect(50, 130, 250, 25))
            Ajouter_Adherent.numAdherentLbl.setGeometry(QRect(50, 170, 250, 25))
        else:
            Ajouter_Adherent.msgAdherentLbl.setVisible(True)
            Ajouter_Adherent.msgAdherentLbl.setText("Format de saisie incorrect!")
            Ajouter_Adherent.msgAdherentLbl.setStyleSheet("color: red;")

    def supprimerAdherant(self, Supprimer_Adherent, Supprimer_Adherent_prenom):
        adherent_trouve = False
        for adherent in self.__liste_Adherents:
            if adherent.get_numero_adherent() == Supprimer_Adherent_prenom:
                self.__liste_Adherents.remove(adherent)
                adherent_trouve = True
        if not adherent_trouve:
            Supprimer_Adherent.messageSuppressionAdherentLbl.setText("L'adhérent est indisponible!")
            Supprimer_Adherent.messageSuppressionAdherentLbl.setStyleSheet("color: red;")
        else:
            Supprimer_Adherent.messageSuppressionAdherentLbl.setText("L'adhérent a bien été supprimé!")
            Supprimer_Adherent.messageSuppressionAdherentLbl.setStyleSheet("color: green;")

    def afficher_liste_adherent(self, tableListeAdherent):
        tableListeAdherent.setRowCount(len(self.__liste_Adherents))
        if len(self.__liste_Adherents) > 0:
            row = 0
            for adherent in self.__liste_Adherents:
                tableListeAdherent.setItem(row, 0, QTableWidgetItem(adherent.get_numero_adherent()))
                tableListeAdherent.item(row, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                tableListeAdherent.setItem(row, 1, QTableWidgetItem(adherent.get_nom_adherent()))
                tableListeAdherent.item(row, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                tableListeAdherent.setItem(row, 2, QTableWidgetItem(adherent.get_prenom_adherent()))
                tableListeAdherent.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                row += 1

    def ajouter_document(self, ajouter_document, contenu1, contenu2, contenu3, choix):
        if choix == "Journal":
            ISBN = gest.generer_isbn()
            titre = contenu1
            document = Doc.Document(ISBN, titre)
            date = contenu2
            journal = Doc.Journal(document, date)
            self.__liste_journal.append(journal)
            ajouter_document.reinitialiser_data()
            ajouter_document.ajouter_document_titre_lbl.setText("ISBN: <b>" + ISBN + "</b>")
            ajouter_document.ajouter_document_2_lbl.setText("Titre: <b>" + titre + "</b>")
            ajouter_document.ajouter_document_3_lbl.setText("Date édition: <b>" + date + "</b>")
            ajouter_document.ajouter_document_5_lbl.setText("Le journal a bien été ajouté!")
            ajouter_document.ajouter_document_5_lbl.setStyleSheet("color: green;")
            ajouter_document.cacher_option_ajout_document_droit()

        elif choix == "Livre":
            ISBN = gest.generer_isbn()
            titre = contenu1
            document = Doc.Document(ISBN, titre)
            auteur = contenu2
            volume = Doc.Volume(document, auteur)
            livre = Doc.Livre(volume, "True")
            self.__liste_livres.append(livre)
            ajouter_document.reinitialiser_data()
            ajouter_document.ajouter_document_titre_lbl.setText("ISBN: <b>" + ISBN + "</b>")
            ajouter_document.ajouter_document_2_lbl.setText("Titre: <b>" + titre + "</b>")
            ajouter_document.ajouter_document_3_lbl.setText("Auteur: <b>" + auteur + "</b>")
            ajouter_document.ajouter_document_5_lbl.setText("Le livre a bien été ajouté!")
            ajouter_document.ajouter_document_5_lbl.setStyleSheet("color: green;")
            ajouter_document.cacher_option_ajout_document_droit()

        elif choix == "Dictionnaire":
            ISBN = gest.generer_isbn()
            titre = contenu1
            document = Doc.Document(ISBN, titre)
            auteur = contenu2
            volume = Doc.Volume(document, auteur)
            dictionnaire = Doc.Dictionnaire(volume)
            self.__liste_dictionnaire.append(dictionnaire)
            ajouter_document.reinitialiser_data()
            ajouter_document.ajouter_document_titre_lbl.setText("ISBN: <b>" + ISBN + "</b>")
            ajouter_document.ajouter_document_2_lbl.setText("Titre: <b>" + titre + "</b>")
            ajouter_document.ajouter_document_3_lbl.setText("Auteur: <b>" + auteur + "</b>")
            ajouter_document.ajouter_document_5_lbl.setText("Le dictionnaire a bien été ajouté!")
            ajouter_document.ajouter_document_5_lbl.setStyleSheet("color: green;")
            ajouter_document.cacher_option_ajout_document_droit()

        elif choix == "Bande dessinee":
            ISBN = gest.generer_isbn()
            titre = contenu1
            document = Doc.Document(ISBN, titre)
            auteur = contenu2
            volume = Doc.Volume(document, auteur)
            dessinateur = contenu3
            bd = Doc.BD(volume, dessinateur)
            self.__liste_bondeDessinee.append(bd)
            ajouter_document.reinitialiser_data()
            ajouter_document.reinitialiser_data()
            ajouter_document.ajouter_document_titre_lbl.setText("ISBN: <b>" + ISBN + "</b>")
            ajouter_document.ajouter_document_2_lbl.setText("Titre: <b>" + titre + "</b>")
            ajouter_document.ajouter_document_3_lbl.setText("Auteur: <b>" + auteur + "</b>")
            ajouter_document.ajouter_document_5_lbl.setText("Dessinateur: <b>" + dessinateur + "</b>")

            ajouter_document.ajouter_document_4_lbl.setVisible(True)
            ajouter_document.ajouter_document_4_lbl.setText("La bande dessinée a bien été ajoutée!")
            ajouter_document.ajouter_document_4_lbl.setStyleSheet("color: green;")
            ajouter_document.cacher_option_ajout_document_droit()

    def supprimer_document(self, Supprimer_Document, numero):
        document_trouve = False
        for document_liste in [self.__liste_journal, self.__liste_livres, self.__liste_dictionnaire, self.__liste_bondeDessinee]:
            for document in document_liste:
                if document.get_ISBN() == numero:
                    document_liste.remove(document)
                    document_trouve = True
        if not document_trouve:
            Supprimer_Document.messageSuppressionDocumentLbl.setText("Le document est indisponible!")
            Supprimer_Document.messageSuppressionDocumentLbl.setStyleSheet("color: red;")
        else:
            Supprimer_Document.messageSuppressionDocumentLbl.setText("Le document a bien été supprimé!")
            Supprimer_Document.messageSuppressionDocumentLbl.setStyleSheet("color: green;")


    def set_disponibilite_livre(self, ISBN, etat):
        for objet in self.__liste_livres:
            if objet.get_ISBN() == ISBN:
                objet.set_disponibilite(etat)

    def afficher_liste_document(self, ListeDocument, ListeDocumentTable, choix):
        if choix == "Journal":
            ListeDocumentTable.setRowCount(len(self.__liste_journal))
            if len(self.__liste_Adherents) > 0:
                row = 0
                for document in self.__liste_journal:
                    ListeDocumentTable.setItem(row, 0, QTableWidgetItem(document.get_ISBN()))
                    ListeDocumentTable.item(row, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    ListeDocumentTable.setItem(row, 1, QTableWidgetItem(document.get_titre()))
                    ListeDocumentTable.item(row, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    ListeDocumentTable.setItem(row, 2, QTableWidgetItem(document.get_date()))
                    ListeDocumentTable.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    row += 1

        if choix == "Livre":
            ListeDocumentTable.setRowCount(len(self.__liste_livres))
            if len(self.__liste_livres) > 0:
                if ListeDocument.ListeDocumentcheckBox.isChecked():
                    ListeDocument.ListeDocumenttableWidget.clearContents()
                    row = 0
                    for document in self.__liste_livres:
                        if document.get_empruntable() == "True":
                            ListeDocumentTable.setItem(row, 0, QTableWidgetItem(document.get_ISBN()))
                            ListeDocumentTable.item(row, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            ListeDocumentTable.setItem(row, 1, QTableWidgetItem(document.get_titre()))
                            ListeDocumentTable.item(row, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            ListeDocumentTable.setItem(row, 2, QTableWidgetItem(document.get_auteur()))
                            ListeDocumentTable.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            ListeDocumentTable.setItem(row, 3, QTableWidgetItem("Oui"))
                            ListeDocumentTable.item(row, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            row += 1

                elif ListeDocument.ListeDocumentcheckBox_2.isChecked():
                    ListeDocument.ListeDocumenttableWidget.clearContents()
                    row = 0
                    for document in self.__liste_livres:
                        if document.get_empruntable() != "True":
                            ListeDocumentTable.setItem(row, 0, QTableWidgetItem(document.get_ISBN()))
                            ListeDocumentTable.item(row, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            ListeDocumentTable.setItem(row, 1, QTableWidgetItem(document.get_titre()))
                            ListeDocumentTable.item(row, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            ListeDocumentTable.setItem(row, 2, QTableWidgetItem(document.get_auteur()))
                            ListeDocumentTable.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            ListeDocumentTable.setItem(row, 3, QTableWidgetItem("Non"))
                            ListeDocumentTable.item(row, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            row += 1
                else:
                    ListeDocument.ListeDocumenttableWidget.clearContents()
                    row = 0
                    for document in self.__liste_livres:
                        ListeDocumentTable.setItem(row, 0, QTableWidgetItem(document.get_ISBN()))
                        ListeDocumentTable.item(row, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        ListeDocumentTable.setItem(row, 1, QTableWidgetItem(document.get_titre()))
                        ListeDocumentTable.item(row, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        ListeDocumentTable.setItem(row, 2, QTableWidgetItem(document.get_auteur()))
                        ListeDocumentTable.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        if document.get_empruntable() == "True":
                            ListeDocumentTable.setItem(row, 3, QTableWidgetItem("Oui"))
                        else:
                            ListeDocumentTable.setItem(row, 3, QTableWidgetItem("Non"))
                        ListeDocumentTable.item(row, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        row += 1

        if choix == "Dictionnaire":
            ListeDocumentTable.setRowCount(len(self.__liste_dictionnaire))
            if len(self.__liste_dictionnaire) > 0:
                row = 0
                for document in self.__liste_dictionnaire:
                    ListeDocumentTable.setItem(row, 0, QTableWidgetItem(document.get_ISBN()))
                    ListeDocumentTable.item(row, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    ListeDocumentTable.setItem(row, 1, QTableWidgetItem(document.get_titre()))
                    ListeDocumentTable.item(row, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    ListeDocumentTable.setItem(row, 2, QTableWidgetItem(document.get_auteur()))
                    ListeDocumentTable.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    row += 1

        if choix == "Bande dessinee":
            ListeDocumentTable.setRowCount(len(self.__liste_bondeDessinee))
            if len(self.__liste_bondeDessinee) > 0:
                row = 0
                for document in self.__liste_bondeDessinee:
                    ListeDocumentTable.setItem(row, 0, QTableWidgetItem(document.get_ISBN()))
                    ListeDocumentTable.item(row, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    ListeDocumentTable.setItem(row, 1, QTableWidgetItem(document.get_titre()))
                    ListeDocumentTable.item(row, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    ListeDocumentTable.setItem(row, 2, QTableWidgetItem(document.get_auteur()))
                    ListeDocumentTable.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    ListeDocumentTable.setItem(row, 3, QTableWidgetItem(document.get_dessinateur()))
                    ListeDocumentTable.item(row, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    row += 1

    def ajouter_emprunt(self, ajout_emprunt, numero_adherant, ISBN, date_retour):
        adherant_trouve = "non"
        livre_trouve = "non"
        date_verifie = True
        dateEmprunt = gest.recuperer_date_aujourdhui()

        for objet in self.__liste_Adherents:
            if objet.get_numero_adherent() == numero_adherant:
                adherant_trouve = "oui"
        if adherant_trouve == "non":
            ajout_emprunt.msgEmpruntLbl.setVisible(True)
            ajout_emprunt.msgEmpruntLbl.setText("L'adhérent est indisponible!")
            ajout_emprunt.msgEmpruntLbl.setStyleSheet("color: red;")

        if adherant_trouve == "oui":
            for objet in self.__liste_livres:
                if objet.get_ISBN() == ISBN:
                    if objet.get_empruntable() == "True":
                        livre_trouve = "oui"
            if livre_trouve == "non":
                ajout_emprunt.msgEmpruntLbl.setVisible(True)
                ajout_emprunt.msgEmpruntLbl.setText("Le livre est indisponible!")
                ajout_emprunt.msgEmpruntLbl.setStyleSheet("color: red;")
        if livre_trouve == "oui":
            try:
                datetime.strptime(date_retour, "%Y-%m-%d")
                if date_retour <= dateEmprunt:
                    ajout_emprunt.msgEmpruntLbl.setText("La date est incorrecte!")
                    ajout_emprunt.msgEmpruntLbl.setStyleSheet("color: red;")
                    date_verifie = False
            except ValueError:
                ajout_emprunt.msgEmpruntLbl.setText("La date est incorrecte!")
                ajout_emprunt.msgEmpruntLbl.setStyleSheet("color: red;")
                date_verifie = False

        if adherant_trouve == "oui" and livre_trouve == "oui" and date_verifie:
            emprunt = Emp.Emprunte(numero_adherant, ISBN, dateEmprunt, date_retour)
            self.set_disponibilite_livre(ISBN, "False")
            self.__listeEmprunt.append(emprunt)
            ajout_emprunt.msgEmpruntLbl.setText("L'emprunt est bien été ajouté!")
            ajout_emprunt.msgEmpruntLbl.setStyleSheet("color: green;")

    def prolonger_date_retour_livre(self, prolonger_date, ISBN, nbr_jour):
        prolonger_date.messageProlongerDateRetourLbl.setVisible(True)
        ISBN_trouve = "non"
        for objet in self.__listeEmprunt:
            if objet.get_ISBN_livre() == ISBN:
                objet.prolongerDateRetour(nbr_jour)
                ISBN_trouve = "oui"
        if ISBN_trouve == "oui":
            prolonger_date.messageProlongerDateRetourLbl.setText("Changement effectué!")
            prolonger_date.messageProlongerDateRetourLbl.setStyleSheet("color: green;")
        else:
            prolonger_date.messageProlongerDateRetourLbl.setText("Emprunt indisponible!")
            prolonger_date.messageProlongerDateRetourLbl.setStyleSheet("color: red;")

    def supprimer_emprunt(self, supprimer_emprunt, ISBN):
        emprunt_trouve = False
        for emprunt in self.__listeEmprunt:
            if emprunt.get_ISBN_livre() == ISBN:
                self.__listeEmprunt.remove(emprunt)
                emprunt_trouve = True
        if not emprunt_trouve:
            supprimer_emprunt.messageSuppressionEmpruntLbl.setText("L'emprunt est indisponible!")
            supprimer_emprunt.messageSuppressionEmpruntLbl.setStyleSheet("color: red;")
        else:
            self.set_disponibilite_livre(ISBN, "True")
            supprimer_emprunt.messageSuppressionEmpruntLbl.setText("L'emprunt a bien été supprimé!")
            supprimer_emprunt.messageSuppressionEmpruntLbl.setStyleSheet("color: green;")

    def afficher_liste_emprunt(self, tableListeEmprunt):
        tableListeEmprunt.setRowCount(len(self.__listeEmprunt))
        if len(self.__listeEmprunt) > 0:
            row = 0
            for emprunt in self.__listeEmprunt:
                for adherent in self.__liste_Adherents:
                    if emprunt.get_numero_adherant() == adherent.get_numero_adherent():
                        numAdh = adherent.get_numero_adherent()
                        nomAdh = adherent.get_nom_adherent()
                        prenomAdh = adherent.get_prenom_adherent()
                        tableListeEmprunt.setItem(row, 0, QTableWidgetItem(numAdh))
                        tableListeEmprunt.item(row, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        tableListeEmprunt.setItem(row, 1, QTableWidgetItem(nomAdh))
                        tableListeEmprunt.item(row, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        tableListeEmprunt.setItem(row, 2, QTableWidgetItem(prenomAdh))
                        tableListeEmprunt.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                for livre in self.__liste_livres:
                    if emprunt.get_ISBN_livre() == livre.get_ISBN():
                        ISBN= livre.get_ISBN()
                        titre = livre.get_titre()
                        dateEmprunt = emprunt.get_dateEmprunt()
                        dateRetour = emprunt.get_dateRetour()
                        tableListeEmprunt.setItem(row, 3, QTableWidgetItem(ISBN))
                        tableListeEmprunt.item(row, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        tableListeEmprunt.setItem(row, 4, QTableWidgetItem(titre))
                        tableListeEmprunt.item(row, 4).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        tableListeEmprunt.setItem(row, 5, QTableWidgetItem(dateEmprunt))
                        tableListeEmprunt.item(row, 5).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        tableListeEmprunt.setItem(row, 6, QTableWidgetItem(dateRetour))
                        tableListeEmprunt.item(row, 6).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                row += 1

    def enregistrer_modification_document(self):
        try:
            with open(os.getcwd() + "/Modele/sauvegardeDonnees/documents.txt", "w") as fichier:
                if len(self.__liste_journal) > 0:
                    for objet in self.__liste_journal:
                        contenu = objet.get_ISBN() + ";" + objet.get_type() + ";" + objet.get_titre() + ";" + objet.get_date()
                        fichier.write(contenu)
                        fichier.write("\n")

                if len(self.__liste_dictionnaire) > 0:
                    for objet in self.__liste_dictionnaire:
                        contenu = objet.get_ISBN() + ";" + objet.get_type() + ";" + objet.get_titre() + ";" + objet.get_auteur()
                        fichier.write(contenu)
                        fichier.write("\n")

                if len(self.__liste_livres) > 0:
                    for objet in self.__liste_livres:
                        contenu = objet.get_ISBN() + ";" + objet.get_type() + ";" + objet.get_titre() + ";" + objet.get_auteur() + ";" + str(
                            objet.get_empruntable())
                        fichier.write(contenu)
                        fichier.write("\n")

                if len(self.__liste_bondeDessinee) > 0:
                    for objet in self.__liste_bondeDessinee:
                        contenu = objet.get_ISBN() + ";" + objet.get_type() + ";" + objet.get_titre() + ";" + objet.get_auteur() + ";" + objet.get_dessinateur()
                        fichier.write(contenu)
                        fichier.write("\n")
        except IOError as e:
            print("Erreur lors de l'écriture dans le fichier :", e)
        gest.afficher_menu_principale()

    def enregistrer_modification_adherant(self):
        try:
            with open(os.getcwd() + "/Modele/sauvegardeDonnees/adherents.txt", "w") as fichier:
                if len(self.__liste_Adherents) > 0:
                    for objet in self.__liste_Adherents:
                        contenu = objet.get_numero_adherent() + ";" + objet.get_nom_adherent() + ";" + objet.get_prenom_adherent()
                        fichier.write(contenu)
                        fichier.write("\n")
        except IOError as e:
            print("Erreur lors de l'écriture dans le fichier :", e)
        gest.afficher_menu_principale()

    def enregistrer_modification_emprunt(self):
        try:
            with open(os.getcwd() + "/Modele/sauvegardeDonnees/emprunts.txt", "w") as fichier:
                if len(self.__listeEmprunt) > 0:
                    for objet in self.__listeEmprunt:
                        contenu = objet.get_numero_adherant() + ";" + objet.get_ISBN_livre() + ";" + objet.get_dateEmprunt() + ";" + objet.get_dateRetour()
                        fichier.write(contenu)
                        fichier.write("\n")
        except IOError as e:
            print("Erreur lors de l'écriture dans le fichier :", e)
        gest.afficher_menu_principale()
