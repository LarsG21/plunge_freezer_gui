# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PEM_new_guiYcIHSM.ui'
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
        MainWindow.resize(1080, 640)
        MainWindow.setMinimumSize(QSize(1080, 640))
        MainWindow.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACT"
                        "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #3a3a3a;\n"
"	color: #fff;\n"
"	selection-background-color: #b78620;\n"
"	selection-color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #000;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"	background-color: rgb(183, 134, 32);\n"
""
                        "	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"   	background-color: rgb(183, 134, 32);\n"
"	height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBar-----*/\n"
"QToolBar\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(69, 69, 69, 255),stop"
                        ":1 rgba(58, 58, 58, 255));\n"
"	border-top: none;\n"
"	border-bottom: 1px solid #4f4f4f;\n"
"	border-left: 1px solid #4f4f4f;\n"
"	border-right: 1px solid #4f4f4f;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBar::separator\n"
"{\n"
"	background-color: #2e2e2e;\n"
"	width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	padding: 5px;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"	margin-left: 1px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"	\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, "
                        "50, 255));\n"
"	border: 1px solid #222;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"	color: #ffffff;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #b78620;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #131313;\n"
"	color : #eee;\n"
"	border: 1px solid #343434;\n"
"	border-radius: 2px;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPlainTExtEdit-----*/\n"
"QPlainTextEdit\n"
"{\n"
"	background-color: #131313;\n"
"	color : #eee;\n"
"	border: 1px solid #343434;\n"
"	border-radius: 2px;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabBar-----*/\n"
"QTabBar::tab\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #666;\n"
"	border-bottom: none;\n"
"	padding: 5px;\n"
"	padding-lef"
                        "t: 15px;\n"
"	padding-right: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"	background-color: red;\n"
"	border: 1px solid #666;\n"
"	top: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"	margin-right: 0; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"	background-color: #0c0c0d;\n"
"	margin-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"	color: #b1b1b1;\n"
"	border-bottom-style: solid;\n"
"	background-color: #0c0c0d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"	margin-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"	border-top-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #000;\n"
"    padding-left: 6px;\n"
"    color: #ffffff;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"	b"
                        "ackground-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #b78620;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #b78620;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDateTimeEdit-----*/\n"
"QSpinBox,\n"
"QDateTimeEdit \n"
"{\n"
"    background"
                        "-color: #131313;\n"
"	color : #eee;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"    border-radius : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, \n"
"QDateTimeEdit::up-button\n"
"{\n"
"	border-top-right-radius:2px;\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, \n"
"QDateTimeEdit::up-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, \n"
"QDateTimeEdit::up-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button, \n"
"QDateTimeEdit::down-button\n"
"{\n"
"	border-bottom-right-radius:2px;\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
""
                        "QSpinBox::down-button:hover, \n"
"QDateTimeEdit::down-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:pressed, \n"
"QDateTimeEdit::down-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"	border-radius: 5px;\n"
"    margin-top: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: transparent;\n"
"    color: #eee;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2"
                        ":1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #000;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"	padding: 4px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeView\n"
"{\n"
"	show-decoration-selected: 1;\n"
"	alternate-background-color: #3a3a3a;\n"
"	selection-color: #fff;\n"
"	background-color: #2d2d2d;\n"
"	border: 1px solid gray;\n"
"	padding-top : 5px;\n"
"	color: #fff;\n"
"	font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"	color:#fff;\n"
"	background-color: #b78620;\n"
"	border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"	image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branc"
                        "h:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"	image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"    border : none;\n"
"    color: white;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"	border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"	background-color: #2d2d2d;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate \n"
"{\n"
"    background-color: #3a3a3a;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"    color: lightgray;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"	background-color: #b78620;\n"
"    border: 1px solid #3a546e;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"	border: 1px solid #b78620; \n"
"\n"
"}\n"
"\n"
"\n"
""
                        "QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton \n"
"{\n"
"	color: lightgray;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"	background-color: lightgray;\n"
"	border: 2px solid #b78620;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"	border: 2px solid #b78620;\n"
"	border-radius: 6px;\n"
"	background-color: rgba(183,134,32,20%);  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider::groove:horizontal \n"
"{\n"
"	background-color: transparent;\n"
"	height: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"	background-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"	background-color: #131313;\n"
""
                        "\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"	background-color: #b78620;\n"
"	width: 14px;\n"
"	margin-top: -6px;\n"
"	margin-bottom: -6px;\n"
"	border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"	background-color: #d89e25;\n"
"	border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:"
                        "1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arr"
                        "ow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 16px;\n"
