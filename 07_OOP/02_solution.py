# FUNCTION IN CLASS

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def get_info(self): # use self to make context-connection
        return f"Car: {self.brand} {self.model}"


my_car = Car("Mitsubishi", "Pajero")
print(my_car.brand) # Mitsubishi
print(my_car.model) # Pajero
print(my_car.get_info()) # Brand: Mitsubishi, Model: Pajero