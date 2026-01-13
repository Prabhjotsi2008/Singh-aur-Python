# FUNCTION WITH *args # function with multiple number of params

# only use *args # cannot use *chai or anything else
def sum_all(*args): # * signifies that multiple argument are possible
    print(*args)
    print(args)
    print(type(args)) # tuple # as we dont want to change the argument given to function

    for i in args:
        print(i, end=" ")
    return sum(args)

print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))