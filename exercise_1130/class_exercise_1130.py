class Cars:

    def __init__(self,color,seat):
        self.color=color
        self.seat=seat

    def drive(self):
        print(f"My car is {self.color} and {self.seat} seats.")

class Motorcycle:
    pass

mazda = Cars("blue",3)
print(isinstance(mazda, Cars))
print(isinstance(mazda, Motorcycle)) 