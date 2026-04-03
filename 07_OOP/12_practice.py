class Demo:
    a = 1
    def show(self):
        print(Demo.a)

obj = Demo()
obj.a = 5
obj.show() # 1

class Demo2:
    a = 1
    @classmethod
    def show(cls):
        print(cls.a)
    
obj2 = Demo2()
obj2.a = 23
obj2.show()

# EXPLANATION:
# In the first class, we are changing the instance attribute a to 5 but when we call the show method it is still printing 1 because in the show method we are accessing the class attribute a and not the instance attribute a. 
# In the second class, we are using @classmethod and in the show method we are accessing the class attribute a using cls.a and when we change the instance attribute a to 23 it does not affect the class attribute a and it still prints 1.