# PRIME NUMBER CHECKER
number = int(input("Enter a number to check whether it is prime or not : "))
isPrime = True

if number<2:
    isPrime = False

else:
    for i in range(2,number):
        if (number%i==0):
            print(i)
            isPrime = False
            break

if isPrime:
    print(f"{number} is Prime")
else:
    print(f"{number} is not Prime")