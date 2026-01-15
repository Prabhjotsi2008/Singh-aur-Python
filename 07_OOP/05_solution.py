# POLYMORPHISM # ANEK-ROOP

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def car_info(self):
        return f"Car: {self.__brand} {self.model}"
    
    # brand-getter
    def get_brand(self):
        return f"{self.__brand.upper()}!"
    
    # brand-setter
    def set_brand(self,brand):
        self.__brand = brand

    # FUEL-METHOD
    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    # POLYMORPHISM FOR OUTPUT
    def fuel_type(self): # ditto same function as Car just output is different
        return "Electric Charge"



my_ev = ElectricCar("Tesla","S","85kWh")
print(my_ev.fuel_type()) # Electric Charge

safari = Car("Tata","Safari")
print(safari.fuel_type()) # Pertol or Deisel