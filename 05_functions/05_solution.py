# DEFAULT PARAMETER VALUE IN FUNCTION

def greet(name="Chai"): # "Chai" is default value of parameter
    return f"Hello, {name}!"


print(greet("Prabhjot")) # with argument # Hello, Prabhjot!
print(greet()) # without argument # Hello, Chai! 