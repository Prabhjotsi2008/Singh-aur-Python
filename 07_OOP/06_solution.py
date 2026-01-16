<<<<<<< HEAD
# ClASS VARIABLE
=======
# POLYMORPHISM # ANEK-ROOP
>>>>>>> 990fc99fadf8576eebf5f03c42e394e1f2ee729a

class Car:
    total_car = 0 # made a varible for car-count
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car +=1 # use instead of self.total_car, in order to update values # self.total_car will not update total_car 
        # self refer to current context (the object created from class, not the class itself)
        # Class_name (Car in this case) refer to the Class itself (blueprint), not to the current-context(Object created from Class)

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



tesla = ElectricCar("Tesla","S","85kWh")
print(tesla.car_info())
print(tesla.fuel_type()) # Electric Charge
print(tesla.total_car) # 1

safari = Car("Tata","Safari")
print(safari.car_info())
print(safari.fuel_type()) # Pertol or Deisel
print(safari.total_car) # 2

nexon = Car("Tata","Nexon")
print(nexon.car_info())
print(nexon.fuel_type()) # Pertol or Deisel
print(nexon.total_car) # 3


# ACCESING USING CLASS (CAR), NOT OBJECTS OF THE CLASS
test = Car("test","test")
print(Car.total_car) # 4 # we can access directly through Car (CLASS) # it is a better practice