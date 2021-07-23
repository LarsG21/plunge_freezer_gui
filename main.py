import csv
import math
import sys
import platform
import PySide2
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

import numpy as np
import logging
import random
import time
import serial
from serial.tools import list_ports
import datetime

from testing import DateAxisItem

log_file_name = "logfile" + str(datetime.datetime.now().strftime("%M%S")) + ".log"

# logging.basicConfig(filename=log_file_name,level=logging.INFO)


# GUI FILE
from ui_PEM_new_gui import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

########################################Variables##############################
# General
waiting_for_serial = True
shutdown = False
STATUS = 'IDLE'
STATUS_INTERNAL = 'IDLE'
ERROR_MSG = ''

serial_pid = 42021  # 14155    #42021          # id of the serial device

# Temp Humid
set_blot_force, set_blot_time, set_blot_nr = 0, 0, 0
set_temp_chamber, set_temp_cryo, set_humid = 0, 0, 0
temp_chamber, temp_cryo, humid = 0, 0, 0

# Manual Movement and Settings
calib_successful, homing_successful = False, True
calib_offset_right, calib_offset_left = 0, 0
cryo_pos, plunging_pos = 0, 0

# Plotting
x = [1]
y_chamber = [0.0]
y_cryo = [0.0]
y_humid = [0.0]
pid_ps, pid_ds = [0.0], [0.0]
time_plot = [datetime.datetime.now().strftime("%H:%M:%S")]

# Testing
hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]


#################################################################################


class Counter(QRunnable):
    def __init__(self):
        super().__init__()
        # self.start_time = time.time()
        # self.elapsed_time = 0

    def run(self):
        global x, y_chamber, time_plot
        while True:
            x.append(x[-1] + 1)
            # now = time.time()
            # x = np.linspace(self.start_time, now, self.elapsed_time)
            # self.elapsed_time += 1
            y_chamber.append(int(3 * math.sin(x[-1])))
            y_cryo.append(int(3 * math.cos(x[-1])))
            y_humid.append(int(3 * math.sin(x[-1])))
            time_plot.append(datetime.datetime.now().strftime("%H:%M:%S"))
            time.sleep(0.1)


def state_machine(calib_offset_left, calib_offset_right, s_binary, set_blot_force, set_blot_nr, set_blot_time,
                  set_humid, set_temp_chamber, set_temp_cryo):
    global STATUS, STATUS_INTERNAL
    if STATUS_INTERNAL == 'PREHEATING':
        STATUS = "PREHEATING"
        s = 'P/' + str(set_temp_chamber) + "/" + str(abs(set_temp_cryo)) + "/" + str(set_humid) + "/"
        s_binary = bytes(s, 'utf-8')
        print("Preheat", set_temp_chamber, set_temp_cryo, set_humid)
        STATUS_INTERNAL = 'IDLE'
    elif STATUS_INTERNAL == 'UPDATE_BLOT':
        STATUS = "BLOTTING"
        s = 'S/' + str(set_blot_force) + "/" + str(set_blot_time) + "/" + str(set_blot_nr) + "/"
        s_binary = bytes(s, 'utf-8')
        print("BLOT", set_blot_force, set_blot_time, set_blot_nr)
        STATUS_INTERNAL = 'IDLE'
    elif STATUS_INTERNAL == 'SHUTDOWN':
        STATUS = "SHUTDOWN"
        s = 'X/'
        s_binary = bytes(s, 'utf-8')
        print("SHUTDOWN")
        STATUS_INTERNAL = 'IDLE'
    elif STATUS_INTERNAL == 'CALIBRATE_BLOT':
        STATUS = "CALIBRATING"
        s = 'C/' + str(calib_offset_left) + "/" + str(calib_offset_right) + "/"
        s_binary = bytes(s, 'utf-8')
        print("CALIBRATING", calib_offset_left, calib_offset_right)
        STATUS_INTERNAL = 'IDLE'
    elif STATUS_INTERNAL == 'MANUAL_MOVEMENT':
        STATUS = "MOVE"
        s = 'M/' + str(plunging_pos * 1415) + "/" + str(cryo_pos * 1240) + "/"
        s_binary = bytes(s, 'utf-8')
        print("MOVING", plunging_pos, cryo_pos)
        STATUS_INTERNAL = 'IDLE'
    elif STATUS_INTERNAL == "HOME_STEPPERS":
        STATUS = 'CURRENTLY_HOMING'
        STATUS_INTERNAL = 'CURRENTLY_HOMING'
        s = 'H/'
        s_binary = bytes(s, 'utf-8')
        print("HOMING")
    return s_binary


