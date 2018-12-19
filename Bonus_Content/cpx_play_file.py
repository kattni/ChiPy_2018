from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        cpx.play_file("coin.wav")
    elif cpx.button_b:
        cpx.play_file("eep.wav")
