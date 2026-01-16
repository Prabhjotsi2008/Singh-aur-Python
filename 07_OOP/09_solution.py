# CLASS INHERITANCE & isinstance()

class Car:
    car_count = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model # made it private # so that access-denied
        Car.car_count += 1

    def get_brand(self):
        return f"{self.__brand.upper()}!"
    
    def car_info(self):
        return f"Car: {self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description(): # now self (current-context) isn't needed as method is static
        return "Cars are means of transport"
    

    @property # kind of model-getter # it makes the function as an attribute 
    def model(self):
        return self.__model + "!"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"
    

# PROVING INSTANCE
my_tesla = ElectricCar("Tesla","S","85kWh")

# isinstance(object,class)
print(isinstance(my_tesla, Car)) # True
print(isinstance(my_tesla, ElectricCar)) # True