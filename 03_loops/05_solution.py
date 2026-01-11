# FIND THE FIRST NON-REPEATED CHARACTER
input_str = "teeteracdcd"


for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("The first non-repeated character is", char)
        break # break loop when the char is detected
