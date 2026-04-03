class Vector:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        result = Vector(self.a + other.a, self.b + other.b, self.c + other.c)
        return result
    
    def __mul__(self, other):
        result = (self.a * other.a) + (self.b * other.b) + (self.c * other.c)
        return result
    
    def __str__(self):
        return f"{self.a}i + {self.b}j + {self.c}k"
    
    def __len__(self):
        return 3 # returning the dimensions of the vector i.e 3 in this case

v1 = Vector(1,2,3)
v2 = Vector(3,2,4)

print(f"Vector1: {v1}")
print("Dimensions of Vector1:",len(v1))
print(f"Vector2: {v2}")
print("Dimensions of Vector2:",len(v2))

v3 = v1 + v2
print(f"Vector2: {v3}")

dot_product = v1 * v2
print(f"Dot Product of v1 and v2 (v1.v2): {dot_product}")

print("Dimensions of Vector3:",len(v3))