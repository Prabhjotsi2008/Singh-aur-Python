# RECURSION

# Iterative-Method
def iterative_fact(num):
    fact = 1
    for i in range(1,num+1):
        print(i)
        fact*=i
    return fact

print(f"Iterative Factorial : {iterative_fact(1)}")


# Recursive-Method
def recursive_fact(num):
    if num==0: return 1 # BASE-CASE
    return num * recursive_fact(num-1) # RECURSIVE CASE

print(f"Recursive Factorial : {recursive_fact(5)}")