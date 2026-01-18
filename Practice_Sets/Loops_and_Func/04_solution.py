n = int(input("Enter value of n: "))

"""
*** # for first and last term only # i==1 or i==n
* * # " " --> (n-2) times
***
"""

for i in range(1,n+1):
    if i==1 or i==n: # for first and last row only
        print("*" * n)
    else:
        print("*",end="")
        print(" " * (n-2), end="")
        print("*",end="")
        print()

