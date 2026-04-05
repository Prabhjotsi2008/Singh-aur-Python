# TYPE HINTS in Python.
# Type hints are a way to indicate the expected data types of variables, function parameters, and return values. They are not enforced by the Python interpreter but can be used by developers and tools to improve code readability and catch potential type-related errors.

n : str = 323

print(n,type(n)) # 323 <class 'int'>

# print(len(n)) # TypeError: object of type 'int' has no len()

name: str = "Prabhjot" # we are using type hints to specify that the variable name is expected to be of type str (string).




# TYPE HINTS IN FUNCTIONS
def sum(a:int,b:int) -> int: 
    return a + b
# we are using type hints to specify that the function sum takes two integers as input and returns an integer as output.

print(sum(5,4)) # in this it suggests that the function sum should be called with two integers, and it will return an integer.

# NORMAL FUNCTION # without TYPE HINTS
def sum(a,b):
    return a + b
print(sum(5,4)) # this will work without type hints as well, but it does not provide any information about the expected types of the parameters or the return value.