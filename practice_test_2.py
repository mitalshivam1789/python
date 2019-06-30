n= int(input("number of apples you have "))
mn = int(input("minimum students "))
mx = int(input("maximum students "))
try:
    for i in range(mn,mx+1):
        if n%i==0:
            print("total no of apples each student will get ",i/n)

        else:
            print("each student will not get equal no of apples.")

except Exception as e:
    print(e)