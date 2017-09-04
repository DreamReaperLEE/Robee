from datetime import datetime
from time import sleep

# seconds in one day
SECONDS_PER_DAY = 24 * 60 * 60


# set when would you run the function again
def dosleep(text):
    curTime = datetime.now()
    nextday = curTime.day + 1
    desTime = curTime.replace(day=nextday, hour=text, minute=0, second=0, microsecond=0)
    delta = desTime - curTime
    skipSeconds = delta.total_seconds()
    sleep(skipSeconds)
