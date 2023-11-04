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
    dutyVal = (5/6)*(t.tm_sec)
    print(dutyVal)
    ledFade.ChangeDutyCycle(dutyVal)
    sleep(0.05)