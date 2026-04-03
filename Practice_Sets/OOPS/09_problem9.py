class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def display(self):
        print(f"{self.r} + {self.i}i")
    
    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)
    
    def __mul__(self, other):
        return Complex((self.r * other.r) - (self.i * other.i), (self.r * other.i) + (self.i * other.r))
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1,2)
c2 = Complex(4,3)
c3 = c1 * c2

c3.display()

c4 = c3 + c1
print(c4) # possible due to __str__ method