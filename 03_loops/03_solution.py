# MULTIPLICATION TABLE OF A NUMBER UPTO 10 (SKIP THE FIFTH ITERATION)
num = int(input("Enter a number to print its multiplication table : "))

for i in range(1,11):
    if i==5: # checks 5th iteration
        print("Skipped 5th iteration")
        continue
    print(f"{num} X {i} = {num*i}")
