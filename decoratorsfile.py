def func(num):
    if num ==0:
        return print
    if num ==1:
        return sum
a = func(1)
print(a)
def exec(func):
    func("this")
exec(print)

def dec1(func1):
    def nowexe():
        print("executing now")
        func1()
        print("executed")
    return nowexe()

@dec1
def who_is_harry():
    print("harry is paakau")

#who_is_harry = dec1(who_is_harry)
who_is_harry()