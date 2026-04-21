# USERNAME-VALIDATOR
import re

username = input("Enter Username: ")
pattern = r"^[A-Za-z_0-9]{5,15}$"
s = re.match(pattern,username)
print(s)

print(f"{username} is VALID") if s else print(f"{username} is INVALID")