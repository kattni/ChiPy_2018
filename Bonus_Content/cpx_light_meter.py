# Shine a light on your phone to watch the LEDs show light levels increase and decrease!
# REQUIRES LOADING simpleio.mpy onto your CIRCUITPY drive
import time
from adafruit_circuitplayground.express import cpx
import simpleio

cpx.pixels.auto_write = False
cpx.pixels.brightness = 0.3

while True:
    # Light value remapped to pixel position
    peak = simpleio.map_range(cpx.light, 0, 320, 0, 10)
    print(cpx.light)  # Raw light levels
    print(int(peak))  # Remapped light levels

    for i in range(0, 10, 1):
        if i <= peak:
            cpx.pixels[i] = (0, 255, 255)
        else:
            cpx.pixels[i] = (0, 0, 0)
    cpx.pixels.show()
    time.sleep(0.05)
