# TUPLE (IMMUTABLE) 
# we cannot change value from memory as we can do in case of list

tea_types = ("Black", "Green", "Oolong")
print(tea_types)


# ACCESSING VALUES
print(tea_types[0]) # Black
print(tea_types[-1]) # Oolong # last value

# SLICING 
print(tea_types[1:]) # ('Green', 'Oolong')


# CHANGING VALUES NOT POSSIBLE # TUPLE IS IMMUTABLE
# tea_types[0] = "Lemon" # TypeError: 'tuple' object does not support item assignment


# LENGTH of TUPLE 
print(len(tea_types)) # 3


# JOINING MULTIPLE TUPLE # it can work for LIST as well
more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types # concatenate two TUPLES
print(all_tea) # ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')


# CONDITIONAL on TUPLES
if "Green" in all_tea:
    print("I have green tea")


# COUNT of a PARTICULAR VALUE in TUPLE
more_tea = ("Herbal", "Earl Grey", "Herbal")
print(more_tea)
print(more_tea.count("Herbal")) # 2
print(more_tea.count("Herb")) # 0 # as "Herb" is not present in more_tea


# UNWRAPING a TUPLE using a TUPLE
(tea1, tea2, tea3) = tea_types # the count must be same # In this case, both tuples have 3 values
print(tea1) # Black
print(tea2) # Green
print(tea3) # Oolong


# TYPE of TUPLE
print(type(tea_types)) # tuple
print(type(tea1)) # string


# NESTED TUPLE
players = (("Abhishek", "Sanju","Tilak"),("Surya","Axar","Hardik","Dube"),("Varun","Harshit","Bumrah","Arsh"))

print("Captain :",players[1][0]) # Captain: Surya
print("Top Order :", players[0]) # Top Order : ('Abhishek', 'Sanju', 'Tilak')
print("Middle Order :", players[1]) # Middle Order : ('Surya', 'Axar', 'Hardik', 'Dube')
print("Lower Order :", players[2]) # Lower Order : ('Varun', 'Harshit', 'Bumrah', 'Arsh')