import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtCore import QRunnable, Qt, QThreadPool
from PySide2.QtWidgets import QMessageBox

import logging
import random
import time
import serial
from serial.tools import list_ports

# help(serial)


logging.basicConfig(format="%(message)s", level=logging.INFO)

# GUI FILE
from ui_PEM_new_gui import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

global window
global temp_chamber
global temp_cryo
global humid
global STATUS
global ERROR_MSG
global update_preheat_variables_bool, update_blot_variables_bool, shutdown
global set_temp_cryo, set_temp_chamber, set_humid, set_blot_force, set_blot_time, set_blot_nr
global calib_offset_right, calib_offset_left, update_calibration
global calib_successful

temp_chamber, temp_cryo, humid = 0, 0, 0

set_blot_force, set_blot_time, set_blot_nr = 0, 0, 0

update_preheat_variables_bool, update_blot_variables_bool, shutdown, update_calibration, calib_successful = False, False, False, False, False

set_temp_chamber = 0
set_temp_cryo = 0
set_humid = 0

calib_offset_right, calib_offset_left = 0,0

STATUS = 'IDLE'
ERROR_MSG = ''


class SerialCommunicator(QRunnable):
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial()  # open serial port>>> ser = serial.Serial()
        # sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
        self.ser.baudrate = 9600
        self.ser.port = 'COM7'
        self.ser.open()
        self.send_message = False
        self.message = ''
        self.received = ''
        print(self.ser)
        # received

    def run(self):
        global temp_chamber, STATUS, ERROR_MSG, humid, temp_cryo, update_preheat_variables_bool,\
            set_temp_cryo, set_temp_chamber, set_humid, update_blot_variables_bool, set_blot_force,\
            set_blot_time, set_blot_nr, shutdown, calib_offset_left, calib_offset_right, update_calibration,\
            calib_successful


        print(calib_offset_left,calib_offset_right)
        while True:
            #print("1")

            # check which port was really used
            # ser.write(b'b\n')     # write a string
            # time.sleep(1)
            while self.ser.in_waiting:
                msg = self.ser.readline()
                print(msg)
                msg = msg.decode("utf-8")
                msg = msg[0:len(msg) - 2]
                msg_split = msg.split("/")

                if msg_split[0] == 'D':
                    self.received = msg
                    STATUS, temp_chamber, temp_cryo, humid = msg_split[1], int(msg_split[2]), int(msg_split[3]), int(
                        msg_split[4])
                    # print(STATUS, temp_chamber, temp_cryo, humid)
                    # print(self.received)
                elif msg_split[0] == 'F' and STATUS != "ERROR":
                    STATUS = "ERROR"
                    ERROR_MSG = msg_split[1]
                    #window.warning()
                elif msg_split[0] == 'I':
                    STATUS = msg_split[1]
                elif msg_split[0] == 'C':
                    if msg_split[1] == 'S': calib_successful = True
                    elif msg_split[1] == 'F': calib_successful = False


            if update_preheat_variables_bool:
                STATUS = "PREHEATING"
                s = 'P/' + str(set_temp_chamber) + "/" + str(set_temp_cryo) + "/" + str(set_humid) + "/"
                s_binary = bytes(s, 'utf-8')
                print("Preheat", set_temp_chamber, set_temp_cryo, set_humid)
                self.ser.write(s_binary)
                update_preheat_variables_bool = False
            elif update_blot_variables_bool:
                STATUS = "BLOTTING"
                s = 'B/' + str(set_blot_force) + "/" + str(set_blot_time) + "/" + str(set_blot_nr) + "/"
                s_binary = bytes(s, 'utf-8')
                self.ser.write(s_binary)
                print("BLOT", set_blot_force, set_blot_time, set_blot_nr)
                update_blot_variables_bool = False
            elif shutdown:
                STATUS = "SHUTDOWN"
                s = 'X/'
                s_binary = bytes(s, 'utf-8')
                self.ser.write(s_binary)
                print("SHUTDOWN")
                shutdown = False
            elif update_calibration:
                STATUS = "CALIBRATING"
                s = 'C/' + str(calib_offset_left) + "/" + str(calib_offset_right) + "/"
                s_binary = bytes(s, 'utf-8')
                self.ser.write(s_binary)
                print("CALIBRATING", calib_offset_left, calib_offset_right)
                update_calibration = False


