# REVERSE A STRING
input_str = input("Enter a string : ")
reverse_str = ""

for char in input_str:
    # reverse_str = reverse_str + char # it will copy
    reverse_str = char + reverse_str # work done # just by flipping the formula

print(f"The reverse of \"{input_str}\" : \"{reverse_str}\"")



# ANOTHER APPROACH
input_len = len(input_str)

# using staight loop
# for i in range(input_len): 
#     # print(input_len - i - 1)
#     reverse_str += input_str[input_len-i-1]

# using reverse loop
# for i in range(input_len-1,-1,-1): # range(start,end(excluded),step)
#     # print(i)
#     reverse_str += input_str[i]

# print(reverse_str)