# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PEM_new_guioHqMZE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 652)
        MainWindow.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle_button = QPushButton(self.frame_toggle)
        self.toggle_button.setObjectName(u"toggle_button")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_button.sizePolicy().hasHeightForWidth())
        self.toggle_button.setSizePolicy(sizePolicy)
        self.toggle_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);\n"
"border: px solid\n"
"")

        self.verticalLayout_2.addWidget(self.toggle_button)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.go_settings_button = QPushButton(self.frame_top)
        self.go_settings_button.setObjectName(u"go_settings_button")
        self.go_settings_button.setMaximumSize(QSize(100, 40))
        self.go_settings_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 0px solid\n"
"}")

        self.horizontalLayout_6.addWidget(self.go_settings_button, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menues = QFrame(self.frame_left_menu)
        self.frame_top_menues.setObjectName(u"frame_top_menues")
        self.frame_top_menues.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menues.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menues)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.button_page_home = QPushButton(self.frame_top_menues)
        self.button_page_home.setObjectName(u"button_page_home")
        self.button_page_home.setMinimumSize(QSize(0, 40))
        self.button_page_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 0px solid\n"
"}")

        self.verticalLayout_4.addWidget(self.button_page_home)

        self.button_page_plots = QPushButton(self.frame_top_menues)
        self.button_page_plots.setObjectName(u"button_page_plots")
        self.button_page_plots.setMinimumSize(QSize(0, 40))
        self.button_page_plots.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 0px solid\n"
"}")

        self.verticalLayout_4.addWidget(self.button_page_plots)

        self.button_page_Data = QPushButton(self.frame_top_menues)
        self.button_page_Data.setObjectName(u"button_page_Data")
        self.button_page_Data.setMinimumSize(QSize(0, 40))
        self.button_page_Data.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 0px solid\n"
