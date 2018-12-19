from adafruit_circuitplayground.express import cpx

while True:
    if cpx.shake():
        print("Shake detected!")
        cpx.red_led = True
    else:
        cpx.red_led = False
