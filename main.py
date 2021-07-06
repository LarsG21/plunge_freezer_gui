

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtCore import QRunnable, Qt, QThreadPool
import logging
import random
import time
import serial

#help(serial)

ser = serial.Serial()  # open serial port>>> ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM7'
ser.open()
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()

logging.basicConfig(format="%(message)s", level=logging.INFO)

# GUI FILE
from ui_PEM_new_gui import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *


class LableUpdater(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.temp_chamber = 0
        self.temp_cryo = 0
        self.humid = 0


    def run(self):
        logging.info(f"LableUpdater{self.n}")
        for i in range(1,1000):
            time.sleep(1)
            self.temp_chamber,self.temp_cryo, self.humid = i,2*i,3*i

            print(self.temp_chamber)

class MainWindow(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        ## Functions
        ###################################################################
        self.ui.start_button_4.clicked.connect(lambda: UIFunctions.send_start_command(self))

        #self.ui.shutdown_button_4.clicked.connect(lambda: UIFunctions.update_labels(self,1,2,3))
        #self.ui.shutdown_button_4.clicked.connect(lambda: print(lable_updater.humid, lable_updater.temp_cryo, lable_updater.temp_chamber))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    #######################################THREADS#########################################
    pool = QThreadPool.globalInstance()  # Thread to update lables in background
    lable_updater = LableUpdater(1)
    pool.start(lable_updater)
    ###############################################################
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: UIFunctions.update_labels(window, lable_updater.temp_chamber, lable_updater.temp_cryo, lable_updater.humid))
    timer.start(100)  # every 100 milliseconds

    sys.exit(app.exec_())
