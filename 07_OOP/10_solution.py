# MULTIPLE-INHERITANCE 


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


class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "This is engine"


# inherit from Battery, Engine, Car
class ElectricCar(Battery,Engine,Car):
    pass

my_ev = ElectricCar("Tesla","S")
print(my_ev.car_info())
print(my_ev.battery_info())
print(my_ev.engine_info())