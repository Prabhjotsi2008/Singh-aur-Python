# DICTIONARY
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)

# ACCESSING VALUES # through keys
print(chai_types["Masala"]) # Spicy 
print(chai_types.get("Ginger")) # Zesty

print(chai_types.get("Masalaaaaa")) # None # as key is not present
# print(chai_types["Masalaaaaaaaa"]) # throws error # as key is not present


# CHANGING VALUES
chai_types["Green"] = "Fresh" # value changed
print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}


# LOOPING THROUGH DICT
for chai in chai_types:
    print(chai, ":", chai_types[chai]) # (key :  value)

# special for DICT
for key,val in chai_types.items():
    print(key,val)


# BASIC CONDITIONAL on DICT
if "Masala" in chai_types:
    print("I have masala chai")


# LENGTH of DICT # returns number of items (key + value = item) present in a dict
print(len(chai_types)) # 3


# ADDING NEW VALUE in DICT
chai_types["Earl Grey"] = "Citrus"
print(chai_types) # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

# REMOVE in DICT
chai_types.pop("Ginger")
print(chai_types) # {'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

# REMOVE LAST ITEM in DICT
print(chai_types.popitem()) # ('Earl Grey', 'Citrus')
print(chai_types) # {'Masala': 'Spicy', 'Green': 'Fresh'}

# DELETE in DICT
del chai_types["Green"] # it deletes the memory reference of the data-value
print(chai_types) # {'Masala': 'Spicy'}


# COPY of DICT
chai_types_copy = chai_types.copy() # new dict will be created in the memory


# NESTED-DICT
tea_shop = {
    "chai" : {"Masala" : "Spicy", "Ginger": "Zesty"},
    "Tea" : {"Green" : "Fresh", "Black" : "Strong"}
}

print(tea_shop)
print(tea_shop["chai"]) # {'Masala': 'Spicy', 'Ginger': 'Zesty'}
print(tea_shop["Tea"]) # {"Green" : "Fresh", "Black" : "Strong"}
print(tea_shop["chai"]["Ginger"]) # Zesty
print(tea_shop["Tea"]["Green"]) # Fresh


# DICT-COMPREHENSION
squared_nums = {x : x**2 for x in range(6)}
print(squared_nums) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# REMOVE ENTIRE ITEMS from DICT
squared_nums.clear()
print(squared_nums) # {} empty dict


# ANOTHER-WAY
keys = ["Masala","Ginger","Lemon"]
default_val = "Delicious"

new_dict = dict.fromkeys(keys,default_val)
print(new_dict) # {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}

new_dict = dict.fromkeys(keys,keys) # CHAOS
print(new_dict) # {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}


# DICT - PRACTICE
player = {
    "top" : ["Rohit","Gill","Virat"],
    "middle" : ["Iyer","Rahul", "Hardik", "Axar"],
    "lower" : ["Varun", "Kuldeep","Bumrah","Arsh"]
}

player_2 = player.items()
for p in player_2:
    print(f"{p[0].capitalize()} Order : {" ".join(p[1])}")


print(player.popitem()) # removes lower order
for p in player_2:
    print(f"{p[0].capitalize()} Order : {" ".join(p[1])}")


print(player.update({"lower" : ["Harshit", "Bumrah", "Siraj", "Arsh"]}))  # added new lower order
for p in player_2:
    print(f"{p[0].capitalize()} Order : {" ".join(p[1])}")


print(player.update({"top" : ["Abhishek", "Sanju", "Tilak"]})) # updated top # can update only one item at a time
for p in player_2:
    print(f"{p[0].capitalize()} Order : {" ".join(p[1])}")


print(player.update({"middle" : ["Surya", "Hardik", "Axar", "Dube"]})) # updated middle order
for p  in player_2:
    print(f"{p[0].capitalize()} Order : {" ".join(p[1])}")