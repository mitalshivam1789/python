ls = [i for i in range(100)] # this is comprehension
print(ls)
ls1 = [i for i in range(100) if i%3==0]
print(ls1)


#dict1 = {i: f"item{i}" for i in range(1,101) if i%3==0} # this is dict comprehension
dict1 = {i: f"item{i}" for i in range(5) } # this is dict comprehension
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)


dresses = {dress for dress in ["dress1","dress2","dress1"]}
print(dresses)
print(type(dresses))


events = (i for i in range(100) if i%2==0)
print(type(events))
print(events)
print(events.__next__())
print(events.__next__())
print(events.__next__())
print(events.__next__())
print(events.__next__())