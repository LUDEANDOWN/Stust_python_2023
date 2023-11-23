class ClassName:
    #variables 變數
    #functions 函式
    #constructor 建構子 最重要
    x=5

y=ClassName()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Name:{self.name}\nAge = {self.age}"


    def myfuns(self):
        print("Hello my name is "+self.name)
        
p1=Person("Jon",36)
p2=Person("ASS",38)
p1.age=60
del p1.age 
p1.age=70
print(y.x)

print("\n")

print(p1.name + " is " + str(p1.age) + " old ")
print(p1)

p2.myfuns()

class Pass:
    pass