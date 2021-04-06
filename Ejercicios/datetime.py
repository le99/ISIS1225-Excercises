#https://docs.python.org/3/library/datetime.html
#Format Codes, tabla para fomatos

import datetime

dateWithTime = datetime.datetime.strptime('2021/03/01', '%Y/%m/%d')
date = datetime.datetime.strptime('2021/03/01', '%Y/%m/%d').date()
now = datetime.datetime.now()

print("datetime a String:")
print(dateWithTime.strftime("%d/%m/%y"))

print()
print("date a String:")
print(date.strftime("%d/%m/%y"))

print("Comparaciones")
print(dateWithTime < now)
d = datetime.datetime(date.year, date.month, date.day)
print(d <= now)

print()
print("Tiempo transcurrido")
diff = now - dateWithTime
print(diff)
print(diff.total_seconds())


import sys
print()
print("datetime es mas grande que date")
print(sys.getsizeof(dateWithTime))
print(sys.getsizeof(date))