class Employee:
    amt = 1000 # HARRY-WAY

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def increment(self,amt): # MY-WAY
        if amt <= 0:
            print("Invalid Salary entered...")
            return
        self.salary += amt
        print(f"Updated Salary: {self.salary}")
    
    @property #HARRY-WAY
    def salary_after_increment(self):
        return self.salary + Employee.amt
    
    def display_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

emp1 = Employee("Prabhjot Singh",60000)
emp1.display_info()
emp1.increment(5600)
emp1.display_info()
emp1.increment(-1000)
emp1.display_info()

print(emp1.salary_after_increment)