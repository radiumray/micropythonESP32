import m
import time
import machine, neopixel

def demo(np, r, b, g):
    n = np.n
    np.fill((0,0,0))
    np.write()
    time.sleep_ms(1000)

    for i in range(n):
        np[i] = ( r,b,g )
        np.write()
        time.sleep_ms(100)

def run(t):
    np = neopixel.NeoPixel(machine.Pin(4), 10, timing = t )
    demo(np, 255, 0, 0)
    demo(np, 0, 255, 0)
    demo(np, 0, 0, 255)
    demo(np, 255, 255, 255)
    np.fill((0, 0, 0))
    np.write()



np = neopixel.NeoPixel(machine.Pin(m.D8), 10, timing = 1 )
demo(np, 255, 0, 0)