class SerialCommunicator(QRunnable):
    def __init__(self):
        super().__init__()
        use_port = ""
        ports = serial.tools.list_ports.comports(include_links=False)
        if len(ports) != 0:
            for p in ports:
                print(p.name, p.device, p.description, p.manufacturer, p.product, p.serial_number, p.pid, p.vid,
                      p.interface, p.location)
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
        global temp_chamber, STATUS, ERROR_MSG, humid, temp_cryo, \
            set_temp_cryo, set_temp_chamber, set_humid, set_blot_force, \
            set_blot_time, set_blot_nr, shutdown, calib_offset_left, calib_offset_right, \
            calib_successful, waiting_for_serial, x, y_chamber, y_cryo, y_humid, \
            STATUS_INTERNAL, homing_successful, pid_ps, pid_ds, time_plot

        while True:
            if waiting_for_serial == False:
                try:
                    while self.ser.in_waiting:
                        # Read in messages from serial
                        msg = self.ser.readline()

                        msg = msg.decode("utf-8")
                        msg = msg[0:len(msg) - 1]
                        print(msg)
                        msg_split = msg.split("/")
                        identifier = msg_split[0]
                        if identifier == 'H':
                            if msg_split[1] == 'S':
                                homing_successful = True
                                STATUS_INTERNAL = 'IDLE'
                            else:
                                homing_successful = False
                                STATUS = 'ERROR HOMING'
                        if identifier == 'D':
                            temp_chamber, temp_cryo, humid = float(msg_split[1]), float(msg_split[2]), float(
                                msg_split[3])
                            if len(msg_split) == 6:  # For plotting PID values
                                pid_p, pid_d = float(msg_split[4]), float(msg_split[5])
                                pid_ps.append(pid_p)
                                pid_ds.append(pid_d)
                            x.append(x[-1] + 1)
                            if y_chamber[-1] == 0.0:
                                y_chamber[-1] = temp_chamber
                            if y_cryo[-1] == 0.0:
                                y_cryo[-1] = temp_cryo
                            if y_humid[-1] == 0.0:
                                y_humid[-1] = humid
                            y_chamber.append(temp_chamber)
                            y_cryo.append(temp_cryo)
                            y_humid.append(humid)
                            time_plot.append(datetime.datetime.now().strftime("%H:%M:%S"))
                        elif identifier == 'F' and STATUS != "ERROR":
                            STATUS = "ERROR"
                            ERROR_MSG = msg_split[1]
                            # window.warning()
                        elif identifier == 'I':
                            STATUS = msg_split[1]
                        elif identifier == 'C':
                            if msg_split[1] == 'S':
                                calib_successful = True
                            elif msg_split[1] == 'F':
                                calib_successful = False

                    # if one of the update flags is set --> Send update to UC and reset Flag
                    if STATUS_INTERNAL != 'IDLE':
                        s_binary = bytes("", 'utf-8')
                        s_binary = state_machine(calib_offset_left, calib_offset_right, s_binary, set_blot_force,
                                                 set_blot_nr, set_blot_time, set_humid, set_temp_chamber,
                                                 set_temp_cryo)
                        # print(s_binary)
                        self.ser.write(s_binary)

                except serial.serialutil.SerialException as e:
                    print(e)
                    waiting_for_serial = True  # Set Flag and try to regain serial
                    STATUS = "Connection Lost!"
            else:  # Handle if Serial communication is lost
                homing_successful = False
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
        self.ui.setupUi(self)  # Set up the external generated ui

        ########################ADD ADITIONAL FUNCTIONALITY LIKE PLOTTING######################
        self.ui.graphWidget = pg.PlotWidget(self.ui.plot1_label)
        # axis = DateAxisItem(orientation='bottom')
        # axis.attachToPlotItem(self.ui.graphWidget.getPlotItem())
        width_plots = 2000
        height_plots = 420
        self.ui.graphWidget.setMinimumSize(QSize(width_plots, height_plots))
        self.ui.graphWidget.setMaximumSize(QSize(width_plots, height_plots))
        self.ui.graphWidget.scene().sigMouseMoved.connect(self.onMouseMoved)

        self.ui.graphWidget1 = pg.PlotWidget(self.ui.plot2_label)
        self.ui.graphWidget1.setMinimumSize(QSize(width_plots, height_plots))
        self.ui.graphWidget.setMaximumSize(QSize(width_plots, height_plots))
        self.ui.graphWidget1.scene().sigMouseMoved.connect(self.onMouseMoved1)

        self.ui.graphWidget2 = pg.PlotWidget(self.ui.plot3_label)
        self.ui.graphWidget2.setMinimumSize(QSize(width_plots, height_plots))
        self.ui.graphWidget.setMaximumSize(QSize(width_plots, height_plots))
        self.ui.graphWidget2.scene().sigMouseMoved.connect(self.onMouseMoved2)

        ######################################################################################

        self.setStyleSheet(open('Combinear/Combinear.qss').read())  # Add an Stylesheet

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
        self.ui.data_export_button.clicked.connect(lambda: UIFunctions.write_csv(self))
        self.ui.clear_plots_button.clicked.connect(lambda: UIFunctions.clear_all_plots(self))

        self.ui.cryo_slider.sliderReleased.connect(lambda: UIFunctions.update_manual_positioning(self))
        self.ui.plunging_slider.sliderReleased.connect(lambda: UIFunctions.update_manual_positioning(self))
        self.ui.home_button.clicked.connect(lambda: UIFunctions.home_steppers(self))

        # self.warning()

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    def warning(self, message="Default"):
        QMessageBox.about(self, "Error", message)

    def onMouseMoved(self, evt):
        if self.ui.graphWidget.plotItem.vb.mapSceneToView(evt):
            point = self.ui.graphWidget.plotItem.vb.mapSceneToView(evt)
            if int(np.round(point.x())) < len(y_chamber) and len(y_chamber) > 0:
                self.ui.temp_chamber_plot.setText(
                    "<p style='color:white'> {0}°C</p>".format(y_chamber[int(np.round(point.x()))]))

    def onMouseMoved1(self, evt):
        if self.ui.graphWidget1.plotItem.vb.mapSceneToView(evt):
            point = self.ui.graphWidget1.plotItem.vb.mapSceneToView(evt)
            if int(np.round(point.x())) < len(y_humid) and len(y_humid) > 0:
                self.ui.humid_plot.setText(
                    "<p style='color:white'> {0}%</p>".format(y_humid[int(np.round(point.x()))]))

    def onMouseMoved2(self, evt):
        if self.ui.graphWidget2.plotItem.vb.mapSceneToView(evt):
            point = self.ui.graphWidget2.plotItem.vb.mapSceneToView(evt)
            if int(np.round(point.x())) < len(y_cryo) and len(y_cryo) > 0:
                self.ui.temp_cryo_plot.setText(
                    "<p style='color:white'> {0}°C</p>".format(y_cryo[int(np.round(point.x()))]))


