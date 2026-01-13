# FUNCTION WITH **kwargs # it is used to get multiple key:value arguments

def print_kwargs(**kwargs): # keyword-argument 
    # print("Name:", name,"Power:", power)

    print(type(kwargs)) # dict

    for key,val in kwargs.items():
        print(f"{key} : {val}",end=" ")
    print()

    # JUST ANOTHER WAY OF LOOPING OVER A DICT
    for key in kwargs:
        print(f"{key} : {kwargs[key]}", end= " ")
    print()



print_kwargs(name="shaktiman",power="lazer") # Name: shaktiman Power: lazer

# using named argument for calling function # in this the order of argument doesn't matter as we are explicitally defining the argument for a particular param
print_kwargs(power="lazer",name="shaktiman") # same output as above # Name: shaktiman Power: lazer

print_kwargs(name="shaktiman",power="lazer", enemy="Dr. Jackaal")