import math, board, busio, time
import adafruit_ads1x15.ads1115 as ads

i2c = busio.I2C(board.SCL, board.SDA)
ads = ads.ADS1115(i2c)
from adafruit_ads1x15.analog_in import AnalogIn
pressure_sensor = AnalogIn(ads, 0)

while True:     # loop to constantly check voltage input
    voltage = pressure_sensor.voltage

    print(f"Voltage: {voltage:.3f} V")
    time.sleep(0.5)

#    Voltage to Pressure

def voltage_to_pressure(voltage):
    pressure = (voltage - 2.713) * SENSOR_GAIN
    return pressure

#    Bernoulli's Equation

rho = 1.225
delta_p = voltage_to_pressure(voltage) # h in Bernoulli's Eq
airspd_Pa = math.sqrt((2 * h) / rho)
airspd_kPa = airspd_Pa * 1000

