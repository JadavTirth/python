import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
current_hour = int(time.strftime('%H'))
mor = 5
aft = 12
eve = 18
nig = 21


if 5 <= current_hour < 12:
    print("Good morning")
elif 12 <= current_hour < 18:
    print("Good afternoon")
elif 18 <= current_hour < 21:
    print("Good evening")
else:
    print("Good night")