# FACTORIAL CALCULATOR
number = int(input("Enter a number : "))
fact = 1
num = number # just so that we have the input value for output
# using FOR-LOOP
# for i in range(1,number+1):
#     fact *= i

# using WHILE-LOOP
while number > 0:
    fact *= number
    number -= 1

print(f"Factorial of {num} : {fact}")