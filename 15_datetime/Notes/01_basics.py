# DateTime Basics
from datetime import datetime, date, time

# Get the current date and time
now = datetime.now()
print(f"Data-type: {type(now)}") # <class 'datetime.datetime'>, it is a datetime object which contains both date and time information

print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Get today's date
today_full = datetime.today()
print("Today's date and time:", today_full)

# comparison between now and today
# In now we have the time component, but in today we don't have the time component, so the difference will be the time component of now


# Get just the date part
today = date.today()
print("Today's date:", today)
print(f"Type of today: {type(today)}") # <class 'datetime.date'>

# Get just the time part
current_time = now.time()
print("Current time:", current_time)
print(f"Type of current_time: {type(current_time)}") # <class 'datetime.time'>