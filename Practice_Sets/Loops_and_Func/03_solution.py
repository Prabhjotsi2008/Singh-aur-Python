n = int(input("Enter value of n: "))

"""
*
**
***
****
*****
"""

for i in range(1,n+1):
    print("*" * i,end="")
    print()


"""
*****
****
***
**
*
"""
for i in range(n,0,-1): # just reverse the outer loop and DONE
    print("*" * i)