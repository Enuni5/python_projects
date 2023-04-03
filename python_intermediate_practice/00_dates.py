### Working with Dates ###

from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day )
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()

print(timestamp)

year_2023 = datetime(2023, 1, 1) # Minimum data to reference a date: year, month and day.

def print_date(date):
	print(date.year)
	print(date.month)
	print(date.day)
	print(date.hour)
	print(date.minute)
	print(date.second)
	print(date.timestamp())

print_date(now)
print("")
print_date(year_2023)

print("\nImport time()")
from datetime import time

current_time = time() # It's an object used to encapsulate time (you need to give its values)
current_time = time(21, 6, 0)
# print_date(current_time) # Can't use the time() because it doesn't have the same attributes

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print("\nImport date()")
from datetime import date # It's the same as time but for the date

current_date = date.today() # Use the .today() method to get the system date

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 9, 5) # Define the date with the given arguments

print(current_date.year)
print(current_date.month)
print(current_date.day)

# current_date.year = current_date.year + 1 # This won't work

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)


diff = year_2023.date() - current_date # You can do arithmetics with objects of same type
print(diff)
diff = year_2023 - now
print(diff)

print("\nImport timedelta()")
from datetime import timedelta

# Work with time diffs

start_timedelta = timedelta(200, 100, 100, weeks=10) 
end_timedelta = timedelta(300, 100, 100, weeks=13) 
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
# print(end_timedelta * start_timedelta) # Non-sense
print(end_timedelta / start_timedelta)