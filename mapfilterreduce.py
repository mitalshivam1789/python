lis = ["1","2","5","3","4"]
num = list(map(int,lis))
print(num,type(num),lis)
def sq (a):
    return a*a
square = list(map(sq,num))
print(square)
sqr = list(map(lambda x: x*x,num))
print(sqr)
def sqr1(a):
    return a*a
def cube(a):
    return a*a*a
func = [sqr1,cube]
for i in range(5):
    val = list(map(lambda x : x(i),func))
    print(val)
list1 =[1,2,3,5,6,7,4,54,6,3,66,0]
def greater(num):
    return num>5
gr = list(filter(greater,list1))
print(gr)

from functools import reduce
list2 =[1,2,3,4]
num = reduce(lambda x,y:x+y,list2)
print(num)