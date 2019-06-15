f= open("shivam.txt")
print(f.tell())# tells where is the pointer
print(f.readline())
print(f.tell())
f.seek(10)# takes the pointer to the defined point
print(f.readline())
f.close()
with open("shivam.txt") as f:
    a=f.read(5)
    print(a)
f=open("shivam.txt")
print(f.readline())
f.close()