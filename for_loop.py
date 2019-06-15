l=[["harry",1],["larry", 2],["carry", 8],["marie", 47]]
for item in l:
    print(item)
    print(item[1])
for item,value in l:
    print(item,value)
x = dict(l)
print(x)
for y,z in x.items():
    print(y)
    print(y,z)