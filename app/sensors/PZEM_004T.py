import pymodbus
import math
import time
from pymodbus import FramerType
from pymodbus.client import ModbusSerialClient

class PZEM_004TSensors:
    voltage = 0
    current = 0
    power = 0
    energy = 0
    frequency = 0    

    def __init__(self, port='/dev/ttyAMA0', baudrate=9600, timeout=1):
        self.client = ModbusSerialClient(
            port=port,
            framer=FramerType.RTU,            
            baudrate=baudrate,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=timeout            
        )
        self.connection = self.client.connect()
        
        if self.connection:            
            print("Connected to PZEM-004T")
        else:
            print("Failed to connect to PZEM-004T")

    def reset_energy(self):
        data = [0x01, 0x42, 0x80, 0x11]
        self.client.send(data)

    def read_data(self):
        result = self.client.read_input_registers(0x00, count=10, slave=1)
        self.voltage = self.calc(result.registers[0:1], 10)
        self.current = self.calc(result.registers[1:3], 1000)
        self.power = self.calc(result.registers[3:5], 10)
        self.energy = self.calc(result.registers[5:7], 1)
        self.frequency = self.calc(result.registers[7:8], 10)
        self.power_factor = self.calc(result.registers[8:9], 100)
        self.alarm = self.calc(result.registers[9:10], 1)

    def get_voltage(self):
        return self.voltage

    def set_voltage(self, value):
        self.voltage = value

    def get_current(self):
        return self.current

    def set_current(self, value):
        self.current = value

    def get_power(self):
        return self.power

    def set_power(self, value):
        self.power = value

    def get_energy(self):
        return self.energy

    def set_energy(self, value):
        self.energy = value

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, value):
        self.frequency = value

    def get_power_factor(self):
        return self.power_factor

    def set_power_factor(self, value):
        self.power_factor = value

    def get_alarm(self):
        return self.alarm

    def set_alarm(self, value):
        self.alarm = value

    @staticmethod
    def calc(registers, factor):
        format = '%%0.%df' % int(math.ceil(math.log10(factor)))
        if len(registers) == 1:
            return format % ((1.0 * registers[0]) / factor)
        elif len(registers) == 2:
            return format % (((1.0 * registers[1] * 65535) + (1.0 * registers[0])) / factor)
