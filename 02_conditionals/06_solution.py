# TRANSPORTATION MODE SELECTION
dist = float(input("Enter distance to travel : "))
suggest = ""


# LOGIC
if dist<0:
    print("Invalid distance entered")
    exit()

if dist < 3:
    suggest = "You should walk"
elif dist <=15:
    suggest = "You should take a Bike"
else:
    suggest = "You should take a Car"

# OUTPUT
print(f"The distance is {dist} km, {suggest}")