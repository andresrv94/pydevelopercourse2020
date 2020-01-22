#Testing classes

class Dog:
    def __init__(self,name,colour,age):
        self.name=name
        self.colour=colour
        self.age=age
    
    def bark(self):
        print("Woof!!")
    
    def description(self):
        print(f"The dog\'s name is {self.name}, it's {self.colour} and is {self.age} years old")


dog1 = Dog("tito","gray","14")

dog1.bark()
dog1.description()
