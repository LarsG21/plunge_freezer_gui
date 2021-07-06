################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_PEM_new_gui import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(open('Combinear/Combinear.qss').read())

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.toggle_button.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.button_page_home.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_home))

        # PAGE 2
        self.ui.button_page_plots.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_plots))

        # PAGE 3
        self.ui.button_page_Data.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_dataExport))

        # PAGE Settings
        self.ui.go_settings_button.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_settings))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
