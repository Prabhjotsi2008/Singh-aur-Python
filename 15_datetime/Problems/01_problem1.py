# AGE CALCULATOR
from datetime import datetime

def age_calc(dob):
    current = datetime.now()

    # age = current - dob
    # print(f"Your age: {age}")

    year = current.year - dob.year
    month = current.month - dob.month
    day = current.day - dob.day

    if day<0:
        day+=30
        month-=1

    if month<0:
        month+=12
        year-=1

    return f"Age: {year} Years, {month} Months, {day} Days"


try:
    input_str = input("Enter DOB (DD-MM-YYYY): ")
    dob = datetime.strptime(input_str,"%d-%m-%Y")
except ValueError:
    print("Invalid input entered!!!")
else:
    age = age_calc(dob)
    print(age)