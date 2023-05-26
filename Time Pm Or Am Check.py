import time
hour = int(time.strftime('%H'))
# print(hour)

if hour >= 0 and hour < 12:
     print(hour, "is Am")
elif hour >=12 and hour < 23:
    print(hour,"is Pm")