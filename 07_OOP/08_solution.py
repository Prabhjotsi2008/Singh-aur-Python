# PROPERTY DECORATOR # make model read-only

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
    

my_car = Car("Tata", "Safari")
# my_car.model = "City" # AttributeError: property 'model' of 'Car' object has no setter
# print(my_car.model()) # TypeError: 'str' object is not callable
print(my_car.model) # Safari 