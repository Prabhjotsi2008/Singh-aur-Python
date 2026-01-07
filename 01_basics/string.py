# STRINGS
chai = "Masala Chai"
print(chai) # Masala Chai

# INDEX in Strings
first_char = chai[0]
print(first_char) # M

third_last = chai[-3] # -ve index starts in reverse order
print(third_last) # h


# SLICING in Strings
slice_chai = chai[0:6] # [start_idx : end_idx] # start_idx is included # end_idx isn't included
print(slice_chai) # Masala

# Slicing in-depth
num_list = "0123456789"
print(num_list[:]) # 0123456789 # entire string 
print(num_list[3:]) # 3456789 # from 3rd index to end
print(num_list[:7]) # 0123456 # from start upto 6th index (as 7th index not included)

# SLICE WITH THREE PARAMS
print(num_list[2:8]) # 234567 # without hopping
print(num_list[2:8:2]) # [start_idx : end_idx : step_size(no_of_terms_hopped)] # 246


# METHODS OF STRINGS
print(chai.lower()) # lower-case # masala chai
print(chai.upper()) # Upper-case # MASALA CHAI

chai_2 = "     Masala Chai     "
print(chai_2.strip()) # removes whitespaces at start and end 

chai_3 = "Lemon Chai"
print(chai_3.replace("Lemon", "Ginger"))

# STRING to LIST
chai_4 = "Lemon, Ginger, Masala, Mint"
print(chai_4.split()) # by-default, it split by spaces " "
print(chai_4.split(', ')) # it split when ", " is detected

# TRAVERSING USIGN LOOP
myList = chai_4.split(", ")
for l in myList:
    print(l)

print(chai.find("Chai")) # gives the start_idx of the value # 7
print(chai.find("l")) # 4
print(chai.find("p")) # -1 # signifies that value is not present
print(chai.find("chai")) # -1 # as "chai" is not present

chai_5  = "Masala Chai Chai Chai"
print(chai_5.count("Chai")) # 3 # gives count of the value occured



# ORDER-FORMATTING
chai_type = "Masala Chai"
quantity = 2
order = "I ordered {} cups of {}" # here {} is placeholder for values

print(order) # I ordered {} cups of {}
print(order.format(quantity,chai_type)) # I ordered 2 cups of Masala Chai


# LIST to STRINGS
chai_variety = ['Lemon', 'Ginger', 'Masala', 'Mint']
print(chai_variety)
print("".join(chai_variety)) # LemonGingerMasalaMint # joins all the list elements
print("-".join(chai_variety)) # Lemon-Ginger-Masala-Mint # joins list elements with "-" seperated

# LENGTH of STRING
print(len(chai)) # 11


# ESCAPE-CHARACTERS
myStr = "He said, \"Masala chai is awesome\" "
print(myStr) # He said, "Masala chai is awesome"
print(len(myStr)) # 34


# RAW-STRING
chai_6 = r"Masala\nChai" # used as raw string 
print(chai_6) # Masala\nChai # even escape characters are counted

path = r"c:\Users\Hp\OneDrive" # use-case of r"" (raw-string)
print(path)


# CONTAINS OR NOT
print("Masala" in chai) # True
print("Massala" in chai) # False