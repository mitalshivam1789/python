var1 = 3
var2 = 7
if var1>var2:
    print("var1 is greater")
elif var2>var1:
    print("var1 is smaller")
else:
    print("both are equal")

l=[1,2,3,4,5]
if 4 in l:
    print("yes")
print(12 not in l)
v=input("age of the person: ")
v = int(v)
if v>7 and v<80:
    if v>18:
        print("yes, you can")
    elif v<18:
        print("no, you can not")
    else:
        print("we can't decide")
else:
    print("wrong age")