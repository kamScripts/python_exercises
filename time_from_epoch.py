import time

t=time.time()
print(t)

SECONDS_IN_MINUTES = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTES
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR

print(SECONDS_IN_MINUTES, SECONDS_IN_HOUR, SECONDS_IN_DAY)

days_since_epoch_one = int(t // SECONDS_IN_DAY)

print('days since epoch one (1-1-1970): ', days_since_epoch_one)

