# FRUIT RIPENESS CHECKER
fruit = input("Enter a Fruit : ")

# LOGIC

# works only if fruit is "Banana" or "banana"
if fruit == "Banana" or fruit=="banana":
    
    color = input("Enter color of fruit (Green,Yellow,Brown) : ")
    ripeness = ""

    if color == "Green" or color == "green":
        ripeness = "Unripe"
    elif color == "Yellow" or color == "yellow":
        ripeness = "Ripe"
    elif color == "Brown" or color == "brown":
        ripeness = "Overripe"
    else:
        ripeness = "unknown"
    
    print("The Banana is", ripeness)

# works if fruit isn't Banana
else:
    print("Fruit is not Banana")
