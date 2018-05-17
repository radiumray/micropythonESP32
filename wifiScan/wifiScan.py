from machine import Pin
import network
import time

ssid=bytearray('Microduino_SS')
wifiGood=50

led4 = Pin(32, Pin.OUT)
led5 = Pin(33, Pin.OUT)

count=2
rssi0=wifiGood
rssi1=wifiGood

for i in range(5):
    led4.value(True)
    led5.value(False)
    time.sleep_ms(100)
    led4.value(False)
    led5.value(True)
    time.sleep_ms(100)
    
led4.value(False)
led5.value(False)

station = network.WLAN(network.STA_IF)
station.active(True)

while(True):
    nets=station.scan()
    if(count==2):
        count=0

    for net in nets:
        print("ssid: %s rssi: %d "%(net[0],net[3]))
        if(net[0]==ssid):
            if(count==0):
                rssi0=net[3]
            if(count==1):
                rssi1=net[3]
            rssi=min(abs(rssi0),abs(rssi1))
            print(rssi)
            if(rssi<wifiGood):
                led5.value(True)
                led4.value(False)
            else:
                led4.value(True)
                led5.value(False)
            print("--------")
            count=count+1




# while(True):
#     nets=station.scan()
#     for net in nets:
#         print("ssid: %s rssi: %d "%(net[0],net[3]))
#         if(net[0]==md):
#             if(abs(net[3])<wifiGood):
#                 led5.value(True)
#             else:
#                 led5.value(False)
#             print("--------")