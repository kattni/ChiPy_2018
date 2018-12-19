from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.3

while True:
    if cpx.switch:
        print("Slide switch off!")
        cpx.pixels.fill((0, 0, 0))
        cpx.stop_tone()
        continue
    if cpx.touch_A1:
        print("Touched 1!")
        cpx.pixels.fill((255, 0, 0))
        cpx.start_tone(262)
    elif cpx.touch_A2:
        print("Touched 2!")
        cpx.pixels.fill((210, 45, 0))
        cpx.start_tone(294)
    elif cpx.touch_A3:
        print("Touched 3!")
        cpx.pixels.fill((155, 100, 0))
        cpx.start_tone(330)
    elif cpx.touch_A4:
        print("Touched 4!")
        cpx.pixels.fill((0, 255, 0))
        cpx.start_tone(349)
    elif cpx.touch_A5:
        print("Touched 5!")
        cpx.pixels.fill((0, 135, 125))
        cpx.start_tone(392)
# touch_A6 and touch_A7 are coded to allow for touching each for a note and both for a third note.
    elif cpx.touch_A6 and not cpx.touch_A7:
        print("Touched 6!")
        cpx.pixels.fill((0, 0, 255))
        cpx.start_tone(440)
    elif cpx.touch_A7 and not cpx.touch_A6:
        print("Touched 7!")
        cpx.pixels.fill((100, 0, 155))
        cpx.start_tone(494)
# There are seven capacitive touch pads - the next block allows for a full 8 note octave.
# Touch both A6 and A7 together to play the last note.
    elif cpx.touch_A6 and cpx.touch_A7:
        print("Touched '8'!")
        cpx.pixels.fill((200, 0, 55))
        cpx.start_tone(523)
    else:
        cpx.stop_tone()
        cpx.pixels.fill((0, 0, 0))
