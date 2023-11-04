import time
from time import sleep
import pwm
from datetime import datetime
import pytz

targetHour = int(input("Enter the Hour when you want to wake up (24hr): ")) #5 pm
targetMinute = int(input("Enter the Minute when you want to wake up: ")) #5 pm
activated = 0

target_timezone = pytz.timezone('US/Eastern')#('America/New_York')  # Replace with your desired timezone
datetime.now(target_timezone)

print(f'Target Hour - Target Minute: {targetHour}:{targetMinute} ')
while(True):
    t = datetime.now()
    print(f'Time:{int(t.hour)}:{t.minute}')
    sleep(.5)
    if((t.hour == targetHour) and (targetMinute -1 == t.minute) and not activated):
        activated = 1
        print("LIGHTS TURNING ON")
        pwm.lightingUp()
    
    