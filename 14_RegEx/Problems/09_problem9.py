# PASSWORD-VALIDATOR
import re

def password_validator(password):
    suggest = [] # a list for suggestions
    strength = 0

    if re.search(r"\s",password):
        suggest.append("Password must not have spaces")
    else:
        if len(password) >= 8:
            strength += 1
        else:
            suggest.append("Password must have at least 8 characters")
        
        if re.search(r"[A-Z]",password):
            strength += 1
        else:
            suggest.append("Password must have at least 1 Upper-case character")
        
        if re.search(r"\d",password):
            strength += 1
        else:
            suggest.append("Password must have at least 1 digit")
        
        if re.search(r"[^\w\s]|_",password):
            strength += 1
        else:
            suggest.append("Password must have at least 1 symbol")
    
    return strength,suggest

password = input("Enter your password: ")
strength,suggestion = password_validator(password)

if strength == 4:
    print("Password is STRONG")
elif strength == 3:
    print("Password is MODERATE")
elif strength in (1,2):
    print("Password is WEAK")

if suggestion:
    print("Suggestions are :")
    for i,s in enumerate(suggestion,start=1):
        print(f"{i}. {s}")