"}")

        self.verticalLayout_4.addWidget(self.button_page_Data)


        self.verticalLayout_3.addWidget(self.frame_top_menues, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_6 = QVBoxLayout(self.page_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.upper_chamer_box = QGroupBox(self.page_home)
        self.upper_chamer_box.setObjectName(u"upper_chamer_box")
        self.upper_chamer_box.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.horizontalLayoutWidget_2 = QWidget(self.upper_chamer_box)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 20, 931, 231))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.temp_box_2 = QGroupBox(self.horizontalLayoutWidget_2)
        self.temp_box_2.setObjectName(u"temp_box_2")
        self.temp_control_2 = QDoubleSpinBox(self.temp_box_2)
        self.temp_control_2.setObjectName(u"temp_control_2")
        self.temp_control_2.setGeometry(QRect(160, 80, 141, 81))
        self.temp_control_2.setValue(22.000000000000000)
        self.temp_lable_2 = QLabel(self.temp_box_2)
        self.temp_lable_2.setObjectName(u"temp_lable_2")
        self.temp_lable_2.setGeometry(QRect(40, 90, 91, 51))

        self.horizontalLayout_4.addWidget(self.temp_box_2)

        self.humid_box_2 = QGroupBox(self.horizontalLayoutWidget_2)
        self.humid_box_2.setObjectName(u"humid_box_2")
        self.humid_control_2 = QDoubleSpinBox(self.humid_box_2)
        self.humid_control_2.setObjectName(u"humid_control_2")
        self.humid_control_2.setGeometry(QRect(160, 80, 141, 81))
        self.humid_control_2.setDecimals(0)
        self.humid_control_2.setValue(80.000000000000000)
        self.humid_lable_2 = QLabel(self.humid_box_2)
        self.humid_lable_2.setObjectName(u"humid_lable_2")
        self.humid_lable_2.setGeometry(QRect(40, 90, 91, 51))

        self.horizontalLayout_4.addWidget(self.humid_box_2)

        self.blotting_box_2 = QGroupBox(self.horizontalLayoutWidget_2)
        self.blotting_box_2.setObjectName(u"blotting_box_2")
        self.blotting_force_control_2 = QDoubleSpinBox(self.blotting_box_2)
        self.blotting_force_control_2.setObjectName(u"blotting_force_control_2")
        self.blotting_force_control_2.setGeometry(QRect(160, 20, 121, 61))
        self.label_4 = QLabel(self.blotting_box_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 30, 61, 41))
        font = QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.blotting_time_control_2 = QDoubleSpinBox(self.blotting_box_2)
        self.blotting_time_control_2.setObjectName(u"blotting_time_control_2")
        self.blotting_time_control_2.setGeometry(QRect(160, 90, 121, 61))
        self.label_5 = QLabel(self.blotting_box_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 100, 61, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.blotting_box_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 170, 81, 41))
        self.label_6.setFont(font)
        self.blotting_number_control_2 = QDoubleSpinBox(self.blotting_box_2)
        self.blotting_number_control_2.setObjectName(u"blotting_number_control_2")
        self.blotting_number_control_2.setGeometry(QRect(160, 160, 121, 61))

        self.horizontalLayout_4.addWidget(self.blotting_box_2)


        self.verticalLayout_6.addWidget(self.upper_chamer_box)

        self.spacer = QWidget(self.page_home)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.spacer)

        self.cryo_box = QGroupBox(self.page_home)
        self.cryo_box.setObjectName(u"cryo_box")
        self.cryo_box.setCursor(QCursor(Qt.ArrowCursor))
        self.cryo_box.setAcceptDrops(False)
        self.cryo_box.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.cryo_box.setCheckable(False)
        self.horizontalLayoutWidget_3 = QWidget(self.cryo_box)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(9, 19, 931, 231))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.temp_box_bottom = QGroupBox(self.horizontalLayoutWidget_3)
        self.temp_box_bottom.setObjectName(u"temp_box_bottom")
        self.temp_control_botttom = QDoubleSpinBox(self.temp_box_bottom)
        self.temp_control_botttom.setObjectName(u"temp_control_botttom")
        self.temp_control_botttom.setGeometry(QRect(160, 80, 141, 81))
        self.temp_control_botttom.setMinimum(-200.000000000000000)
        self.temp_control_botttom.setValue(22.000000000000000)
        self.temp_lable_bottom = QLabel(self.temp_box_bottom)
        self.temp_lable_bottom.setObjectName(u"temp_lable_bottom")
        self.temp_lable_bottom.setGeometry(QRect(40, 90, 91, 51))

        self.horizontalLayout_5.addWidget(self.temp_box_bottom)

        self.widget = QWidget(self.horizontalLayoutWidget_3)
        self.widget.setObjectName(u"widget")
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 60, 271, 23))
        self.progressBar.setValue(24)
        self.progressBar.setInvertedAppearance(False)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(106, 20, 71, 21))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_7.setFont(font2)
        self.current_step_lable = QLabel(self.widget)
        self.current_step_lable.setObjectName(u"current_step_lable")
        self.current_step_lable.setGeometry(QRect(36, 150, 231, 61))
        self.current_step_lable.setFont(font2)
        self.current_step_lable.setLayoutDirection(Qt.LeftToRight)
        self.current_step_lable.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.widget)

        self.control_box = QGroupBox(self.horizontalLayoutWidget_3)
        self.control_box.setObjectName(u"control_box")
        self.start_button = QCommandLinkButton(self.control_box)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(60, 30, 185, 41))
        self.start_button.setStyleSheet(u"")
        self.shutdown_button = QCommandLinkButton(self.control_box)
        self.shutdown_button.setObjectName(u"shutdown_button")
        self.shutdown_button.setGeometry(QRect(60, 180, 185, 41))
        self.shutdown_button.setAutoDefault(True)
        self.shutdown_button.setDefault(False)

        self.horizontalLayout_5.addWidget(self.control_box)


        self.verticalLayout_6.addWidget(self.cryo_box)

        self.pages_widget.addWidget(self.page_home)
        self.page_plots = QWidget()
        self.page_plots.setObjectName(u"page_plots")
        self.verticalLayout_7 = QVBoxLayout(self.page_plots)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.page_plots)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setPointSize(40)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.pages_widget.addWidget(self.page_plots)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_9 = QVBoxLayout(self.page_settings)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.settings_box = QGroupBox(self.page_settings)
        self.settings_box.setObjectName(u"settings_box")
        self.settings_box.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.horizontalLayoutWidget_4 = QWidget(self.settings_box)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 20, 931, 231))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stepper_box = QGroupBox(self.horizontalLayoutWidget_4)
        self.stepper_box.setObjectName(u"stepper_box")
        self.plunge_stepper_control = QDoubleSpinBox(self.stepper_box)
        self.plunge_stepper_control.setObjectName(u"plunge_stepper_control")
        self.plunge_stepper_control.setGeometry(QRect(160, 30, 141, 61))
        self.plunge_stepper_control.setValue(22.000000000000000)
        self.plunging_lable = QLabel(self.stepper_box)
        self.plunging_lable.setObjectName(u"plunging_lable")
        self.plunging_lable.setGeometry(QRect(10, 40, 121, 51))
        self.plunging_lable.setFont(font1)
        self.cryo_stepper_control = QDoubleSpinBox(self.stepper_box)
        self.cryo_stepper_control.setObjectName(u"cryo_stepper_control")
        self.cryo_stepper_control.setGeometry(QRect(160, 140, 141, 61))
        self.cryo_stepper_control.setValue(22.000000000000000)
        self.cryo_lable = QLabel(self.stepper_box)
        self.cryo_lable.setObjectName(u"cryo_lable")
        self.cryo_lable.setGeometry(QRect(10, 150, 121, 51))
        self.cryo_lable.setFont(font1)

        self.horizontalLayout_8.addWidget(self.stepper_box)

        self.data_box = QGroupBox(self.horizontalLayoutWidget_4)
        self.data_box.setObjectName(u"data_box")
        self.verticalLayoutWidget = QWidget(self.data_box)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 291, 201))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.buzzer_button = QRadioButton(self.verticalLayoutWidget)
        self.buzzer_button.setObjectName(u"buzzer_button")

        self.verticalLayout_8.addWidget(self.buzzer_button)

        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_8.addWidget(self.radioButton_3)

        self.radioButton = QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_8.addWidget(self.radioButton)


        self.horizontalLayout_8.addWidget(self.data_box)

        self.blotting_box_3 = QGroupBox(self.horizontalLayoutWidget_4)
        self.blotting_box_3.setObjectName(u"blotting_box_3")
        self.blotting_force_control_3 = QDoubleSpinBox(self.blotting_box_3)
        self.blotting_force_control_3.setObjectName(u"blotting_force_control_3")
        self.blotting_force_control_3.setGeometry(QRect(160, 20, 121, 61))
        self.label_10 = QLabel(self.blotting_box_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 30, 61, 41))
        self.label_10.setFont(font)
        self.blotting_time_control_3 = QDoubleSpinBox(self.blotting_box_3)
        self.blotting_time_control_3.setObjectName(u"blotting_time_control_3")
        self.blotting_time_control_3.setGeometry(QRect(160, 90, 121, 61))
        self.label_11 = QLabel(self.blotting_box_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 100, 61, 41))
        self.label_11.setFont(font)
        self.label_12 = QLabel(self.blotting_box_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 170, 81, 41))
        self.label_12.setFont(font)
        self.blotting_number_control_3 = QDoubleSpinBox(self.blotting_box_3)
        self.blotting_number_control_3.setObjectName(u"blotting_number_control_3")
        self.blotting_number_control_3.setGeometry(QRect(160, 160, 121, 61))

        self.horizontalLayout_8.addWidget(self.blotting_box_3)


        self.verticalLayout_9.addWidget(self.settings_box)

        self.pages_widget.addWidget(self.page_settings)
        self.page_dataExport = QWidget()
        self.page_dataExport.setObjectName(u"page_dataExport")
        self.horizontalLayout_7 = QHBoxLayout(self.page_dataExport)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.page_dataExport)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.pages_widget.addWidget(self.page_dataExport)

        self.verticalLayout_5.addWidget(self.pages_widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pages_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_button.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.go_settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.button_page_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.button_page_plots.setText(QCoreApplication.translate("MainWindow", u"Plots", None))
        self.button_page_Data.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.upper_chamer_box.setTitle(QCoreApplication.translate("MainWindow", u"Upper Chamber", None))
        self.temp_box_2.setTitle(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.temp_lable_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.humid_box_2.setTitle(QCoreApplication.translate("MainWindow", u"Humitity", None))
        self.humid_lable_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.blotting_box_2.setTitle(QCoreApplication.translate("MainWindow", u"Blotting", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Force:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Number:", None))
#if QT_CONFIG(whatsthis)
        self.cryo_box.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.cryo_box.setTitle(QCoreApplication.translate("MainWindow", u"Cryo Bath", None))
        self.temp_box_bottom.setTitle(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.temp_lable_bottom.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.current_step_lable.setText(QCoreApplication.translate("MainWindow", u"Current Step", None))
        self.control_box.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.shutdown_button.setText(QCoreApplication.translate("MainWindow", u"Shutdown", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Page Plots", None))
        self.settings_box.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.stepper_box.setTitle(QCoreApplication.translate("MainWindow", u"Steppers", None))
        self.plunging_lable.setText(QCoreApplication.translate("MainWindow", u"Plunging Arm", None))
        self.cryo_lable.setText(QCoreApplication.translate("MainWindow", u"Cryo Platfom", None))
        self.data_box.setTitle(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.buzzer_button.setText(QCoreApplication.translate("MainWindow", u"Buzzer on", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.blotting_box_3.setTitle(QCoreApplication.translate("MainWindow", u"Blotting", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Force:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Number:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Page Data", None))
    # retranslateUi

