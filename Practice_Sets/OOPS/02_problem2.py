class Calculator:
    def __init__(self,num):
        self.num = num
        print(f"The Number is {self.num}")
    
    def square(self):
        print(f"Sqaure of {self.num}: {self.num**2}")
    
    def cube(self):
        print(f"Cube of {self.num}: {self.num ** 3}")
    
    def square_root(self):
        print(f"Square root of {self.num}: {(self.num ** 0.5):.2f}")


calc = Calculator(5)

calc.square()
calc.cube()
calc.square_root()