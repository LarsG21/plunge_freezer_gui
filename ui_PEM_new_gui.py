# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PEM_new_guiqXlHZL.ui'
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
        MainWindow.resize(1080, 700)
        MainWindow.setMinimumSize(QSize(1080, 700))
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
        self.toggle_button.setMinimumSize(QSize(90, 0))
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
        self.frame_14 = QFrame(self.frame_top)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_2 = QFrame(self.frame_14)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(20, 20))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_2)

        self.connection_frame = QFrame(self.frame_14)
        self.connection_frame.setObjectName(u"connection_frame")
        self.connection_frame.setMinimumSize(QSize(20, 20))
        self.connection_frame.setMaximumSize(QSize(20, 20))
        self.connection_frame.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.connection_frame.setFrameShape(QFrame.StyledPanel)
        self.connection_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.connection_frame)


        self.horizontalLayout_6.addWidget(self.frame_14)

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

        self.horizontalLayout_6.addWidget(self.go_settings_button)


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
        self.button_page_home.setMinimumSize(QSize(90, 60))
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
        self.button_page_plots.setMinimumSize(QSize(90, 60))
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
        self.button_page_Data.setMinimumSize(QSize(90, 60))
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
        self.temp_box_2.setMinimumSize(QSize(0, 245))
        self.gridLayout = QGridLayout(self.temp_box_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.temp_box_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 91))
        self.frame_3.setMaximumSize(QSize(16777215, 91))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.temp_lable_2 = QLabel(self.frame_3)
        self.temp_lable_2.setObjectName(u"temp_lable_2")
        self.temp_lable_2.setMinimumSize(QSize(91, 51))
        font = QFont()
        font.setPointSize(9)
        self.temp_lable_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.temp_lable_2)

        self.temp_control_2 = QDoubleSpinBox(self.frame_3)
        self.temp_control_2.setObjectName(u"temp_control_2")
        self.temp_control_2.setMinimumSize(QSize(141, 81))
        self.temp_control_2.setStyleSheet(u"")
        self.temp_control_2.setValue(22.000000000000000)

        self.horizontalLayout_5.addWidget(self.temp_control_2)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.temp_box_2)

        self.humid_box_2 = QGroupBox(self.upper_chamer_box)
        self.humid_box_2.setObjectName(u"humid_box_2")
        self.humid_box_2.setMinimumSize(QSize(0, 245))
        self.gridLayout_2 = QGridLayout(self.humid_box_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_4 = QFrame(self.humid_box_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 91))
        self.frame_4.setMaximumSize(QSize(16777215, 91))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.humid_lable_2 = QLabel(self.frame_4)
        self.humid_lable_2.setObjectName(u"humid_lable_2")
        self.humid_lable_2.setMinimumSize(QSize(91, 51))
        self.humid_lable_2.setFont(font)

        self.horizontalLayout_9.addWidget(self.humid_lable_2)

        self.humid_control_2 = QDoubleSpinBox(self.frame_4)
        self.humid_control_2.setObjectName(u"humid_control_2")
        self.humid_control_2.setMinimumSize(QSize(141, 81))
        self.humid_control_2.setDecimals(0)
        self.humid_control_2.setValue(80.000000000000000)

        self.horizontalLayout_9.addWidget(self.humid_control_2)


        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.humid_box_2)

        self.blotting_box_2 = QGroupBox(self.upper_chamer_box)
        self.blotting_box_2.setObjectName(u"blotting_box_2")
        self.blotting_box_2.setMinimumSize(QSize(0, 245))
        self.verticalLayout_7 = QVBoxLayout(self.blotting_box_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_6 = QFrame(self.blotting_box_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(311, 76))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(61, 41))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_4.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_4)

        self.blotting_force_control_2 = QDoubleSpinBox(self.frame_6)
        self.blotting_force_control_2.setObjectName(u"blotting_force_control_2")
        self.blotting_force_control_2.setMinimumSize(QSize(121, 61))
        self.blotting_force_control_2.setDecimals(0)
        self.blotting_force_control_2.setValue(1.000000000000000)

        self.horizontalLayout_12.addWidget(self.blotting_force_control_2)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.blotting_box_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(81, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(16)
        self.label_5.setFont(font2)

        self.horizontalLayout_13.addWidget(self.label_5)

        self.blotting_time_control_2 = QDoubleSpinBox(self.frame_7)
        self.blotting_time_control_2.setObjectName(u"blotting_time_control_2")
        self.blotting_time_control_2.setMinimumSize(QSize(121, 61))
        self.blotting_time_control_2.setDecimals(0)
        self.blotting_time_control_2.setValue(1.000000000000000)

        self.horizontalLayout_13.addWidget(self.blotting_time_control_2)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.blotting_box_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(81, 41))
        self.label_6.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_6)

        self.blotting_number_control_2 = QDoubleSpinBox(self.frame_8)
        self.blotting_number_control_2.setObjectName(u"blotting_number_control_2")
        self.blotting_number_control_2.setMinimumSize(QSize(121, 61))
        self.blotting_number_control_2.setDecimals(0)
        self.blotting_number_control_2.setValue(1.000000000000000)

        self.horizontalLayout_14.addWidget(self.blotting_number_control_2)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.horizontalLayout_4.addWidget(self.blotting_box_2)


        self.verticalLayout_6.addWidget(self.upper_chamer_box)

        self.spacer = QWidget(self.page_home)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setMaximumSize(QSize(16777215, 10))
        self.spacer.setContextMenuPolicy(Qt.NoContextMenu)

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
        self.temp_box_bottom_4.setMinimumSize(QSize(331, 229))
        self.gridLayout_3 = QGridLayout(self.temp_box_bottom_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_5 = QFrame(self.temp_box_bottom_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 91))
        self.frame_5.setMaximumSize(QSize(16777215, 91))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.temp_lable_bottom_4 = QLabel(self.frame_5)
        self.temp_lable_bottom_4.setObjectName(u"temp_lable_bottom_4")
        self.temp_lable_bottom_4.setMinimumSize(QSize(91, 51))
        self.temp_lable_bottom_4.setFont(font)

        self.horizontalLayout_10.addWidget(self.temp_lable_bottom_4)

        self.temp_control_botttom_4 = QDoubleSpinBox(self.frame_5)
        self.temp_control_botttom_4.setObjectName(u"temp_control_botttom_4")
        self.temp_control_botttom_4.setMinimumSize(QSize(141, 81))
        self.temp_control_botttom_4.setMinimum(-200.000000000000000)
        self.temp_control_botttom_4.setValue(-180.000000000000000)

        self.horizontalLayout_10.addWidget(self.temp_control_botttom_4)


        self.gridLayout_3.addWidget(self.frame_5, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.temp_box_bottom_4)

        self.frame = QFrame(self.cryo_box)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(160, 45))
        self.label_22.setMaximumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(16)
        self.label_22.setFont(font3)

        self.gridLayout_5.addWidget(self.label_22, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(251, 31))
        self.progressBar.setMaximumSize(QSize(251, 31))
        self.progressBar.setValue(42)

        self.gridLayout_5.addWidget(self.progressBar, 1, 0, 1, 1)

        self.current_step_label = QLabel(self.frame)
        self.current_step_label.setObjectName(u"current_step_label")
        self.current_step_label.setMinimumSize(QSize(241, 51))
        self.current_step_label.setMaximumSize(QSize(241, 51))

        self.gridLayout_5.addWidget(self.current_step_label, 2, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame)

        self.control_box_4 = QGroupBox(self.cryo_box)
        self.control_box_4.setObjectName(u"control_box_4")
        self.control_box_4.setMinimumSize(QSize(331, 229))
        self.gridLayout_4 = QGridLayout(self.control_box_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.prep_button = QCommandLinkButton(self.control_box_4)
        self.prep_button.setObjectName(u"prep_button")
        self.prep_button.setMinimumSize(QSize(92, 41))
        self.prep_button.setMaximumSize(QSize(185, 41))
        self.prep_button.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.prep_button, 0, 0, 1, 1)

        self.start_button_4 = QCommandLinkButton(self.control_box_4)
        self.start_button_4.setObjectName(u"start_button_4")
        self.start_button_4.setMinimumSize(QSize(92, 41))
        self.start_button_4.setMaximumSize(QSize(185, 41))
        self.start_button_4.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.start_button_4, 1, 0, 1, 1)

        self.shutdown_button_4 = QCommandLinkButton(self.control_box_4)
        self.shutdown_button_4.setObjectName(u"shutdown_button_4")
        self.shutdown_button_4.setMinimumSize(QSize(92, 41))
        self.shutdown_button_4.setMaximumSize(QSize(185, 41))
        self.shutdown_button_4.setAutoDefault(True)
        self.shutdown_button_4.setDefault(False)

        self.gridLayout_4.addWidget(self.shutdown_button_4, 2, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.control_box_4)


        self.verticalLayout_6.addWidget(self.cryo_box)

        self.pages_widget.addWidget(self.page_home)
        self.page_plots = QWidget()
        self.page_plots.setObjectName(u"page_plots")
        self.verticalLayout_12 = QVBoxLayout(self.page_plots)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.plot_box = QGroupBox(self.page_plots)
        self.plot_box.setObjectName(u"plot_box")
        self.gridLayout_6 = QGridLayout(self.plot_box)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.plot1_label_box = QGroupBox(self.plot_box)
        self.plot1_label_box.setObjectName(u"plot1_label_box")
        self.horizontalLayout_22 = QHBoxLayout(self.plot1_label_box)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.plot1_label = QFrame(self.plot1_label_box)
        self.plot1_label.setObjectName(u"plot1_label")
        self.plot1_label.setFrameShape(QFrame.StyledPanel)
        self.plot1_label.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.plot1_label)
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.horizontalLayout_22.addWidget(self.plot1_label)

        self.frame_17 = QFrame(self.plot1_label_box)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(100, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_17)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.temp_chamber_plot = QLabel(self.frame_17)
        self.temp_chamber_plot.setObjectName(u"temp_chamber_plot")

        self.gridLayout_12.addWidget(self.temp_chamber_plot, 0, 0, 1, 1)


        self.horizontalLayout_22.addWidget(self.frame_17)


        self.verticalLayout_8.addWidget(self.plot1_label_box)

        self.plot2_label_box = QGroupBox(self.plot_box)
        self.plot2_label_box.setObjectName(u"plot2_label_box")
        self.horizontalLayout_23 = QHBoxLayout(self.plot2_label_box)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.plot2_label = QFrame(self.plot2_label_box)
        self.plot2_label.setObjectName(u"plot2_label")
        self.plot2_label.setFrameShape(QFrame.StyledPanel)
        self.plot2_label.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.plot2_label)
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.horizontalLayout_23.addWidget(self.plot2_label)

        self.frame_18 = QFrame(self.plot2_label_box)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(100, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_18)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.humid_plot = QLabel(self.frame_18)
        self.humid_plot.setObjectName(u"humid_plot")

        self.gridLayout_13.addWidget(self.humid_plot, 0, 0, 1, 1)


        self.horizontalLayout_23.addWidget(self.frame_18)


        self.verticalLayout_8.addWidget(self.plot2_label_box)

        self.plot3_label_box = QGroupBox(self.plot_box)
        self.plot3_label_box.setObjectName(u"plot3_label_box")
        self.horizontalLayout_24 = QHBoxLayout(self.plot3_label_box)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.plot3_label = QFrame(self.plot3_label_box)
        self.plot3_label.setObjectName(u"plot3_label")
        self.plot3_label.setFrameShape(QFrame.StyledPanel)
        self.plot3_label.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.plot3_label)
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.horizontalLayout_24.addWidget(self.plot3_label)

        self.frame_19 = QFrame(self.plot3_label_box)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(100, 16777215))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_19)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.temp_cryo_plot = QLabel(self.frame_19)
        self.temp_cryo_plot.setObjectName(u"temp_cryo_plot")

        self.gridLayout_14.addWidget(self.temp_cryo_plot, 0, 0, 1, 1)


        self.horizontalLayout_24.addWidget(self.frame_19)


        self.verticalLayout_8.addWidget(self.plot3_label_box)


        self.gridLayout_6.addLayout(self.verticalLayout_8, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.plot_box)

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
        self.verticalLayout_11 = QVBoxLayout(self.stepper_box)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_13 = QFrame(self.stepper_box)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(311, 76))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.plunging_lable = QLabel(self.frame_13)
        self.plunging_lable.setObjectName(u"plunging_lable")
        self.plunging_lable.setFont(font2)

        self.horizontalLayout_18.addWidget(self.plunging_lable)

        self.plunging_slider = QSlider(self.frame_13)
        self.plunging_slider.setObjectName(u"plunging_slider")
        self.plunging_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_18.addWidget(self.plunging_slider)


        self.verticalLayout_11.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.stepper_box)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(311, 76))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.cryo_lable = QLabel(self.frame_12)
        self.cryo_lable.setObjectName(u"cryo_lable")
        self.cryo_lable.setFont(font2)

        self.horizontalLayout_19.addWidget(self.cryo_lable)

        self.cryo_slider = QSlider(self.frame_12)
        self.cryo_slider.setObjectName(u"cryo_slider")
        self.cryo_slider.setOrientation(Qt.Vertical)

        self.horizontalLayout_19.addWidget(self.cryo_slider)


        self.verticalLayout_11.addWidget(self.frame_12)

        self.frame_15 = QFrame(self.stepper_box)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 50))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(120, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_16)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.homing_sucess_label = QLabel(self.frame_16)
        self.homing_sucess_label.setObjectName(u"homing_sucess_label")
        self.homing_sucess_label.setFont(font1)
        self.homing_sucess_label.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.gridLayout_11.addWidget(self.homing_sucess_label, 0, 0, 1, 1)


        self.horizontalLayout_21.addWidget(self.frame_16)

        self.home_button = QPushButton(self.frame_15)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setMinimumSize(QSize(92, 40))
        self.home_button.setMaximumSize(QSize(160, 30))

        self.horizontalLayout_21.addWidget(self.home_button)


        self.verticalLayout_11.addWidget(self.frame_15)


        self.horizontalLayout_8.addWidget(self.stepper_box)

        self.data_box = QGroupBox(self.settings_box)
        self.data_box.setObjectName(u"data_box")
        self.gridLayout_7 = QGridLayout(self.data_box)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.buzzer_button = QCheckBox(self.data_box)
        self.buzzer_button.setObjectName(u"buzzer_button")
        self.buzzer_button.setMinimumSize(QSize(289, 31))

        self.gridLayout_7.addWidget(self.buzzer_button, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.data_box)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMinimumSize(QSize(0, 31))

        self.gridLayout_7.addWidget(self.checkBox_3, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.data_box)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 31))

        self.gridLayout_7.addWidget(self.checkBox, 2, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.data_box)

        self.blotting_box_3 = QGroupBox(self.settings_box)
        self.blotting_box_3.setObjectName(u"blotting_box_3")
        self.verticalLayout_10 = QVBoxLayout(self.blotting_box_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_9 = QFrame(self.blotting_box_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(311, 76))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(121, 41))
        self.label_10.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_10)

        self.calib_right = QDoubleSpinBox(self.frame_9)
        self.calib_right.setObjectName(u"calib_right")
        self.calib_right.setMinimumSize(QSize(121, 61))
        self.calib_right.setDecimals(0)
        self.calib_right.setMinimum(-100.000000000000000)
        self.calib_right.setMaximum(100.000000000000000)
        self.calib_right.setValue(0.000000000000000)

        self.horizontalLayout_15.addWidget(self.calib_right)


        self.verticalLayout_10.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.blotting_box_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(311, 76))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(111, 41))
        self.label_11.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_11)

        self.calib_left = QDoubleSpinBox(self.frame_10)
        self.calib_left.setObjectName(u"calib_left")
        self.calib_left.setMinimumSize(QSize(121, 61))
        self.calib_left.setDecimals(0)
        self.calib_left.setMinimum(-100.000000000000000)

        self.horizontalLayout_16.addWidget(self.calib_left)


        self.verticalLayout_10.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.blotting_box_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(311, 76))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.calib_sucess_label = QLabel(self.frame_11)
        self.calib_sucess_label.setObjectName(u"calib_sucess_label")
        self.calib_sucess_label.setFont(font1)
        self.calib_sucess_label.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.horizontalLayout_17.addWidget(self.calib_sucess_label)

        self.calib_save_button = QPushButton(self.frame_11)
        self.calib_save_button.setObjectName(u"calib_save_button")

        self.horizontalLayout_17.addWidget(self.calib_save_button)


        self.verticalLayout_10.addWidget(self.frame_11)


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
        font4 = QFont()
        font4.setPointSize(40)
        self.label_9.setFont(font4)
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
        self.current_step_label.setText(QCoreApplication.translate("MainWindow", u"Current Step", None))
        self.control_box_4.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.prep_button.setText(QCoreApplication.translate("MainWindow", u"Preheat", None))
        self.start_button_4.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.shutdown_button_4.setText(QCoreApplication.translate("MainWindow", u"Shutdown", None))
        self.plot_box.setTitle(QCoreApplication.translate("MainWindow", u"Plots", None))
        self.plot1_label_box.setTitle(QCoreApplication.translate("MainWindow", u"Temp Chamber \u00b0C", None))
        self.temp_chamber_plot.setText(QCoreApplication.translate("MainWindow", u"           -           ", None))
        self.plot2_label_box.setTitle(QCoreApplication.translate("MainWindow", u"Humidity %", None))
        self.humid_plot.setText(QCoreApplication.translate("MainWindow", u"           -           ", None))
        self.plot3_label_box.setTitle(QCoreApplication.translate("MainWindow", u"Temp Cryo Bath \u00b0C", None))
        self.temp_cryo_plot.setText(QCoreApplication.translate("MainWindow", u"           -           ", None))
        self.settings_box.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.stepper_box.setTitle(QCoreApplication.translate("MainWindow", u"Steppers", None))
        self.plunging_lable.setText(QCoreApplication.translate("MainWindow", u"Plunging Arm", None))
        self.cryo_lable.setText(QCoreApplication.translate("MainWindow", u"Cryo Platfom", None))
        self.homing_sucess_label.setText(QCoreApplication.translate("MainWindow", u"Sucess", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"Home Steppers", None))
        self.data_box.setTitle(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.buzzer_button.setText(QCoreApplication.translate("MainWindow", u"Buzzer on", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"RGB on", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.blotting_box_3.setTitle(QCoreApplication.translate("MainWindow", u"Blotting Calibration", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Right Arm", None))
        self.calib_right.setSuffix("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Left Arm", None))
        self.calib_sucess_label.setText(QCoreApplication.translate("MainWindow", u"Sucess", None))
        self.calib_save_button.setText(QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Page Data", None))
    # retranslateUi

