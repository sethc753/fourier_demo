"""This module defines the class for the application controller"""
from fourier_view import FourierView
from fourier_model import FourierModel
import sys
from PyQt5 import QtWidgets

# TODO: Add duty cycle functionality
# TODO: Add reverse sawtooth input
# TODO: Plot formatting

class FourierController:
    """Class to manage the application logic and link the application's model and view objects"""
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.view = FourierView()
        self.model = FourierModel()
        self.connectSignals()
        self.radio_buttons = ('Square', 'Triangle', 'Sawtooth')
        self.model.recalculate()
        self.updatePlots()

    def connectSignals(self):
        """Connect the signals from the UI to the application logic"""
        # Radio Buttons (use lambda to pass argument)
        self.view.ui.squareBtn.clicked.connect(self.updateModel)
        self.view.ui.triangleBtn.clicked.connect(self.updateModel)
        self.view.ui.sawtoothBtn.clicked.connect(self.updateModel)

        # Input Values
        self.view.ui.ampSelect.valueChanged.connect(self.updateModel)
        self.view.ui.freqSelect.valueChanged.connect(self.updateModel)
        self.view.ui.vertSelect.valueChanged.connect(self.updateModel)
        self.view.ui.termSelect.valueChanged.connect(self.updateModel)
        self.view.ui.phaseSelect.valueChanged.connect(self.updateModel)

        # Check Buttons
        self.view.ui.showInputSelect.toggled.connect(self.updateModel)

    def updateModel(self):
        """Perform all steps to recalculate values and update plots"""
        self.modifyInputs()
        self.model.recalculate()
        self.updatePlots()

    def modifyInputs(self):
        """Apply user inputs values to stored values in model"""
        # Changing the radio button selection requires additional logic to determine the new selection
        if self.app.sender().text() in self.radio_buttons:
            self.model.radio_select = self.app.sender().text()
        # Update all other values based on their current state
        self.model.amp = self.view.ui.ampSelect.value()
        self.model.freq = self.view.ui.freqSelect.value()
        self.model.v_shift = self.view.ui.vertSelect.value()
        self.model.phase_deg = self.view.ui.phaseSelect.value()
        self.model.terms = self.view.ui.termSelect.value()
        self.model.input_toggle = self.view.ui.showInputSelect.isChecked()

    def updatePlots(self):
        """Instructs the view object to update all plots"""
        # Clear old data and plot new data. Plot color scheme is reset so colors remain consistent
        self.view.clearPlots()
        self.view.resetColors()
        self.view.drawInputPlot(self.model.t, self.model.input_wave)

        for plot in self.model.series:
            self.view.drawFourierPlot(self.model.t, plot)

        self.view.drawCombinedPlot(self.model.t, self.model.comp_series)

        if self.model.input_toggle:
            self.view.drawCombinedPlot(self.model.t, self.model.input_wave)

    def run(self):
        """GUI event loop"""
        return self.app.exec()


a = FourierController()
sys.exit(a.run())
