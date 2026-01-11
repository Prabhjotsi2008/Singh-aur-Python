# COUNTING +VE NUMBERS
nums = [1,-2,3,-4,5,6,-7,-8,9,10]
pos_count = 0

# LOGIC
for n in nums:
    if n>0:
        pos_count += 1

# OUTPUT
print("Positive Count : ", pos_count)