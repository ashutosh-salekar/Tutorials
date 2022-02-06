# The capability of a class to derive properties and characteristics from another class is called Inheritance. 
# In Inheritance there is a concet of parant class and child class. The child class can access behaviour of parent classes.

# class Child Class(Parant Class):

class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Hi.. I am {self.name} and I am {self.age} years old.")

    def justPet(self):
        print("Calling Parent method by child object.")

    def same(self):
        print("I am parent method.")

class Cat(Pet):        
    def speak(self):
        print("Meow")

    def same(self):
        super().same()
        print("I am child method.")

class Dog(Pet):
    def speak(self):
        print("Bark")

c = Cat("Bill",3)
d = Dog("kit",4)
c.speak()
d.speak()

# A child class can access the methods of parant. If child class
c.justPet()     
d.justPet()

# If child and parant class have methods with same name then using "super" keyword a child class can access the parant method.
c.same()