# TIME-DELTA 
## A timedelta is a duration expressing the difference between two dates or times.
from datetime import datetime, timedelta

current = datetime.now()
print(f"Current date: {current.date()}")

# Adding 5 days to the current date
future_date = current + timedelta(days=5)
print(f"Date after 5 days: {future_date.date()}")

# Subtracting 2 hours from the current time
past_time = current - timedelta(hours=2)
print(f"Time 2 hours ago: {past_time.time()}")

# Adding 1 week and 3 days to the current date
future_date_2 = current + timedelta(weeks=1, days=3)
print(f"Date after 1 week and 3 days: {future_date_2.date()}")


# DIFFERENCE BETWEEN TWO DATES
date1 = datetime(2026,5,1) # 1 May 2026
date2 = datetime(2026,5,10) # 10 May 2026
diff = date2 - date1
print(f"Difference b/w dates: {diff}") # 9 days, 0:00:00
print(f"Type of diff: {type(diff)}") # <class 'datetime.timedelta'>, it is a timedelta object which represents the difference between two dates or times
