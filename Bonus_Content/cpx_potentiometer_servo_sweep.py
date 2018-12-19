# Connect the potentiometer to A0 and the servo to A1.
# Rotate the potentiometer knob to watch the servo rotate!
import board
import simpleio
import analogio
import pulseio
from adafruit_motor import servo

potentiometer = analogio.AnalogIn(board.A0)
pwm = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(pwm)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    # Potentiometer voltage value remapped to servo angle
    servo_sweep = simpleio.map_range(get_voltage(potentiometer), 0, 3.3, 0, 180)
    servo.angle = servo_sweep
