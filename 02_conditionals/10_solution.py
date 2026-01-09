# PET FOOD RECOMMENDATION

species = input("Enter your Pet Species : ").lower()
age = int(input(f"Enter {species} age (in years) : "))
suggest = ""


# LOGIC
if age<0:
    print("Invalid age entered")
    exit()

if species == "dog":
    suggest = "Puppy food" if age<2 else "Dog Food"
elif species == "cat":
    suggest = "Senior Cat food" if age>5 else "Junior Cat food"
else:
    suggest = "Whatever it likes"


# OUTPUT
print(f"Your {species.capitalize()} is {age} years old, Give {suggest}")