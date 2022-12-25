import time
current_time = time.localtime()
hour = int(current_time.tm_hour)
minutes = int(current_time.tm_min)
seconds = int(current_time.tm_sec)

if (hour >= 5 and hour < 12):
    print("Good Morning Sir!")
elif (hour >= 12 and hour < 18):
    print("Good Afternoon Sir!")
elif (hour >= 18 and hour < 21):
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")
