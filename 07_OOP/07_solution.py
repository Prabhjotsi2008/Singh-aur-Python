# STATIC METHOD # method belongs to CLASS (blueprint), but not for instance of object (formed from CLASS)
# If a method does not use self or cls, make it a @staticmethod — to express that it is independent of object and class state.

class Car:
    car_count = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.car_count += 1

    def get_brand(self):
        return f"{self.__brand.upper()}!"
    
    def car_info(self):
        return f"Car: {self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description(): # now self (current-context) isn't needed as method is static
        return "Cars are means of transport"



class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"
    

my_car = Car("Tata", "Safari")
print(my_car.general_description()) # Cars are means of transport # THIS IS POSSIBLE # but BAD PRACTICE
print(Car.general_description()) # Cars are means of transport # THIS IS PREFERRED # PROFESSIONALISM

# both can access, as static doesn't mean that object cannot access # it means that they are context-independent and non-polymorphic