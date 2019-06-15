x = input("write here")
print(x)
y = input(" what you want to search?")
z=[len(y),x.count(y),x.index(y),len(y),0,0]

print(z)
for i in range(x.count(y)):
    #print(i)
    z[2]= x.index(y,z[4])
    z[5]=z[2]+z[3]
    print(x[z[2]:z[5]],z[2],z[5],z[4])
    z[4]=z[2]+1
