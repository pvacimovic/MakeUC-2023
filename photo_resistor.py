import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

rpin = 7 

while True:
    GPIO.setup(rpin, GPIO.OUT)
    GPIO.output(rpin, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(rpin, GPIO.IN)
    currentTime = time.time()
    diff = 0
    
    while(GPIO.input(rpin) == GPIO.LOW):
        diff  = time.time() - currentTime
        
    print(diff * 1000)
    # lower number diff means faster charging means less resistance - more light
    time.sleep(1)