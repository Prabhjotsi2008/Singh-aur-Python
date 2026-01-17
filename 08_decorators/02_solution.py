# DEBUGGING FUNCTION CALLS

def debug(func):
    print("IN debug")
    def wrapper(*args,**kwargs):
        args_value = ", ".join(str(arg) for arg in args) or 0
        kwargs_val = ", ".join(f"{k} : {v}" for k,v in kwargs.items()) or 0
        print(f"Calling {func.__name__} with args {args_value} and kwargs {kwargs_val}")
        result = func(*args,**kwargs)
        count = 0 # counter for arguments
        for i in args: # for arguments
            count += 1
        
        for i in kwargs: # for key-value arguments
            count += 1

        print(f"{func.__name__} has {count} arguments.")
        return result

    return wrapper



@debug # decorator
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

# we are calling wrapper() # as @debug works same as greet = debug(greet)
greet("Prabhjot",greeting="Hanji") # named argument (greeting="Hanji")


# manual-decorator
def hello():
    print("Hello")

hello = debug(hello)
hello()