har = ["harry","rohan","sagar","rajan","shivam"]
a = "this is a normal argument."
d = {"rohan":"monitor","sid":"cr","uday":"dr"}
def fun(nor,*ar,**kw):
    print(type(ar))
    print(type(nor))
    print(type(kw))
    print(kw,nor)
    print(ar[0])
fun(a,*har,**d)
def fun1(ar):
    print(type(ar))
    print(ar[0])
fun1(har)