if (n:=len([1,2,3,4,5])) > 3 :
    print(f"The length ({n}) is too long")

print(n) # you can still access n outside the if statement, as there is no concept of block scope in Python. The variable n is still accessible and retains its value.