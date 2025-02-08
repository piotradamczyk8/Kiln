from Triac import Triac
from sensors.ZCD import ZeroCrossDetector
from sensors import PZEM_004T

class PowerController:
    def __init__(self, triac_pin):
        self.triac = Triac(triac_pin)

    def turn_on(self):
        self.triac.turn_on()

    def turn_off(self):
        self.triac.turn_off()

    def set_power_level(self, level):
        self.triac.set_power_level(level)