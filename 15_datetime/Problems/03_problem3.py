# EVENT-COUNTDOWN
from datetime import datetime,timedelta

def event_counter(d):
    current = datetime.now()

    diff = d - current
    days = diff.days
    seconds = diff.seconds
    
    secs = seconds%60
    mins = (seconds%3600) // 60
    hours = seconds // 3600
    return f"Event in {days} Days, {hours} hours, {mins} minutes, {secs} seconds"

try:
    input_str = input("Enter Event Date (DD-MM-YYYY HH:MM): ")
    future_date = datetime.strptime(input_str,"%d-%m-%Y %H:%M")
except ValueError:
    print("Invalid input entered!!!")
else:
    output = event_counter(future_date)
    print(output)