import time 

def get_current_time():
    """Returns the current time in seconds since the epoch."""
    return time.time()

print(2)
time.sleep(2)
print(3)

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)
