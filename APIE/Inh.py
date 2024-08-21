class Car:
    def __init__(self,type) :
        self.type = type

    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)

Car1 = ToyotaCar("Fortuner","diesel")
Car2 = ToyotaCar("Prius","electric")

print(Car1.type)  
print(Car2.type)