l = ["Rohan","Sachin","suraj","Dubey"]

for name in l:
    # if name[0].lower() == "s":
    if name.startswith("S"): # works same as above # but lower case problem occurs
        print(f"Hello, {name}")