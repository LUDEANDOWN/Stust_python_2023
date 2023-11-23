class Person:

    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def talk(self):
        print("Hi I'm "+self.name )

    def vote(self):
        if self.age<18:
            print("I am not eligble to vote")
        else:
            print("I am eligible to vote")


obj=Person("Sam","Male",10)

obj.talk()
obj.vote()

