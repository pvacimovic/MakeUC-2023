import time
from time import sleep
import pwm

targetHour = int(input("Enter the Hour when you want to wake up (24hr): ")) #5 pm
targetMinute = int(input("Enter the Minute when you want to wake up: ")) #5 pm
activated = 0
print(f'Target Hour - Target Minute: {targetHour} - {targetMinute} ')
while(True):
    t = time.localtime(time.time())
    print(f'Time:{int(t.tm_hour)%12}:{t.tm_min}')
    sleep(.5)
    if((t.tm_hour == targetHour) and (targetMinute -1 == t.tm_min) and not activated):
        activated = 1
        print("LIGHTS TURNING ON")
        pwm.lightingUp()
    
    