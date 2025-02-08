import board
import busio
import adafruit_sht31

class SHT31Sensor:
    def __init__(self):
        # Inicjalizacja I2C
        self.i2c = busio.I2C(board.SCL, board.SDA)
        # Inicjalizacja sensora SHT31
        self.sensor = adafruit_sht31.SHT31D(self.i2c)

    def read_temperature(self):
        return self.sensor.temperature

    def read_humidity(self):
        return self.sensor.relative_humidity

    def is_heater_on(self):
        return self.sensor.heater

    def set_heater(self, state):
        self.sensor.heater = state

if __name__ == "__main__":
    sht31 = SHT31Sensor()
    temperature = sht31.read_temperature()
    humidity = sht31.read_humidity()

    print(f"Temperatura: {temperature:.2f} °C")
    print(f"Wilgotność: {humidity:.2f} %")

    if sht31.is_heater_on():
        print("Grzałka jest włączona")
    else:
        print("Grzałka jest wyłączona")

    # Włączanie grzałki
    sht31.set_heater(True)
