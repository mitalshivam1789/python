"""
Iterable -  __iter__() or __getitem__()
Iterator -  __next__()
Iteration

generators type of iterator which can be iterate only once like range fun
yield keyword - generate on the fly
"""
def gen(n):
    for i in range(n):
        yield i

g = gen(3)
#print(g.__next__())
#print(g.__next__())
#print(g.__next__())
#print(g.__next__())
for i in g:
    print(i)

h ="shiv"
#for c in h:
 #   print(c)

it = iter(h)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
#print(it.__next__())