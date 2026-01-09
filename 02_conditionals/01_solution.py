# AGE GROUP CATEGORIZATION
age = int(input("Enter your age : "))


if (age < 13): # you can add paranthesis () to condition # it will still work without ()
    print("Child")
elif age >13 and age < 20: # and operator is same as (&& in JS/C++)
    print("Teenager")
elif age < 60:
    print("Adult")
else: # for 60+ 
    print("Senior")