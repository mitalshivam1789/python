import time
initial = time.time()
k=0
while(k<50):
    print("this is in whileloop")
    k+=1
print(time.time() - initial)
initial2 = time.time()
for i in range(50):
    print("now it is in for loop")
print(time.time() - initial2)