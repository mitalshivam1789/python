l=10 # hereit is global
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
def harry():
    x=20
    def rohan():
        global x
        x=88
    print("before",x)
    rohan()
    print("after",x)
harry()
print(x)