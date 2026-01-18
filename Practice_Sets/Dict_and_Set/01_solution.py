my_dict = {
    "Hello" : "Namaste",
    "Cat" : "Billi",
    "Batsman" : "Ballebaaz",
    "Bowler" : "Gendbaaz" 
}

print("English-words available in dictionary: ", end="")
for key in my_dict.keys():
    print(key,end=" ")
print()

input_val = input("Enter a word you want to translate to Hindi: ")
if input_val in my_dict.keys():
    print(f"{input_val} = {my_dict[input_val]}")
else:
    print("Word not present in dictionary")