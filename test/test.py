import m
from machine import ADC,Pinimport network
'''ap = network.WLAN(network.AP_IF)ap.active(True)ap.config(essid='rayESP32PythonAP')ap.config(authmode=3, password='microduino')



pinMap={
    'A0':Pin(m.A0, Pin.IN),
    'A1':Pin(m.A1, Pin.IN),
    'A2':Pin(m.A2, Pin.IN),
    'A3':Pin(m.A3, Pin.IN),
    #'A4':Pin(m.SDA, Pin.IN),
    #'A5':Pin(m.SCL, Pin.IN),
    'A6':Pin(m.A6, Pin.IN),
    'A7':Pin(m.A7, Pin.IN),
}

'''

pinMap={
    #'A0':Pin(m.A0),
    #'A1':Pin(m.A1),
    #'A2':Pin(m.A2),
    #'A3':Pin(m.A3),
    #'A4':Pin(m.SDA),
    #'A5':Pin(m.SCL),
    'A6':Pin(m.A6),
    'A7':Pin(m.A7),
}

#adc0=ADC(Pin(37))
#adc0=ADC(Pin(m.A6))

#sss=pinMap['A0']
#adc0=ADC(sss)
#adc0=ADC(pinMap['A0'])
#print(ADC(Pin(m.A6)).read())




#rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(key), pinMap[key].value()) for key in sorted(pinMap)]
#rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(key), ADC(pinMap[key]).read()) for key in sorted(pinMap)]

#print(rows)



'''html = """<!DOCTYPE html><html>    <head> <title>ESP32 Pins</title> </head>    <body> <h1>ESP32 Pins</h1>        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>    </body></html>""" import socketaddr = socket.getaddrinfo('0.0.0.0', 80)[0][-1] s = socket.socket()s.bind(addr)s.listen(1) print('listening on', addr) while True:    cl, addr = s.accept()    print('client connected from', addr)    cl_file = cl.makefile('rwb', 0)    while True:        line = cl_file.readline()        if not line or line == b'\r\n':            break    #rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    #rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(key), pinMap[key].value()) for key in sorted(pinMap)]
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(key), ADC(pinMap[key]).read()) for key in sorted(pinMap)]    response = html % '\n'.join(rows)    cl.send(response)    cl.close()'''