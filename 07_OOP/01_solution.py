# BASIC CLASS AND OBJECT

# creating a class
class Car:
    # brand = None
    # model = None

    # Constructor (the one which is called immediately when an object is formed)
    def __init__(self, brand, model): # self links context # same as this in JS 
        self.brand = brand
        self.model = model



# creating an object
my_car = Car("Toyota","Corolla")
print(my_car.brand) # Toyota
print(my_car.model) # Corolla

# another object from class
my_new_car = Car("Tata", "Safari")
print(my_new_car.model) # Safari