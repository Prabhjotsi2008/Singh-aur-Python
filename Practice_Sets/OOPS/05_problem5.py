class Person:
    def __init__(prabh,name,age): # we can even name self as prabh or anything its just a placeholder for the object which is being created
        prabh.name = name
        prabh.age = age

    def getInfo(prabh):
        print(f"Name: {prabh.name}\nAge: {prabh.age}")
    

p = Person("Prabhjot",18)
p.getInfo()