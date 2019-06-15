class Employee:
    no_of_leaves=8
    _protected =49
    __private = 432
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name} salary is {self.salary}"

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

class Programmer (Employee):
    noofholidays = 56
    def __init__(self,aname,asalary,arole,language):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = language

    def printprog(self):
        return f"The Programmer's name is {self.name}. Salary is {self.salary} and role is {self.role}."

class player:
    noofgames=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"Yhe name is {self.name} and game is {self.game}"

class Coolprogrammer(Employee,player):
    pass


harry2=Employee("harry1",244,"instructor")
larry2=Employee("larry1",234,"sales")

shubham = Programmer("Shubham",933,"programmer",["python"])
print(shubham.noofholidays)
print(shubham.languages)

carbon = player("acrbon",["cricket"])
rohan = Coolprogrammer("rohan",9999,"Coolprog")

det = rohan.printdetails()
print(det)
ppp=Employee("rakesh",324,"friend")
print(ppp._protected)
print(ppp._Employee__private) #way to access private variable.