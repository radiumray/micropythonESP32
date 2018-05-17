import m 
import time
from machine import Pin,I2C
from ultrasonicLib import ULTRASONIC

ultrasonic = ULTRASONIC(I2C(scl=Pin(m.SCL),sda=Pin(m.SDA), freq=10000))

while(True):
    distance = ultrasonic.getDistance()
    print(distance)
    time.sleep(1)
