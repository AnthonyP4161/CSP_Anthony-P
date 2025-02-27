#Anthony Petersen, Time Of Day
import time

#first instance of time in programming
first_time  = time.gmtime()

#get time in seconds
current = time.time()
#print(seconds_time) #seconds since Janurary 1 1970

#current date and time the normal way
now = time.ctime(current)
#print(date)

#part of the time
local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour
minute = local_time.tm_min
seconds = local_time.tm_sec
print(day)