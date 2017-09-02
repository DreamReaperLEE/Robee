from datetime import datetime
from time import sleep

# seconds in one day
SECONDS_PER_DAY = 24 * 60 * 60


# set when would you run the function again
def dosleep(text):
    curTime = datetime.now()
    desTime = curTime.replace(hour=text, minute=0, second=0, microsecond=0)
    delta = curTime - desTime
    skipSeconds = SECONDS_PER_DAY - delta.total_seconds()
    sleep(skipSeconds)
