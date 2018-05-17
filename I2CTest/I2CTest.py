import m
from machine import Pin,I2C
import time

def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = value / 256.0
    return temp

i2c = I2C(scl=Pin(m.SCL),sda=Pin(m.SDA), freq=10000)

address=i2c.scan()
add=i2c.scan()[0]
for addr in address:
    print ("Hex = 0x%2x" % (addr))


# while True:
#   data = bytearray(2)
#   i2c.readfrom_mem_into(add, 0, data)
#   print(temp_c(data))
#   time.sleep(1)


