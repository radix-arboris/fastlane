from datetime import dt
from playsound import playsound

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
  if isNowInTimePeriod(dt.time(3,45), dt.time(3,47), dt.datetime.now().time())
    playsound("Alarm1.mp3")
  sleep(30)
