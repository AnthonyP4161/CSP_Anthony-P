#Anthony Petersen, Time Of Day
import time
current = time.time()
local_time = time.localtime(current)
hour = local_time.tm_hour
if(hour >= 17):
    print("Good evening! \n")
elif(hour >= 12):
    print("Good afternoon! \n")
else:
    print("Good morning!")