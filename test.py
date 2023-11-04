import RPi.GPIO as GPIO
import time

base = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(base, GPIO.OUT)

while(1):
    GPIO.output(base, GPIO.HIGH)
    print("ON")
    time.sleep(0.8)
    GPIO.output(base, GPIO.LOW)
    print("OFF")
    time.sleep(2)
    