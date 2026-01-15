# ENCAPSULATION # GETTER SETTER

class Car:
    def __init__(self,brand,model):
        print("Car constructor called")
        self.__brand = brand # by doing __variable_name # we make variable_name private
        self.model = model

    # getter # we can give any name to getter # however conventionally used get_variable_name
    def get_brand(self):
        return self.__brand.upper() + "!"

    # setter # used to set attribute value in a class
    def set_brand(self,brand):
        self.__brand = brand

    def set_model(self,model):
        self.model = model

    def car_info(self):
        return f"Car: {self.__brand} {self.model}"
    


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model) # at this point car constructor is called 
        print("Electric constructor called")
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla","S","85kWh")
# print(my_tesla.__brand) # AttributeError: 'ElectricCar' object has no attribute '__brand'. # PRIVATE
print(my_tesla.get_brand()) # get data # Tesla!
print(my_tesla.car_info()) # Car: Tesla S

my_tesla.set_brand("Mitsubishi") # set value
my_tesla.set_model("Pajero") # set value

print(my_tesla.get_brand()) # get data # Mitsubishi!
print(my_tesla.car_info()) # Car: Mitsubishi Pajero