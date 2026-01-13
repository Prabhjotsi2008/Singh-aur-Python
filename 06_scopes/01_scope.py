username = "chaiaurcode"
def func():
    username = "chai" # it is a different variable
    print(username) # chai # access the local variable # if not present, it access the global variable
    
print(username) # chaiaurcode # as it can access the global variable only

func() # called function



x = 99 # global variable
def func2(y):
    z = x+y
    return z

print(func2(1)) # 100 # x + y -> 99 + 1 -> 100



# using global keyword to access # however it is a bad practice to manipualte global variable 
def func3():
    global x
    x = 12 # global variable

func3() # called function
print(x) # 12 # x value changed



n = 99
def f1():
    # n = 88
    def f2():
        print(n) # 88 # if n not in f1(), then global variable n is used # 99
    f2() # calling f2()
f1() # calling f1()




# CLOSURE # BAG THEORY # when a function definition is returned, its associated variable are also returned
def f1():
    n = 88
    def f2():
        print(n) # 88 # if n not in f1(), then global variable n is used # 99
    return f2 # returned function definition of 2 with n as well # bag-pack

my_result = f1()
print(my_result) # <function f1.<locals>.f2 at 0x0000019C1B277690>

my_result() # 88



# PROPER-CLOSURE  # factory functions
def chai_coder(num):
    def actual(x):
        return x ** num
    return actual # returned function definition of actual(x) with num as well # bag-pack

result = chai_coder(3) # setted num -> 3
print(result) # <function chai_coder.<locals>.actual at 0x000001F2DDE278A0>
output = result(2) # setted x -> 2
print(output) # x ** num --> 2**3 --> 8

# shorthand of closure execution
print(chai_coder(2)(3)) # 3 ** 2 --> 9