me = "harry"
al = "ok"
a = "he is %s %s"%(me,al) #this is string formating
print(a)
a = "THAT PERSON IS  {} {}"
b=a.format(me,al) # this is dot formating
print(b)
a = "THAT PERSON IS  {1} {0}" # we can decide the position
b=a.format(me,al)
print(b)
c = f"who is {me} {al}." # this is f string method
print(c)