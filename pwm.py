import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
import pytz

def lightingUp():
    led = 33
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led, GPIO.OUT)
    ledFade = GPIO.PWM(led, 1000)
    ledFade.start(0)
    target_timezone = pytz.timezone('US/Eastern')#('America/New_York')  # Replace with your desired timezone
    datetime.now(target_timezone)

    wakeUpTime = 60
    deltaLvl = 100/wakeUpTime
    
    while True:
        t = datetime.now()
        for i in range(wakeUpTime+1):
            dutyVal = (deltaLvl)*(i)
            #print(f'Hour:Minute:Second : {t.hour}:{t.minute}:{t.second}')
            if (dutyVal%1 == 0): print(dutyVal)
            ledFade.ChangeDutyCycle(dutyVal)
            sleep(1)
        sleep(wakeUpTime)

        for i in range(wakeUpTime/2):
            if(i%2==0):
                dutyVal=100
            else:
                dutyVal=0
            sleep(1)
        break
if __name__ == '__main__':
    # test1.py executed as script
    # do something
    lightingUp()