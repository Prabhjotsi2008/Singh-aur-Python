class MyClass:
    a = 5

obj = MyClass()
obj.a = 1 # we changed instance attribute # not class attribute

print("Class Attribute:",MyClass.a) # class attribute remains the same
print("Instance Attribute:",obj.a)