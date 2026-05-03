# DAYS B/W TWO DATES
from datetime import datetime

def diff_days(date1,date2):
    diff = date1 - date2
    return abs(diff.days) # returns absolute diff # handles -ve values

try:
    date1_str = input("Enter Date 1 (DD-MM-YYYY): ")
    date1 = datetime.strptime(date1_str,"%d-%m-%Y")
    date2_str = input("Enter Date 2 (DD-MM-YYYY): ")
    date2 = datetime.strptime(date2_str,"%d-%m-%Y")
except ValueError:
    print("Invalid input entered!!!")
else:
    diff = diff_days(date1,date2)
    print(f"Difference: {diff} days")