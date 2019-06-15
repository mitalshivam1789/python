def adddata(name):
    whattoadd = input("diet or exercise")
    details = input("what you what to add")
    f = open(name + whattoadd + ".txt", "a")
    f.write(details)
    f.close()


def retrievedata(name):
    whattoretrieve = input("diet or exercise")
    f = open(name + whattoretrieve  + ".txt")
    print(f.read())
    f.close()


def newfile(name):
    namearray.append(name)
    print(namearray)

whattodo = input("want to add or retrieve or add new")
name = input("enter name of the person")
namearray = ["harry", "shivam", "sagar"]
differentfun=["add","retrieve","add new"]
if name in namearray:
    if whattodo == differentfun[0]:
        adddata(name)
    elif whattodo == differentfun[1]:
        retrievedata(name)
elif name not in namearray:
    print(name)
    wanttoadd = input("did you want to add this name then press y :")
    if wanttoadd == "y":
        newfile(name)
if whattodo == differentfun[2]:
    newfile(name)
