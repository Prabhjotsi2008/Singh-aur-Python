# WEATHER ACTIVITY SUGGESTION
weather = input("Enter Weather (Sunny, Rainy, Snowy) : ").lower() # to simplify input
activity = ""


# LOGIC
if weather=="sunny":
    activity = "Go for a walk"
elif weather=="rainy":
    activity = "Read a book"
elif weather=="snowy":
    activity = "Build a snowman"
else:
    activity = "Do whatever you want"


# OUTPUT
print(f"The weather is {weather}, {activity}") # used f-strings # similar to string interpolation in JS