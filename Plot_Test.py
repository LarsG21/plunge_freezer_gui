import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
import numpy as np
import pyqtgraph as pg


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(726, 595)
        self.graphicsView = pg.PlotWidget(Form)
        self.graphicsView.setGeometry(QtCore.QRect(75, 131, 621, 441))
        self.graphicsView.setObjectName("graphicsView")


class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        x = np.linspace(-100, 100, 1000)
        self.data = np.sin(x) / x
        print(type(self.data))
        self.graphicsView.plot(self.data, pen=(255, 255, 255, 200))
        self.label = pg.TextItem(text="Abscissa: {}".format(0))
        self.graphicsView.addItem(self.label)
        self.setMouseTracking(True)
        self.graphicsView.scene().sigMouseMoved.connect(self.onMouseMoved)

    def onMouseMoved(self, evt):
        if self.graphicsView.plotItem.vb.mapSceneToView(evt):
            point = self.graphicsView.plotItem.vb.mapSceneToView(evt)
            print(int(np.round(point.x())))
            self.label.setHtml("<p style='color:white'>Abscissa: {0}</p>".format(self.data[int(np.round(point.x()))]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())