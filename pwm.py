import RPi.GPIO as GPIO
import datetime
import time
from time import sleep

led = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
ledFade = GPIO.PWM(led, 1000)
ledFade.start(0)

while True:
    t = time.localtime(time.time())
    ledFade.ChangeDutyCycle((5/3)*(t.tm_sec))
    sleep(0.05)