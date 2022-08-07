import RPi.GPIO as GPIO
from time import sleep


pin = 11
up = 5
down = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
pwm=GPIO.PWM(pin, 50)

class Light:

    def init(pin):
        pwm.start(0)

    def on(pin):
        pwm.ChangeDutyCycle(up)

    def off(pin):
        pwm.ChangeDutyCycle(down)

    def blink(pin):
        pwm.ChangeDutyCycle(up)
        sleep(1)
        pwm.ChangeDutyCycle(down)
        sleep(1)

    def cleanup(pin):
        pwm.stop()
        GPIO.cleanup()
