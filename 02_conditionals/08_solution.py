# PASSWORD CHECKER
password = input("Enter your Password : ")
length = len(password)
suggest = ""

# LOGIC
if length < 6 :
    suggest = "Weak"
elif length <= 10 :
    suggest = "Medium"
else:
    suggest = "Strong"

# OUTPUT 
print(f"Your password \"{password}\" is {suggest}")