import time
import datetime

a = datetime.datetime.now()
b = datetime.datetime.now()
print(b)
print(b - a < datetime.timedelta(seconds=1))
# print(datetime.datetime.ctime())