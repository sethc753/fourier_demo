"""A module to promote a QWidget to a MatPlotLib plot."""

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt

class MplWidget(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = plt.figure()
        super().__init__(fig)
        self.ax = fig.add_subplot()

    def updatePlot(self, t, data):
        self.ax.plot(t, data)
        self.ax.axes.set_xlim(auto=True)
        self.draw()

    def clearPlot(self):
        self.ax.lines.clear()
        self.draw()

    def resetColor(self):
        self.ax.set_prop_cycle(None)