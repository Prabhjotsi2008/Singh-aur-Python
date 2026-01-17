# TIMING FUNCTION EXECUTION
import time

# timer-function to check
def timer(func):
    print("IN timer function")
    def wrapper(*args, **kwargs): # unlimited arguments
        start_time = time.time()
        print("IN wrapper")
        result = func(*args,**kwargs)
        for i in args:
            print(i, end=" ")
        print()
        print("Result loaded")
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time} seconds") # __name__ gives name of the function
        return result
    return wrapper


@timer # decorator # now example_function always pass through timer function
def example_function(n,a,b,c): # used a,b,c just to check if *args can be used in wrapper
    time.sleep(n)
    print(f"After {n} seconds")

# @timer (decorator) does the follows :
# example_function = timer(example_function) # it also works
example_function(2,24,32,35) # here we are calling wrapper() # not example function