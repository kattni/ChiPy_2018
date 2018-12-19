# Shake your Circuit Playground Express to see the little red LED turn on.
import time
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.shake():
        print("Shake detected!")
        cpx.red_led = True
        time.sleep(0.1)
    else:
        cpx.red_led = False
