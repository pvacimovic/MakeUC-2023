import time
from time import sleep
from datetime import datetime
import pytz
#target_timezone = pytz.timezone('US/Eastern')#('America/New_York')  # Replace with your desired timezone
#datetime.now(target_timezone)
datetime.now()

while(True):
    t = datetime.utcnow()
    print(f'Hour:Minute:Second : {t.hour} - {t.minute} ')
    sleep(1)