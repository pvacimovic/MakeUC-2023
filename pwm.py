import RPi.GPIO as GPIO
import datetime
import time
from time import sleep

def lightingUp():
    led = 33
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led, GPIO.OUT)
    ledFade = GPIO.PWM(led, 1000)
    ledFade.start(0)

    while True:
        t = time.localtime(time.time())
        dutyVal = (5/3)*(t.tm_sec)
        if (dutyVal%1 == 0): print(dutyVal)
        ledFade.ChangeDutyCycle(dutyVal)
        sleep(0.5)
if __name__ == '__main__':
    # test1.py executed as script
    # do something
    lightingUp()