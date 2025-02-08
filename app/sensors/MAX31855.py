import spidev

class MAX31855Sensor:
    corrections = {
        25: 100,
        300: 200,
        500: 200
    }

    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 1)
        self.spi.max_speed_hz = 50000

    def read_max31855(self):
        raw_data = self.spi.xfer2([0x00, 0x00, 0x00, 0x00])
        temp = ((raw_data[0] << 8) | raw_data[1]) >> 3
        if temp & 0x800:
            temp -= 1 << 11

            for key in sorted(self.corrections.keys(), reverse=True):
                if temp > key:
                    temp += self.corrections[key]
                    break
        return temp * 0.25
    
