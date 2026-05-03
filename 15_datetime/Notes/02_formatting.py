# FORMATTING IN DATETIME
from datetime import datetime

# strftime() method is used to format the date and time in a specific way

# Meaning of the format codes:
# %Y - Year with century (e.g., 2024)
# %m - Month as a zero-padded decimal (e.g., 01, 02, ..., 12)
# %d - Day as a zero-padded decimal (e.g., 01, 02, ..., 31)
# %H - Hour (24-hour clock) as a zero-padded decimal (e.g., 00, 01, ..., 23)
# %M - Minute as a zero-padded decimal (e.g., 00, 01, ..., 59)
# %S - Second as a zero-padded decimal (e.g., 00, 01, ..., 59)
# %B - Full month name (e.g., January, February, ..., December)

now = datetime.now()

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

formatted_date_2 = now.strftime("%d %B, %Y") # date month, year format
print("Formatted date 2:", formatted_date_2)



# strptime() method is used to parse a string into a datetime object based on a specified format
date_str = input("Enter a date (DD-MM-YYYY): ")

date_obj = datetime.strptime(date_str,"%d-%m-%Y")
print(f"Date object parsed: {date_obj}")
print(f"Only Date Part: {date_obj.date()}")