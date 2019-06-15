class A:
    classvar1= "I am a class variable in class A."
    def __init__(self):
        self.var1 = "I am in class A's constructor."
        self.classvar1 = "Instance variable of class A"
        self.special = "Special"

class B(A):
    classvar1="I am in class B"
    classvar2 = "I am variable of class B"
    def __init__(self):
        #super().__init__()# as we call this then the values of var1 and classvar1 will change as per class A instance

        self.var1 = "I am in class B's constructor."
        self.classvar1 = "Instance variable of class B"
        # values of var1 and classvar1 will change again
        super().__init__() #as we call this then the values of var1 and classvar1 will change as per class A instance
        # if we comment 1st one then from here the values of var1 and classvar1 will not change

a = A()
b= B()

print(b.classvar1)
print(b.classvar2)
print(b.special,b.var1)