from time import sleep
import pwm
from datetime import datetime
import pytz
import time

targetHour = int(input("Enter the Hour when you want to wake up (24hr): ")) #5 pm
targetMinute = int(input("Enter the Minute when you want to wake up: ")) #5 pm


#targetHour = if(targetMinute)
activated = 0

target_timezone = pytz.timezone('US/Eastern')#('America/New_York')  # Replace with your desired timezone
datetime.now(target_timezone)


print(f'Target HOUR - Target Minute: {targetHour}:{targetMinute} ')
print(f'TEST TIME:{((datetime.now()).hour)}:{(datetime.now()).minute}')

# print(f'Target HOUR - Target Minute: {(time.ctime())}:{targetMinute} ')
# print(f'TEST TIME:{((datetime.utcnow()).hour)}:{(datetime.utcnow()).minute}')
while(True):
    t = datetime.now()
    print(f'Time:{int(t.hour)}:{t.minute}')
    sleep(.5)
    if((t.hour == targetHour) and (targetMinute -1 == t.minute) and not activated):
        activated = 1
        print("LIGHTS TURNING ON")
        pwm.lightingUp()
    
 #   11hours 13 mins