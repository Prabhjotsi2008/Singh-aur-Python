# PHONE-VALIDATOR
import re

text = input("Enter Phone Number: ")
pattern = r"^\d{10}$"
s = re.match(pattern,text)

print(s)
print(f"{text} is VALID") if s else print(f"{text} is INVALID")


# INDIAN-NUMBER VALIDATOR
phone_number = input("Enter a phone number (with country code): ")
indian_pattern = r"^\+91\d{10}$"
s2 = re.match(indian_pattern,phone_number)

print(s2)
print(f"{phone_number} is INDIAN Number") if s2 else print(f"{phone_number} is Non-INDIAN Number")