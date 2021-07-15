import datetime
import time

while True:
    time.sleep(1)
    print(datetime.datetime.now().strftime('%M%S'))