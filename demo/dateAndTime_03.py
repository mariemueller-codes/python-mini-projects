# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

# datetime module supplies classes for manipulating dates and times
# datetime.now(tz=None) returns the current local date and time
import datetime

presenttime = datetime.datetime.now()
print(" Current date and time : ")
print(presenttime.strftime("%Y-%m-%d %H:%M:%S"))
