# INHERITANCE in CLASS

# BASE CLASS
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def car_info(self):
        return f"Car: {self.brand} {self.model}"


# DERIVED CLASS (INHERITED)
class ElectricCar(Car): # inherits Car class
    def __init__(self, brand, model, battery_size):
        # used super to get access of Base Class property
        super().__init__(brand,model) # used dot (.) notation to access property of base class

        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla","S","5kWh")
print(my_tesla.car_info()) # Car: Tesla S
