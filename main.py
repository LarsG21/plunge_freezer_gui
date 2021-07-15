import math
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

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

import logging
import random
import time
import serial
from serial.tools import list_ports
import datetime

# help(serial)


log_file_name = "logfile" + str(datetime.datetime.now().strftime("%M%S")) + ".log"

#logging.basicConfig(filename=log_file_name,level=logging.INFO)



# GUI FILE
from ui_PEM_new_gui import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

global temp_chamber, temp_cryo, humid
global STATUS
global ERROR_MSG
global update_preheat_variables_bool, update_blot_variables_bool, shutdown
global set_temp_cryo, set_temp_chamber, set_humid, set_blot_force, set_blot_time, set_blot_nr
global calib_offset_right, calib_offset_left, update_calibration
global calib_successful
global waiting_for_serial
global cryo_pos, plunging_pos, update_manual_movement

update_manual_movement = False

cryo_pos, plunging_pos = 0,0

waiting_for_serial = True

temp_chamber, temp_cryo, humid = 0, 0, 0

set_blot_force, set_blot_time, set_blot_nr = 0, 0, 0
set_temp_chamber, set_temp_cryo, set_humid = 0, 0, 0

global x, y_chamber, y_cryo, y_humid

x = [1]
y_chamber = [0]
y_cryo = [0]
y_humid = [0]

hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]


update_preheat_variables_bool, update_blot_variables_bool, shutdown, update_calibration, calib_successful = False, False, False, False, False


calib_offset_right, calib_offset_left = 0,0

STATUS = 'IDLE'
ERROR_MSG = ''

serial_pid = 42021       #14155   # id of the serial device

class Counter(QRunnable):
    def __init__(self):
        super().__init__()

    def run(self):
        global x,y_chamber
        while True:
            x.append(x[-1] + 1)
            y_chamber.append(int(3 * math.sin(x[-1])))
            time.sleep(0.1)


class SerialCommunicator(QRunnable):
    def __init__(self):
        super().__init__()
        use_port = ""
        ports = serial.tools.list_ports.comports(include_links=False)
        if len(ports)!= 0:
            for p in ports:
                print(p.name, p.device, p.description, p.manufacturer, p.product, p.serial_number, p.pid, p.vid, p.interface, p.location)
                if p.pid == serial_pid:
                    use_port = p.name
        if not use_port == "":
            self.ser = serial.Serial()  # open serial port>>> ser = serial.Serial()
            # sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
            self.ser.baudrate = 9600
            self.ser.port = use_port
            self.ser.open()
            waiting_for_serial = False
            print(self.ser)

    def run(self):
        global temp_chamber, STATUS, ERROR_MSG, humid, temp_cryo, update_preheat_variables_bool,\
            set_temp_cryo, set_temp_chamber, set_humid, update_blot_variables_bool, set_blot_force,\
            set_blot_time, set_blot_nr, shutdown, calib_offset_left, calib_offset_right, update_calibration,\
            calib_successful, waiting_for_serial, x, y_chamber, y_cryo, y_humid, update_manual_movement

        while True:
            if waiting_for_serial == False:
                try:
                    while self.ser.in_waiting:
                        # Read in messages from serial
                        msg = self.ser.readline()

                        msg = msg.decode("utf-8")
                        msg = msg[0:len(msg) - 2]
                        print(msg)
                        msg_split = msg.split("/")
                        identifier = msg_split[0]
                        if identifier == 'D':
                            temp_chamber, temp_cryo, humid = float(msg_split[1]), float(msg_split[2]), float(msg_split[3])
                            x.append(x[-1] + 1)
                            y_chamber.append(temp_chamber)
                            y_cryo.append(temp_cryo)
                            y_humid.append(humid)
                        elif identifier == 'F' and STATUS != "ERROR":
                            STATUS = "ERROR"
                            ERROR_MSG = msg_split[1]
                            #window.warning()
                        elif identifier == 'I':
                            STATUS = msg_split[1]
                        elif identifier == 'C':
                            if msg_split[1] == 'S': calib_successful = True
                            elif msg_split[1] == 'F': calib_successful = False


                    # if one of the update flags is set --> Send update to UC and reset Flag
                    if update_preheat_variables_bool:
                        STATUS = "PREHEATING"
                        s = 'P/' + str(set_temp_chamber) + "/" + str(abs(set_temp_cryo)) + "/" + str(set_humid) + "/"
                        s_binary = bytes(s, 'utf-8')
                        print("Preheat", set_temp_chamber, set_temp_cryo, set_humid)
                        self.ser.write(s_binary)
                        update_preheat_variables_bool = False
                    elif update_blot_variables_bool:
                        STATUS = "BLOTTING"
                        s = 'S/' + str(set_blot_force) + "/" + str(set_blot_time) + "/" + str(set_blot_nr) + "/"
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
                    elif update_manual_movement:
                        STATUS = "MOVE"
                        s = 'M/' + str(plunging_pos*1250) + "/" + str(cryo_pos*1250) + "/"
                        s_binary = bytes(s, 'utf-8')
                        self.ser.write(s_binary)
                        print("MOVING", plunging_pos, cryo_pos)
                        update_manual_movement = False


                except serial.serialutil.SerialException as e:
                    print(e)
                    waiting_for_serial = True   #Set Flag and try to regain serial
                    STATUS = "Connection Lost!"
            else:   #Handle if Serial communication is lost
                while waiting_for_serial:
                    STATUS = "WAITING FOR SERIAL"
                    ports = serial.tools.list_ports.comports(include_links=False)
                    use_port = ""
                    if len(ports) != 0:
                        for p in ports:
                            if p.pid == serial_pid:
                                use_port = p.name
                    if use_port == "":
                        waiting_for_serial = True
                        pass
                    else:
                        time.sleep(4)
                        self.ser = serial.Serial()  # open serial port>>> ser = serial.Serial()
                        # sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
                        self.ser.baudrate = 9600
                        self.ser.port = use_port
                        self.ser.open()
                        waiting_for_serial = False
                        STATUS = "IDEL"
                        print("now connected with", self.ser.port)

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)   # Set up the external generated ui

        ########################ADD ADITIONAL FUNCTIONALITY LIKE PLOTTING######################
        self.ui.graphWidget = pg.PlotWidget(self.ui.plot1_label)
        self.ui.graphWidget.setMinimumSize(QSize(1000, 200))

        self.ui.graphWidget1 = pg.PlotWidget(self.ui.plot2_label)
        self.ui.graphWidget1.setMinimumSize(QSize(1000, 200))

        self.ui.graphWidget2 = pg.PlotWidget(self.ui.plot3_label)
        self.ui.graphWidget2.setMinimumSize(QSize(1000, 200))

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        #self.ui.graphWidget.plot(hour, temperature)
        ######################################################################################

        self.setStyleSheet(open('Combinear/Combinear.qss').read())  #Add an Stylesheet

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
        self.ui.cryo_slider.sliderReleased.connect(lambda: UIFunctions.update_manual_positioning(self))
        self.ui.plunging_slider.sliderReleased.connect(lambda: UIFunctions.update_manual_positioning(self))

        #self.warning()

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    def warning(self, message="Default"):
        QMessageBox.about(self, "Error", message)

