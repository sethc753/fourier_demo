import numpy as np
from scipy import signal


class FourierModel:
    """Class to manage the application's data and calculations"""
    def __init__(self):
        self.start = 0
        self.end = 2
        self.samples = 1000
        self.radio_select = 'Square'
        self.freq = 5
        self.omega = 0
        self.phase_deg = 0
        self.phase_shift = 0
        self.v_shift = 0
        self.amp = 1
        self.terms = 3
        self.series = []
        self.comp_series = []
        self.input_toggle = False
        self.t = self.calculateTime()
        self.input_wave = signal.square(2 * np.pi * self.freq * self.t)
        self.recalculate()

    def recalculate(self):
        self.omega = self.freq * 2 * np.pi
        self.phase_shift = (self.phase_deg * 2 * np.pi / 360) / self.omega
        self.calculateTime()
        self.calculateInputFunction()
        self.calculateFourierSeries()

    def calculateTime(self):
        """Calculate time range"""
        return np.linspace(start=self.start, stop=self.end, num=self.samples, endpoint=False)

    def calculateInputFunction(self):
        """Calculates the values of the input function based on user parameters"""
        # Generate the unmodified wave type based on radio button selection
        if self.radio_select == 'Square':
            self.input_wave = signal.square(self.omega * self.t, 0.5)
        elif self.radio_select == 'Triangle':
            self.input_wave = signal.sawtooth(self.omega * self.t, width=0.5)
        elif self.radio_select == 'Sawtooth':
            self.input_wave = signal.sawtooth(self.omega * self.t)

        # Apply the user parameters to the unmodified input function
        self.input_wave = [n * self.amp for n in self.input_wave]
        self.input_wave = [n + self.v_shift for n in self.input_wave]

    def calculateFourierSeries(self):
        waveform = self.radio_select
        self.series.clear()
        if self.v_shift != 0:
            term = self.samples * [self.v_shift]
            self.series.append(term)

        self.comp_series = [0] * self.samples
        if waveform == 'Square':
            n = 1
            for i in range(self.terms):
                term = self.amp * (4 / (n * np.pi)) * np.sin(n * (self.t - self.phase_shift) * self.omega)
                self.series.append(term)
                n += 2
        elif waveform == 'Triangle':
            n = 1
            for i in range(self.terms):
                an = (8 * pow(-1,  ((n - 1) / 2))) / (pow(n, 2) * pow(np.pi, 2))
                term = an * np.sin((self.t - self.phase_shift - (1 / (4 * self.freq))) * n * self.omega)
                self.series.append(term)
                n += 2
        elif waveform == 'Sawtooth':
            for i in range(1, self.terms + 1):
                term = self.amp * 2 * pow(-1, i) * np.sin(i * self.omega * (self.t - self.phase_shift -
                                                                            (1 / (2 * self.freq)))) / (-i * np.pi)
                self.series.append(term)

        self.comp_series = [sum(n) for n in zip(*self.series)]
