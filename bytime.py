from datetime import datetime
from time import sleep

# seconds in one day
SECONDS_PER_DAY = 24 * 60 * 60


# set when would you run the function again
def dosleep(text):
    while 1:
        curTime = datetime.now()
        cur= curTime.hour
        cur=str(cur)
        if text==cur:
            return
        else:
            sleep(3600)