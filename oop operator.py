class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name} standard is {self.std}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        #params=string.split("-")
        #print(params)
        #return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))# another way to do it or one line way
    @staticmethod
    def printgood(string):
        print("thi is ",string)

    def __add__(self,other):   # it is a dunder add method
        return self.salary + other.salary

    def __truediv__(self,other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee({self.name},{self.salary})"

    def __str__(self):
        return f"The name is {self.name} and salary is {self.salary}"
emp1 = Employee("harry",345,"Programmer")
emp2 = Employee("larry",45,"cleaner")

print(emp1+emp2)

print(repr(emp1))

print(str(emp2))
