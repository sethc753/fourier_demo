"""This module defines a class for the demo GUI"""
from PyQt5 import QtWidgets
from fourier_ui import Ui_FourierUi


class FourierView(QtWidgets.QMainWindow):
    """Class to construct and manage the application UI"""
    def __init__(self):
        super().__init__()

        self.ui = Ui_FourierUi()
        self.ui.setupUi(self)
        self.show()

    def clearPlots(self):
        self.ui.inputPlot.clearPlot()
        self.ui.fourierPlot.clearPlot()
        self.ui.combinedPlot.clearPlot()

    def resetColors(self):
        self.ui.inputPlot.resetColor()
        self.ui.fourierPlot.resetColor()
        self.ui.combinedPlot.resetColor()

    def drawInputPlot(self, t, data):
        self.ui.inputPlot.updatePlot(t, data)

    def drawFourierPlot(self, t, data):
        self.ui.fourierPlot.updatePlot(t, data)

    def drawCombinedPlot(self, t, data):
        self.ui.combinedPlot.updatePlot(t, data)
