# Connect the potentiometer to A0 then rotate to see the number of pixels lit up change!
# REQUIRES LOADING simpleio.mpy onto your CIRCUITPY drive
import time
import board
from adafruit_circuitplayground.express import cpx
import simpleio
import analogio

cpx.pixels.auto_write = False
cpx.pixels.brightness = 0.3
potentiometer = analogio.AnalogIn(board.A0)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    # Potentiometer voltage value remapped to pixel position
    cpx_peak = simpleio.map_range(get_voltage(potentiometer), 0, 3.3, 0, 10)

    for i in range(0, 10, 1):
        if i <= cpx_peak:
            cpx.pixels[i] = (0, 255, 255)
        else:
            cpx.pixels[i] = (0, 0, 0)
    cpx.pixels.show()
    time.sleep(0.05)
