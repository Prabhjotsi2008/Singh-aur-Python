# SUM OF EVEN NUMBERS
n = int(input("Enter a number : "))
sum_even = 0

# LOGIC
for i in range(1,n+1):
    if i%2==0:
        sum_even += i

# OUTPUT
print(f"Sum of even numbers upto {n} : {sum_even}")