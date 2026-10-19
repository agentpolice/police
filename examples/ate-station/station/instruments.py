"""Simulated bench: DMM, counter and a 16-channel switch. Replace with pyvisa on a real station."""
import random

# a real board lot: unit 15 has a weak 3.3V regulator (3.452 V, above the 3.40 V limit)
_DEFECT = {(15, "VCC_3V3"): 3.452}
_NOMINAL = {"VCC_3V3": 3.300, "VIN_12V": 12.01, "VDD_CORE": 1.200, "I_STBY": 8.4,
            "CLK_FREQ": 25.000, "RST_HIGH": 3.21, "RIPPLE_3V3": 14.2}


class Bench:
    def __init__(self, seed=7):
        self._rnd = random.Random(seed)
        self.channel = None

    def route(self, ch):
        self.channel = ch

    def measure(self, name):
        if (self.channel, name) in _DEFECT:
            return _DEFECT[(self.channel, name)]
        v = _NOMINAL[name]
        return round(v + self._rnd.uniform(-0.004, 0.004) * max(1.0, v / 10), 4)
