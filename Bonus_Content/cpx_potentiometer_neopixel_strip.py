# Connect the potentiometer to A0 and the NeoPixel strip to A7.
# Rotate the potentiometer knob and watch the number of pixels lit up change!
# REQUIRES LOADING simpleio.mpy onto your CIRCUITPY drive
import time
import board
import simpleio
import analogio
import neopixel

strip = neopixel.NeoPixel(board.A7, 30, auto_write=False)
strip.brightness = 0.3
potentiometer = analogio.AnalogIn(board.A0)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    # Potentiometer voltage value remapped to pixel position
    strip_peak = simpleio.map_range(get_voltage(potentiometer), 0, 3.3, 0, 30)

    for j in range(0, 30, 1):
        if j <= strip_peak:
            strip[j] = (0, 255, 255)
        else:
            strip[j] = (0, 0, 0)

    strip.show()
    time.sleep(0.05)
