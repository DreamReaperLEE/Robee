from datetime import datetime
from time import sleep

SECONDS_PER_DAY = 24 * 60 * 60
def dosleep(text):
    curTime = datetime.now()
    desTime = curTime.replace(hour=text, minute=0, second=0, microsecond=0)
    delta = curTime - desTime
    skipSeconds = SECONDS_PER_DAY - delta.total_seconds()
    print "Next day must sleep %d seconds" % skipSeconds
    sleep(skipSeconds)