class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary= salary
        self.pincode = pincode


prabh = Programmer("Prabhjot",12000000,1234)
print(prabh.company,prabh.name,prabh.salary,prabh.pincode)