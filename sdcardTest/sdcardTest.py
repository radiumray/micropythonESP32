import mfrom machine import SPI,Pinimport sdcardimport os

spi = SPI(baudrate=100000, polarity=1, phase=0, sck=Pin(m.D13), mosi=Pin(m.D11), miso=Pin(m.D12))
sd = sdcard.SDCard(spi, Pin(m.D7))os.mount(sd,"/sd")fd=open('/sd/microduino.txt','rw')fd.write('hello microduino')fd.seek(0)print(fd.read())fd.close()print(os.listdir('/sd'))os.umount("/sd")