class LableUpdater(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.temp_chamber = 0
        self.temp_cryo = 0
        self.humid = 0

    def run(self):
        logging.info(f"LableUpdater{self.n}")
        for i in range(1, 1000):
            time.sleep(1)
            # self.temp_chamber,self.temp_cryo, self.humid = i,2*i,3*i


class MainWindow(QMainWindow):

    def warning(self, message="Default"):
        QMessageBox.about(self, "Error", message)

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

        ## Functions
        ###################################################################
        self.ui.prep_button.clicked.connect(lambda: UIFunctions.update_preheat_variables(self))
        self.ui.start_button_4.clicked.connect(lambda: UIFunctions.update_blot_variables(self))
        self.ui.shutdown_button_4.clicked.connect(lambda: UIFunctions.shutdown(self))
        self.ui.calib_save_button.clicked.connect(lambda: UIFunctions.calibrate_blot_arms(self))
        #self.warning()

        # self.ui.shutdown_button_4.clicked.connect(lambda: UIFunctions.update_labels(self,1,2,3))
        # self.ui.shutdown_button_4.clicked.connect(lambda: print(lable_updater.humid, lable_updater.temp_cryo, lable_updater.temp_chamber))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


class UIFunctions(QMainWindow):

    def update_labels(self, temp_chamber, temp_cryo, humid, status):
        global calib_successful
        self.ui.temp_lable_2.setText(str(temp_chamber) + "°C")
        self.ui.temp_lable_bottom_4.setText(str(temp_cryo) + "°C")
        self.ui.current_step_label.setText(str(status))
        if calib_successful:
            self.ui.calib_sucess_label.setText("Successful")
            self.ui.calib_sucess_label.setStyleSheet(u"color: rgb(0, 170, 0);")
        else:
            self.ui.calib_sucess_label.setText("Failure")
            self.ui.calib_sucess_label.setStyleSheet(u"color: rgb(170, 0, 0);")
        if status == "IDLE":
            self.ui.progressBar.setValue(0)
        elif status == "PREHEATING":
            self.ui.progressBar.setValue(25)
        elif status == "BLOTTING":
            self.ui.progressBar.setValue(50)
        elif status == "SHUTDOWN":
            self.ui.progressBar.setValue(0)
        if humid >= 0 and humid <= 100:
            self.ui.humid_lable_2.setText(str(humid) + "%")
        else:
            self.ui.humid_lable_2.setText("Error in sensor reading")

    def update_preheat_variables(self):
        global set_temp_chamber, set_temp_cryo, set_humid, update_preheat_variables_bool
        set_temp_chamber = self.ui.temp_control_2.value()
        set_temp_cryo = self.ui.temp_control_botttom_4.value()
        set_humid = self.ui.humid_control_2.value()
        update_preheat_variables_bool = True

    def update_blot_variables(self):
        global set_blot_nr, set_blot_time, set_blot_force, update_blot_variables_bool
        set_blot_force = self.ui.blotting_force_control_2.value()
        set_blot_time = self.ui.blotting_time_control_2.value()
        set_blot_nr = self.ui.blotting_number_control_2.value()
        update_blot_variables_bool = True

    def calibrate_blot_arms(self):
        global calib_offset_right, calib_offset_left, update_calibration
        calib_offset_right = self.ui.calib_right.value()
        calib_offset_left = self.ui.calib_left.value()
        update_calibration = True

    def shutdown(self):
        global shutdown
        shutdown = True

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
                self.ui.button_page_home.setText('          Home')
                self.ui.button_page_plots.setText('          Plots')
                self.ui.button_page_Data.setText('          Data')
            else:
                widthExtended = standard
                self.ui.button_page_home.setText('    ')
                self.ui.button_page_plots.setText('    ')
                self.ui.button_page_Data.setText('    ')

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    #######################################THREADS#########################################
    pool = QThreadPool.globalInstance()  # Thread to update lables in background
    serial_communicator = SerialCommunicator()
    pool.start(serial_communicator)
    lable_updater = LableUpdater(1)
    # pool.start(lable_updater)
    # lable_updater.temp_chamber = serial_communicator.received
    # print(serial_communicator.received)
    ###############################################################
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: UIFunctions.update_labels(window, temp_chamber, temp_cryo, humid, STATUS))
    timer.start(100)  # every 100 milliseconds
    #############################################################################

    sys.exit(app.exec_())
