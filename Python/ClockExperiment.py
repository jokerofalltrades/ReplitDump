import datetime
times = []
def hourhand(seconds):
    return round((seconds%43200)/120,1)
def minutehand(seconds):
    return round(seconds%3600/10,1)
for i in range(86400):
    if hourhand(i) == minutehand(i):
        print(datetime.timedelta(seconds=i))
    elif hourhand(i)-180 == minutehand(i) or minutehand(i)-180 == hourhand(i):
        print(datetime.timedelta(seconds=i))
# Outcomes of this little experiment:
# Rounding angles to 1dp gives 3600 different values.
# 34 out of the 86400 second values had an hour and minute hand angle equal to or opposite to each other.
# This is less likely than we'd expect, as 34/86400 < 1/1800 (1800 is for the two distinct possiblities).
# Equal to on its own is 24/86400, which is exactly equal to what we'd expect.
# This means the minute hand and hour hand being exactly opposite is quite unlikely compared to what we'd expect.