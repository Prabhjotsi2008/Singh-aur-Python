class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def sound():
        print("Dog Barks...")

dog = Dog()
dog.sound()