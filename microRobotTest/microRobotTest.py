import m
import machine
from machine import ADC,DAC,Pin,PWM,I2C
# from SSD1306 import SSD1306
from microRobotLib import MICROROBOT
import math
import time

i2c = I2C(scl=Pin(m.SCL),sda=Pin(m.SDA), freq=10000)

microRobot = MICROROBOT(i2c)

'''
d = SSD1306()
d.poweron()
d.init_display()
'''


tempValue=""

# d.clear()
# d._row = 0
# d._col = 0
# d.p_string(tempValue)
# d.display()
# time.sleep(0.1)


def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = value / 256.0
    return temp


led1 = Pin(m.D4, Pin.OUT)
led2 = Pin(m.D5, Pin.OUT)


adc = machine.ADC(Pin(m.A6))
a6Value=0

button = Pin(m.A7, Pin.IN, Pin.PULL_UP)

'''
for i in range(1, 5):
    microRobot.motorInit(i)
#     microRobot.setMode(i, microRobot.MODE_OPEN) #motor set to open mode
    microRobot.setMode(i, microRobot.MODE_SPEED) #motor set to speed mode
    microRobot.setRatio(i, 60)
    microRobot.setResolution(i, 12)
    microRobot.setSpeed(i, 0)
'''




# servo init
for i in range(1, 5):
    microRobot.digitalWrite(i, microRobot.LOW)

# address=i2c.scan()
# add=i2c.scan()[0]
# for addr in address:
#     print ("Hex = 0x%2x" % (addr))

for pos in range(1, 180):
    microRobot.servoWrite(0, pos)
    time.sleep(0.01)
for pos in range(180, 0, -1):
    microRobot.servoWrite(0, pos)
    time.sleep(0.01)
'''

#motorPro
for i in range(1, 5):
    microRobot.setSpeed(i, 200)
time.sleep(2)
print(microRobot.getSpeed(1))
print(microRobot.getSpeed(2))
for i in range(1, 5):
    microRobot.setSpeed(i, microRobot.BRAKE)
time.sleep(2)
for i in range(1, 5):
    microRobot.setSpeed(i, -200)
time.sleep(2)
print(microRobot.getSpeed(1))
print(microRobot.getSpeed(2))
for i in range(1, 5):
#     microRobot.setSpeed(i, microRobot.FREE)
    microRobot.setSpeed(i, microRobot.BRAKE)
time.sleep(2)


music=PWM(Pin(m.D6))
music.duty(512)


while(True):
    #button A6
    a6Value=adc.read()
    if(a6Value<50):
        music.init()
        music.freq(400)
        led1.value(True)
    elif(a6Value>4000):
        music.deinit()
        led1.value(False)

    #button A7
#     print(button.value())
    if not button.value():
        led2.value(True)
    else:
        led2.value(False)


    #LM75
#     data = bytearray(2)
#     i2c.readfrom_mem_into(0x48, 0, data)
#     tempValue=str(temp_c(data))
# #     print(tempValue)

    #OLED
    d.clear()
    d._row = 0
    d._col = 0
    d.p_string(tempValue)
    d.display()
    

    time.sleep(0.1)

'''