class Student:
    pass
harry = Student()
larry = Student()

print(harry,larry)
harry.name = "harry"
harry.std = 12
larry.name = "larry"
print(harry.name,larry.name)
class Employee:
    no_of_leaves=8
    pass
harry1=Employee()
larry1=Employee()
harry1.name = "harry"
harry1.std = 12
larry1.name = "larry"
larry1.std = 11
print(Employee.no_of_leaves)
Employee.no_of_leaves=9
print(Employee.no_of_leaves)
print(harry.__dict__)
print(Employee.__dict__)
harry1.no_of_leaves = 10
print(harry1.__dict__)
print(Employee.no_of_leaves)

class Employee1:
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

harry2=Employee1("harry1",244,"instructor")
larry2=Employee1("larry1",234,"sales")
print(harry2.name)
larry2.change_leaves(34)
print(harry2.no_of_leaves)
Employee1.change_leaves(54)
print(larry2.no_of_leaves)
karan = Employee1.from_dash("karan-299-student")
print(karan.salary)
Employee1.printgood("raman")
#harry2.name = "harry"
#harry2.std = 12

#print(harry2.printdetails())


