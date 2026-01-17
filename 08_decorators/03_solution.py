# CACHE RETURN VALUE OF FUNCTION
import time

def cache(func):
    cache_val = {} # empty dict
    print(f"Cache-Values: {cache_val}")
    def wrapper(*args):
        if args in cache_val:
            print("Already present")
            return cache_val[args]
        
        print("New value")
        result = func(*args)
        cache_val[args] = result
        return result
    
    return wrapper



# decorator function runs even before the long_running_func() is called # it only runs ONCEs
# so Cache Values are printed only first and last time
# Because decorators run at definition time, not call time.
@cache
def long_running_func(a,b):
    time.sleep(4)
    return a+b


print(long_running_func(2,3))
print(long_running_func(2,3))
print(long_running_func(4,3))