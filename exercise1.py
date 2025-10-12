import time

while True:
    localtime = time.localtime()
    if localtime.tm_hour < 12:
        print("Good morning!")
    time.sleep(60)
