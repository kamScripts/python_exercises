import time
import datetime
# seconds from epoch (1-1-1970 UTC) Uk summer time = +1h.
t=int(time.time())


#Convert time into seconds

SECONDS_IN_MINUTES = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTES
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR

print('localtime', time.localtime())
def time_since_epoch(seconds_from_epoch):
    """Calculate days from epoch (1-1-1970UTC)"""
    days_since_epoch = seconds_from_epoch // SECONDS_IN_DAY
    print('days since epoch one (1-1-1970 UTC): ', days_since_epoch)
    

#Remaining seconds in the day
def current_time_since_epoch(seconds_from_epoch, summerTime=True):
    """Calculate current time based on seconds since epoch"""
    reminder_from_days = seconds_from_epoch % SECONDS_IN_DAY
    hours = reminder_from_days // SECONDS_IN_HOUR
    if summerTime:
        hours+=1
    minutes = (reminder_from_days % SECONDS_IN_HOUR) // SECONDS_IN_MINUTES
    seconds = reminder_from_days % SECONDS_IN_MINUTES
    print(f'{hours}:{minutes}:{seconds}')


time_since_epoch(t)
current_time_since_epoch(t)