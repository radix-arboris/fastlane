'''
Todo:

- play sound over bluetooth
'''

import random
from datetime import dt
from playsound import playsound
from time import sleep
from lightswitch import Light

alarm_selection=[
    'alarms/pumped_kicks.mp4' #1
]



def isNowInTimePeriod(startTime, endTime, nowTime): 
    if startTime < endTime: 
        return nowTime >= startTime and nowTime <= endTime 
    else: 
        #Over midnight: 
        return nowTime >= startTime or nowTime <= endTime 

#normal example: 
#isNowInTimePeriod(dt.time(13,45), dt.time(21,30), dt.datetime.now().time())

#over midnight example: 
#isNowInTimePeriod(dt.time(20,30), dt.time(1,30), dt.datetime.now().time())

def UtcNow():
    now = dt.datetime.utcnow()
    return now

while True:

  if isNowInTimePeriod(dt.time(3,45), dt.time(3,47), dt.datetime.now().time()):
    random_index = random.randint(0, len(alarm_selection)-1)
    alarm = alarm_selection[random_index]
    playsound(alarm)
    sleep(10)
    Light.on()
    sleep(10)
    Light.off()
    sleep(10)
    Light.blink()
    sleep(10)
    sleep(10)
    Light.cleanup()
    sleep(10)