"	border: 1px solid #2d2d2d;\n"
"    margin: 16px 0px 16px 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"	background-color: qlinear"
                        "gradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    border: 1px solid #666666;\n"
"    text-align: center;\n"
"	color: #000;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #b78620;\n"
"    width: 30px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"")
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
        self.toggle_button.setMinimumSize(QSize(70, 0))
        self.toggle_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(85, 170, 255,20%);\n"
"border: px solid\n"
"")
        icon = QIcon()
        icon.addFile(u"Icons/Hamburger_icon.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_button.setIcon(icon)
        self.toggle_button.setIconSize(QSize(32, 32))

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
        icon1 = QIcon()
        icon1.addFile(u"Icons/2000px-WMF-Agora-Settings_BCBCBC.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.go_settings_button.setIcon(icon1)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_page_home.sizePolicy().hasHeightForWidth())
        self.button_page_home.setSizePolicy(sizePolicy1)
        self.button_page_home.setMinimumSize(QSize(70, 60))
        self.button_page_home.setMaximumSize(QSize(16777215, 16777215))
        self.button_page_home.setBaseSize(QSize(60, 60))
        self.button_page_home.setAcceptDrops(False)
        self.button_page_home.setLayoutDirection(Qt.LeftToRight)
        self.button_page_home.setAutoFillBackground(False)
        self.button_page_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 0px solid\n"
"}\n"
"\n"
"")
        self.button_page_home.setInputMethodHints(Qt.ImhNone)
        icon2 = QIcon()
        icon2.addFile(u"Icons/217-2171720_icon-white-house-home-icon-white-png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_page_home.setIcon(icon2)
        self.button_page_home.setIconSize(QSize(24, 24))
        self.button_page_home.setAutoRepeat(True)
        self.button_page_home.setAutoExclusive(False)
        self.button_page_home.setFlat(False)

        self.verticalLayout_4.addWidget(self.button_page_home)

        self.button_page_plots = QPushButton(self.frame_top_menues)
        self.button_page_plots.setObjectName(u"button_page_plots")
        self.button_page_plots.setMinimumSize(QSize(70, 60))
        self.button_page_plots.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 0px solid\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"Icons/Plot_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_page_plots.setIcon(icon3)
        self.button_page_plots.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.button_page_plots)

        self.button_page_Data = QPushButton(self.frame_top_menues)
        self.button_page_Data.setObjectName(u"button_page_Data")
        self.button_page_Data.setMinimumSize(QSize(70, 60))
        self.button_page_Data.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 0px solid\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"Icons/Fiel2.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_page_Data.setIcon(icon4)
        self.button_page_Data.setIconSize(QSize(40, 40))

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
        self.pages_widget.setLayoutDirection(Qt.LeftToRight)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_6 = QVBoxLayout(self.page_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.upper_chamer_box = QGroupBox(self.page_home)
        self.upper_chamer_box.setObjectName(u"upper_chamer_box")
        self.upper_chamer_box.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.horizontalLayout_4 = QHBoxLayout(self.upper_chamer_box)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.temp_box_2 = QGroupBox(self.upper_chamer_box)
        self.temp_box_2.setObjectName(u"temp_box_2")
        self.temp_control_2 = QDoubleSpinBox(self.temp_box_2)
        self.temp_control_2.setObjectName(u"temp_control_2")
        self.temp_control_2.setGeometry(QRect(160, 80, 141, 81))
        self.temp_control_2.setStyleSheet(u"")
        self.temp_control_2.setValue(22.000000000000000)
        self.temp_lable_2 = QLabel(self.temp_box_2)
        self.temp_lable_2.setObjectName(u"temp_lable_2")
        self.temp_lable_2.setGeometry(QRect(40, 90, 91, 51))

        self.horizontalLayout_4.addWidget(self.temp_box_2)

        self.humid_box_2 = QGroupBox(self.upper_chamer_box)
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

        self.blotting_box_2 = QGroupBox(self.upper_chamer_box)
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
        self.horizontalLayout_11 = QHBoxLayout(self.cryo_box)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.temp_box_bottom_4 = QGroupBox(self.cryo_box)
        self.temp_box_bottom_4.setObjectName(u"temp_box_bottom_4")
        self.temp_control_botttom_4 = QDoubleSpinBox(self.temp_box_bottom_4)
        self.temp_control_botttom_4.setObjectName(u"temp_control_botttom_4")
        self.temp_control_botttom_4.setGeometry(QRect(160, 80, 141, 81))
        self.temp_control_botttom_4.setMinimum(-200.000000000000000)
        self.temp_control_botttom_4.setValue(22.000000000000000)
        self.temp_lable_bottom_4 = QLabel(self.temp_box_bottom_4)
        self.temp_lable_bottom_4.setObjectName(u"temp_lable_bottom_4")
        self.temp_lable_bottom_4.setGeometry(QRect(40, 90, 91, 51))

        self.horizontalLayout_11.addWidget(self.temp_box_bottom_4)

        self.frame = QFrame(self.cryo_box)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(60, 80, 211, 23))
        self.progressBar.setValue(24)
        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(110, 20, 111, 41))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_22.setFont(font2)
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(110, 150, 121, 51))

        self.horizontalLayout_11.addWidget(self.frame)

        self.control_box_4 = QGroupBox(self.cryo_box)
        self.control_box_4.setObjectName(u"control_box_4")
        self.start_button_4 = QCommandLinkButton(self.control_box_4)
        self.start_button_4.setObjectName(u"start_button_4")
        self.start_button_4.setGeometry(QRect(60, 30, 185, 41))
        self.start_button_4.setStyleSheet(u"")
        self.shutdown_button_4 = QCommandLinkButton(self.control_box_4)
        self.shutdown_button_4.setObjectName(u"shutdown_button_4")
        self.shutdown_button_4.setGeometry(QRect(60, 180, 185, 41))
        self.shutdown_button_4.setAutoDefault(True)
        self.shutdown_button_4.setDefault(False)

        self.horizontalLayout_11.addWidget(self.control_box_4)


        self.verticalLayout_6.addWidget(self.cryo_box)

        self.pages_widget.addWidget(self.page_home)
        self.page_plots = QWidget()
        self.page_plots.setObjectName(u"page_plots")
        self.verticalLayout_12 = QVBoxLayout(self.page_plots)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pages_widget.addWidget(self.page_plots)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_9 = QVBoxLayout(self.page_settings)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.settings_box = QGroupBox(self.page_settings)
        self.settings_box.setObjectName(u"settings_box")
        self.settings_box.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.horizontalLayout_3 = QHBoxLayout(self.settings_box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.stepper_box = QGroupBox(self.settings_box)
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

        self.data_box = QGroupBox(self.settings_box)
        self.data_box.setObjectName(u"data_box")
        self.verticalLayoutWidget = QWidget(self.data_box)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 291, 201))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.buzzer_button = QCheckBox(self.verticalLayoutWidget)
        self.buzzer_button.setObjectName(u"buzzer_button")

        self.verticalLayout_8.addWidget(self.buzzer_button)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_8.addWidget(self.checkBox_3)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_8.addWidget(self.checkBox)


        self.horizontalLayout_8.addWidget(self.data_box)

        self.blotting_box_3 = QGroupBox(self.settings_box)
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


        self.horizontalLayout_3.addLayout(self.horizontalLayout_8)


        self.verticalLayout_9.addWidget(self.settings_box)

        self.pages_widget.addWidget(self.page_settings)
        self.page_dataExport = QWidget()
        self.page_dataExport.setObjectName(u"page_dataExport")
        self.horizontalLayout_7 = QHBoxLayout(self.page_dataExport)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.page_dataExport)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setPointSize(40)
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

        self.button_page_home.setDefault(False)
        self.pages_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_button.setText("")
        self.go_settings_button.setText("")
#if QT_CONFIG(whatsthis)
        self.button_page_home.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.button_page_home.setText("")
        self.button_page_plots.setText("")
        self.button_page_Data.setText("")
#if QT_CONFIG(whatsthis)
        self.pages_widget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
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
        self.temp_box_bottom_4.setTitle(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.temp_lable_bottom_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Current Step", None))
        self.control_box_4.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.start_button_4.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.shutdown_button_4.setText(QCoreApplication.translate("MainWindow", u"Shutdown", None))
        self.settings_box.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.stepper_box.setTitle(QCoreApplication.translate("MainWindow", u"Steppers", None))
        self.plunging_lable.setText(QCoreApplication.translate("MainWindow", u"Plunging Arm", None))
        self.cryo_lable.setText(QCoreApplication.translate("MainWindow", u"Cryo Platfom", None))
        self.data_box.setTitle(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.buzzer_button.setText(QCoreApplication.translate("MainWindow", u"Buzzer on", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.blotting_box_3.setTitle(QCoreApplication.translate("MainWindow", u"Blotting", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Force:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Number:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Page Data", None))
    # retranslateUi

