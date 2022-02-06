# A class is a blueprint for creating objects. A object has properties and methods

# Suppose "Human" is a class.
# "Name", "Gender"," Occupation" are the properties of the object of Human class.
# "Speak", "Do work", "Sleep" are the methods of the Human class.

class Human:
    def __init__(self,n,o):     # This method automatically get called whenever a object get created
        self.Name = n
        self.Occupation = o

    def DoWork(self):
        if self.Occupation == "Player":
            print(self.Name,": Plays Cricket")
        elif self.Occupation == "Actor":
            print(self.Name,": Shoots a film")

obj1 = Human("Tom Cruise","Actor")      #Object/ Instance of the class
print(type(obj1))
print(type(Human))
obj2 = Human("Virat Kohli","Player")



obj1.DoWork()
obj2.DoWork()