class UIFunctions(QMainWindow):

    def clear_all_plots(self):
        global y_humid, y_cryo, y_chamber, x, pid_ps, pid_ps, time_plot
        y_humid, y_cryo, y_chamber, x = [0.0], [0.0], [0.0], [0]
        pid_ps, pid_ds = [0.0], [0.0]
        time_plot = [datetime.datetime.now().strftime("%H:%M:%S")]

    def write_csv(self):
        """
        Writes data from y_lists to csv file in folder
        :return:
        """
        global time_plot
        print(len(time_plot))
        print(len(y_chamber))
        rows = zip(time_plot, y_chamber, y_cryo, y_humid)
        file_name = "Data" + datetime.datetime.now().strftime("%H_%M_%S") + ".csv"
        with open(("C:\\Users\\larsg\\Desktop\\Data\\" +file_name), "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(("Time", "Temp_Chamber", "Temp_Cryo", "Temp_Humid"))
            for row in rows:
                writer.writerow(row)

    def update_labels(self, temp_chamber, temp_cryo, humid, status):
        """
        Updates the Labels in the GUI
        :param temp_chamber:
        :param temp_cryo:
        :param humid:
        :param status:
        :return:
        """
        global calib_successful, homing_successful, waiting_for_serial
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
        if homing_successful:
            self.ui.homing_sucess_label.setText("Successful")
            self.ui.homing_sucess_label.setStyleSheet(u"color: rgb(0, 170, 0);")
        else:
            self.ui.homing_sucess_label.setText("Failure")
            self.ui.homing_sucess_label.setStyleSheet(u"color: rgb(170, 0, 0);")
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
        global set_temp_chamber, set_temp_cryo, set_humid
        global STATUS_INTERNAL
        set_temp_chamber = self.ui.temp_control_2.value()
        set_temp_cryo = self.ui.temp_control_botttom_4.value()
        set_humid = self.ui.humid_control_2.value()
        STATUS_INTERNAL = 'PREHEATING'

    def update_manual_positioning(self):
        """
        Updates the global variables and sets the update Flag
        :return:
        """
        global cryo_pos, plunging_pos
        global STATUS_INTERNAL
        cryo_pos = self.ui.cryo_slider.value()
        plunging_pos = self.ui.plunging_slider.value()
        STATUS_INTERNAL = 'MANUAL_MOVEMENT'

    def update_blot_variables(self):
        """
        Updates the global variables and sets the update Flag
        :return:
        """
        global set_blot_nr, set_blot_time, set_blot_force
        global STATUS_INTERNAL
        set_blot_force = self.ui.blotting_force_control_2.value()
        set_blot_time = self.ui.blotting_time_control_2.value()
        set_blot_nr = self.ui.blotting_number_control_2.value()
        STATUS_INTERNAL = 'UPDATE_BLOT'

    def calibrate_blot_arms(self):
        """
        Updates the global variables and sets the update Flag
        :return:
        """
        global calib_offset_right, calib_offset_left, calib_successful
        global STATUS_INTERNAL
        calib_successful = True
        calib_offset_right = self.ui.calib_right.value()
        calib_offset_left = self.ui.calib_left.value()
        STATUS_INTERNAL = 'CALIBRATE_BLOT'

    def home_steppers(self):
        global STATUS_INTERNAL, homing_successful
        homing_successful = False
        self.ui.cryo_slider.setValue(0)
        self.ui.plunging_slider.setValue(100)
        STATUS_INTERNAL = 'HOME_STEPPERS'

    def shutdown(self):
        """
        Sets the Shutdown Flag
        :return:
        """
        global STATUS_INTERNAL
        self.ui.cryo_slider.setValue(0)
        self.ui.plunging_slider.setValue(0)
        STATUS_INTERNAL = 'SHUTDOWN'

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
    label_update_timer = QtCore.QTimer()
    plot_timer = QtCore.QTimer()
    # Update the Labels
    label_update_timer.timeout.connect(
        lambda: UIFunctions.update_labels(window, temp_chamber, temp_cryo, humid, STATUS))
    # Update the Plots
    plot_timer.timeout.connect(lambda: window.ui.graphWidget.clear())
    plot_timer.timeout.connect(lambda: window.ui.graphWidget.plot(x, y_chamber))
    plot_timer.timeout.connect(lambda: window.ui.graphWidget1.clear())
    plot_timer.timeout.connect(lambda: window.ui.graphWidget1.plot(x, y_humid))
    plot_timer.timeout.connect(lambda: window.ui.graphWidget2.clear())
    plot_timer.timeout.connect(lambda: window.ui.graphWidget2.plot(x, y_cryo))
    plot_timer.start(400)
    label_update_timer.start(100)  # every 100 milliseconds
    #############################################################################

    sys.exit(app.exec_())
