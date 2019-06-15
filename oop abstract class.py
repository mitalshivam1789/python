from abc import ABCMeta, abstractmethod
#from abc import ABC, abstractmethod # it can also done using this. in this at place of metaclass= only ABC is sufficient.
class Shape(metaclass= ABCMeta):  # due to this class it makes to add printarea fun compulsory in the class which inherits this class to be their
    @abstractmethod  #this is the reason to add printarea fun compulsory
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breath = 7

    def printarea(self):
        return self.length * self.breath


rect1 = Rectangle()

#ob = Shape()  #we can't create object of abstract file
