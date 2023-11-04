import RPi.GPIO as GPIO
from time import sleep

led = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
ledFade = GPIO.PWM(led, 1000)
ledFade.start(0)

while True:
    for i in range(0,101, 5):
        ledFade.ChangeDutyCycle(i)
        sleep(0.05)