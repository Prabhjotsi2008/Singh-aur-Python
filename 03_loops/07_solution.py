# VALIDATE INPUT (bw 1 to 10)
input_val = int(input("Enter a number (1-10): "))

while True:
    if(input_val<1 or input_val>10):
        print("Number should be between 1 and 10")
        input_val = int(input("Enter a number : "))
    else:
        break

print("You logged in with", input_val)


# ANOTHER APPROACH (BETTER)
while True:
    number = int(input("Enter a number (1-10) : "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Try again!!!")
