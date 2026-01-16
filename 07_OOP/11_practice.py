# BATTERY CLASS (BASE)
class Battery:
    def __init__(self,battery_size):
        self.__battery_size = battery_size
    
    def battery_info(self):
        return f"Battery Size: {self.__battery_size}"
    
    @property # better than getter # as we dont need to change the output printing syntax
    def battery_size(self):
        return self.__battery_size


# ENGINE CLASS (BASE)
class Engine:
    def __init__(self,engine_type):
        self.__engine_type = engine_type
    
    def engine_info(self):
        return f"Engine Type: {self.__engine_type}"
    
    @property
    def engine_type(self):
        return self.__engine_type


# CAR CLASS (BASE)
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    
    def car_info(self):
        return f"Car: {self.__brand} {self.__model}"
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model


# EV CLASS (DERIVED)
class EV(Car,Battery):
    def __init__(self,brand,model,battery_size):
        Car.__init__(self,brand,model)
        Battery.__init__(self,battery_size)
    
    def car_info(self):
        return f"EV: {self.brand} {self.model} {self.battery_size}"


# NonEV CLASS (DERIVED)
class NonEV(Car,Engine):
    def __init__(self,brand,model,engine_type):
        Car.__init__(self,brand,model)
        Engine.__init__(self,engine_type)
    
    def car_info(self):
        return f"Gasoline-Car: {self.brand} {self.model} {self.engine_type}"


my_ev = EV("Tesla","S","85kWh")
print(my_ev.car_info())
print(my_ev.battery_info())


my_non_ev = NonEV("Ford","Mustang","V8")
print(my_non_ev.car_info())
print(my_non_ev.engine_info())

my_non_ev.__model = "test" # doesn't give any error # but also doesn't do anything # as model is read-only by @property
print(my_non_ev.model) # still same # Mustang # using model method (which is a attribute using @property)