class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
       # self.e = f"{fname}.{lname}@code.com" # when we change the fname then also the email will not change
       # to solve it we give it in return of the fun printemail

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    #def printemail(self):
    #    pass

    @property # this decorator helps to use this fun e as object or not as function
    def e(self):
        if self.fname==None or self.lname == None:
            return "Email is not set."
        return f"{self.fname}.{self.lname}@code.com"

    @e.setter # this decorator helps to set the fun email.
    def e(self,string):  # this fun help to change the values of fname and lanme as email changes
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @e.deleter
    def e(self):
        self.fname=None
        self.lname=None





supporter = Employee("hidustani", "supporter")
pandey = Employee("nikhil","raj")

print(supporter.e)

supporter.fname = "US" # if sarname changes
print(supporter.e)

supporter.e = "this.that@code.com" # this will not work without the setter function
print(supporter.fname)

del supporter.e  # we need a decorator to this as given above
print(supporter.e)
print(supporter.fname)