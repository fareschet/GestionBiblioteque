# -*- coding: utf-8 -*-
import Graphique.MainApplication as MainApp
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow)
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = MainApp.PagePrincipale()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