class UIFunctions(QMainWindow):

    def update_labels(self, temp_chamber, temp_cryo, humid, status):
        """
        Updates the Labels in the GUI
        :param temp_chamber:
        :param temp_cryo:
        :param humid:
        :param status:
        :return:
        """
        global calib_successful, waiting_for_serial
        self.ui.temp_lable_2.setText(str(temp_chamber) + "°C")
        self.ui.temp_lable_bottom_4.setText(str(temp_cryo) + "°C")
        self.ui.current_step_label.setText(str(status))
        if waiting_for_serial:
            self.ui.connection_frame.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        else:
            self.ui.connection_frame.setStyleSheet(u"background-color: rgb(0, 170, 0);")
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
        """
        Updates the global variables and sets the update Flag
        :return:
        """
        global set_temp_chamber, set_temp_cryo, set_humid, update_preheat_variables_bool
        set_temp_chamber = self.ui.temp_control_2.value()
        set_temp_cryo = self.ui.temp_control_botttom_4.value()
        set_humid = self.ui.humid_control_2.value()
        update_preheat_variables_bool = True

    def update_manual_positioning(self):
        """
        Updates the global variables and sets the update Flag
        :return:
        """
        global cryo_pos, plunging_pos, update_manual_movement
        cryo_pos = self.ui.cryo_slider.value()
        plunging_pos = self.ui.plunging_slider.value()
        update_manual_movement = True


    def update_blot_variables(self):
        """
        Updates the global variables and sets the update Flag
        :return:
        """
        global set_blot_nr, set_blot_time, set_blot_force, update_blot_variables_bool
        set_blot_force = self.ui.blotting_force_control_2.value()
        set_blot_time = self.ui.blotting_time_control_2.value()
        set_blot_nr = self.ui.blotting_number_control_2.value()
        update_blot_variables_bool = True

    def calibrate_blot_arms(self):
        """
        Updates the global variables and sets the update Flag
        :return:
        """
        global calib_offset_right, calib_offset_left, update_calibration
        calib_offset_right = self.ui.calib_right.value()
        calib_offset_left = self.ui.calib_left.value()
        update_calibration = True

    def shutdown(self):
        """
        Sets the Shutdown Flag
        :return:
        """
        global shutdown
        shutdown = True

    def toggleMenu(self, maxWidth, enable):
        """
        Displays the toggle animation of the hamburger menu in the GUI
        :param maxWidth:
        :param enable:
        :return:
        """
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
    counter = Counter()
    #pool.start(counter)
    ###############################################################
    timer = QtCore.QTimer()
    timer2 = QtCore.QTimer()
    timer.timeout.connect(lambda: UIFunctions.update_labels(window, temp_chamber, temp_cryo, humid, STATUS))
    #timer2.timeout.connect(lambda: window.ui.graphWidget.plot(x, y_chamber))
    #timer2.timeout.connect(lambda: window.ui.graphWidget1.plot(x, y_cryo))
    #timer2.timeout.connect(lambda: window.ui.graphWidget2.plot(x, y_humid))
    timer2.start(10)
    timer.start(100)  # every 100 milliseconds
    #############################################################################

    sys.exit(app.exec_())
