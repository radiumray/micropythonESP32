import m 
import time
from machine import Pin,I2C
#from microRobotLib.microRobotLib import MICROROBOT
from microRobotLib import MICROROBOT

microRobot = MICROROBOT(I2C(scl=Pin(m.SCL),sda=Pin(m.SDA), freq=10000))

# microRobot.robotScan()

for i in range(1, 5):
    microRobot.motorInit(i)
    microRobot.setMode(i, microRobot.MODE_OPEN) #motor set to open mode
    microRobot.setSpeed(i, 0)

while(True):

    for i in range(1, 5):
        microRobot.setSpeed(i, 100)
    time.sleep(2)
    for i in range(1, 5):
        microRobot.setSpeed(i, microRobot.BRAKE)
    time.sleep(2)
    for i in range(1, 5):
        microRobot.setSpeed(i, -100)
    time.sleep(2)
    for i in range(1, 5):
        microRobot.setSpeed(i, microRobot.FREE)
    time.sleep(2)

