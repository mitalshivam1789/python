mode = input("what you want to do ")
d = {"what":"a question mode","while":"represent some time"}
print(d)
wanttodo=["add","search","delete"]
if mode == wanttodo[0]:
    x = input("enter world")
    y = input("meaning")
    d[x]=y
    print(d)
elif mode == wanttodo[1]:
    s= input("enter word")
    print(d.get(s))
elif mode == wanttodo[2]:
    de = input("which word you want to delete ")
    del d[de]