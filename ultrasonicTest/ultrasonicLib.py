import time
from array import array

class ULTRASONIC:
    i2c = []

    ULTRASONIC_ADDR_1=0X31
    ULTRASONIC_ADDR_2=0X32
    ULTRASONIC_ADDR_3=0X33
    ULTRASONIC_ADDR_4=0X34

    ULTRA_VERSION=3

    ADDR16_DISTANCE=0
    ADDR8_VERSION=2
    ADDR8_BLIND=3
    
    def __init__(self, _i2c):
        self.i2c = _i2c

    def getDistance(self):
        self.i2c.writeto(self.ULTRASONIC_ADDR_1, b'0')
        data = bytearray(2)
        data=self.i2c.readfrom(self.ULTRASONIC_ADDR_1, 2)
        distance=(data[0]<<8)+data[1]
        return distance
