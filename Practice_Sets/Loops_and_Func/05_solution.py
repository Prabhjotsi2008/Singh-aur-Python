def iter_pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end="")
        print()



# IT WORKS BUT IS QUITE COMPLEX TO UNDERSTAND
# def complex_way_pattern(n):
#     for i in range(1,n+1):
#         print("*" * ((n+1)-i))


def recursive_pattern(n):
    if (n==0):
        return
    print("*" * n)
    recursive_pattern(n-1)


iter_pattern(5)
recursive_pattern(5)