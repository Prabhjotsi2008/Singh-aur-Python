# LIST
tea_variety = ["Black","Green", "Oolong", "White"]
print(tea_variety)


# INDEX 
print(tea_variety[1]) # Green # 2nd element
print(tea_variety[-2]) # Oolong # 2nd last element


# SLICING OF LIST
print(tea_variety[1:3]) # ['Green', 'Oolong'] # [start_idx : end_idx] # end_idx not included
print(tea_variety[:2]) # ['Black', 'Green']
print(tea_variety[1:]) # ['Green', 'Oolong', 'White']

# HOPPING IN LIST
print(tea_variety[::2]) # ['Black', 'Oolong'] # [start_idx, end_idx, step_size(no_of_terms_hopped)]

# CHANGING DATA IN LIST
tea_variety[3] = "Herbal"
print(tea_variety) # ['Black', 'Green', 'Oolong', 'Herbal']



# ** PROBLEM **
tea_variety[1:2] = "Lemon"
print(tea_variety) # ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']

# ** SOLUTION **
tea_variety = ["Black","Green", "Oolong", "White"] # starting again
print(tea_variety) # ['Black', 'Green', 'Oolong', 'White']
print(tea_variety[1:2]) # Green
tea_variety[1:2] = ["Lemon"] # passing as a list
print(tea_variety) # DONE # ['Black', 'Lemon', 'Oolong', 'White']



# REPLACING IN LIST # similar to splice in JS
print(tea_variety[1:3]) # ['Lemon', 'Oolong']
tea_variety[1:3] = ["Masala"] # replaces ['Lemon', 'Oolong'] by ["Masala"]
print(tea_variety) # ['Black', 'Masala', 'White']

# ADDING NEW DATA WITHOUT DELETING PREVIOUS ONE
print(tea_variety[1:1]) # returns empty list []
tea_variety[1:1] = ["test","test"]
print(tea_variety) # ['Black', 'test', 'test', 'Masala', 'White']

# REMOVING DATA FROM LIST
print(tea_variety[1:3]) # ['test', 'test']
tea_variety[1:3] = [] # replaced by empty array []
print(tea_variety) # ['Black', 'Masala', 'White']



# TRAVERSING THROUGH LIST
for tea in tea_variety:
    print(tea, end="-") # ends each value with "-" # Black-Masala-White-

print() # to get a new line after the loop ends


# BASIC CONDITIONAL ON LIST
if "Oolong" in tea_variety:
    print("I have Oolong Tea") # doesnot run as "Oolong" is not present


# APPEND in LIST  # adds at end of list
tea_variety.append("Oolong") # adds "Oolong" at end of tea_variety
print(tea_variety) # ['Black', 'Masala', 'White', 'Oolong']

if "Oolong" in tea_variety:
    print("I have Oolong Tea") # works as "Oolong" is present


# POP in LIST # removes last element
print(tea_variety.pop()) # Oolong 
print(tea_variety) # ['Black', 'Masala', 'White']


# REMOVE in LIST # remove a particular value from list
tea_variety.remove("Masala") # removes Masala
print(tea_variety) # ['Black', 'White']


# INSERT in LIST # adds new data at a particular index
tea_variety.insert(1,"Green") # (idx, data_value) # adds "Green" at 1 index
print(tea_variety) # ['Black', 'Green', 'White']


# COPYING A LIST
copy = tea_variety # it is not a copy # both list point to the same memory address
tea_variety_copy = tea_variety.copy() # copy in real sense of memory # both have different memory reference
copy2 = tea_variety[:] # works same as .copy()


copy.append("Lemon")
print(copy) # ['Black', 'Green', 'White', 'Lemon']
print(tea_variety) # ['Black', 'Green', 'White', 'Lemon']
print(tea_variety_copy) # ['Black', 'Green', 'White'] # not affected as it has diff. memory reference


# LIST COMPREHENSION
print(range(10)) # range(0, 10)
squared_num = [x**2 for x in range(10)] # from 0 to 9 # as 10 is not included
print(squared_num) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cubed_nums = [num**3 for num in range(5)]
print(cubed_nums) # [0, 1, 8, 27, 64]