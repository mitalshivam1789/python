def adddata(name):
    whattoadd = input("diet or exercise")
    details = input("what you what to add")
    if whattoadd == "diet":
        diet(name)
    elif whattoadd == "exercise":
        exercise(name)
    f=open(name + whattoadd +".txt","a")
    f.write(details)
    f.close()
def retrievedata(name):
    whattoretrieve = input("diet or exercise")
    if whattoretrieve == "diet":
        diet(name)
    elif whattoretrieve == "exercise":
        exercise(name)
    f=open(name + whattoretrieve +".txt","a")
    print(f.read())
    f.close()
def newfile(name):

    whattoadd = input("diet or exercise")
    details = input("what you what to add")
    if whattoadd == "diet":
        diet(name)
    elif whattoadd == "exercise":
        exercise(name)
    f=open(name + whattoadd +".txt","a")
    f.write(details)
    f.close()

whattodo = input("want to add or retrieve or whant to add new file")
namearray=["harry","shivam","sagar"]
if whattodo == "add":
    name = input("enter name of the person")
    adddata(name)
elif whattodo == "retrieve":
    name = input("enter name of the person")
    retrievedata(name)
elif whattodo == "new file":
    name = input("enter name of the person")
    newfile(name)

