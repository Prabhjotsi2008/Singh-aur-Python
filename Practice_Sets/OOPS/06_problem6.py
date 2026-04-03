class Two_D:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        print("Inside 2-D Constructor")
    
    def get_vector(self):
        print(f"{self.i}i + {self.j}j")

    def __add__(self,other): # OPERATOR OVERLOADING
        return Two_D(self.i + other.i, self.j + other.j)
    
class Three_D(Two_D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
        print("Inside 3-D Constructor")
    
    def get_vector(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

    def __add__(self,other):
        return Three_D(self.i + other.i,self.j + other.j,self.k + other.k)

my_2d = Two_D(2,3)
my_2d.get_vector()

summed_2d = Two_D(2,2) + Two_D(-3,1)
summed_2d.get_vector()

my_3d = Three_D(4,5,6)
my_3d.get_vector()

summed_3d = Three_D(1,2,3) + Three_D(-4,5,6)
summed_3d.get_vector()