my_list = []

# INPUT FROM USER
for i in range(4):
    num = int(input(f"Enter Number {i+1}: "))
    my_list.append(num)

# UNWRAPPING
a,b,c,d = my_list

# MAIN-LOGIC
largest = None
if (a>=b and a>=c and a>=d):
    largest = a
elif (b>=a and b>=c and b>=d):
    largest = b
elif (c>=a and c>=b and c>=d):
    largest = c
else:
    largest = d


print(f"Largest Number: {largest}")