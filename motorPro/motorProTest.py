import m 
import time
from machine import Pin,I2C
from microRobotLib import MICROROBOT

microRobot = MICROROBOT(I2C(scl=Pin(m.SCL),sda=Pin(m.SDA), freq=10000))

# microRobot.robotScan()

for i in range(1, 5):
    microRobot.motorInit(i)
#     microRobot.setMode(i, microRobot.MODE_OPEN) #motor set to open mode
    microRobot.setMode(i, microRobot.MODE_SPEED) #motor set to speed mode
    microRobot.setRatio(i, 60)
    microRobot.setResolution(i, 12)
    microRobot.setSpeed(i, 0)
    
while(True):

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
        microRobot.setSpeed(i, microRobot.BRAKE)
    time.sleep(2)

