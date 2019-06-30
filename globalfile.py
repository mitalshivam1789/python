l=10 # here it is global
def function1(n):
    l=5 # but here it is local though name of variable is same
    m=8
    l= l +45 # it works because we have l as local also. If we don't have l as local then it will through an error
    print(l,m)
    print(n,"m is local variable and can not be used outside it")
function1("value of l will not change for global")
print(l)
def function2(n):
    #l=5 # but here it is local though name of variable is same
    m=8
    global l # now we can chanfe value of l because global keyboard
    l= l +45 # it works because we have l as local also. If we don't have l as local then it will through an error
    print(l,m)
    print(n,"m is local variable and can not be used outside it")
function2("now l is global and value of global l will change")
print(l)

def harry():
    global x
    x=2
    print("before",x)

    def rohan():
        x = 88
    rohan()
    print("after",x)
    return x
y =harry()
print(y)
#x= 20
#print(x)