import math, board, busio 
import adafruit_ads1x15.ads1115 as ADS

pressure_sensor = 0 # initialize A0 on ads1115

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
from adafruit_ads1x15.analog_in import AnalogIn
pressure_sensor = AnalogIn(ads, 0)
voltage = pressure_sensor.voltage

while True:
    print(f"Voltage: {pressure_sensor.voltage:.3f} V")
    time.sleep(0.5)