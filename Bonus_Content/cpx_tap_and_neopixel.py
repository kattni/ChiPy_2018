from adafruit_circuitplayground.express import cpx

cpx.detect_taps = 2
pixel_number = 0

while True:
    if cpx.tapped:
        print("Tap detected!")
        cpx.pixels.fill((0, 0, 0))
        cpx.pixels[pixel_number] = (0, 0, 50)
        pixel_number += 1
        if pixel_number >= 10:
            pixel_number = 0
