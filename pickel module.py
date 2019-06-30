import pickle
#-------Pickeling a python object
#cars = ["audi","bmw","maruti suzuki","ferrari"]
#file="mycar.pkl"
#fileobj = open(file,'wb')
#pickle.dump(cars,fileobj)
#fileobj.close()

# - ----Pickeling object is created

# --------Depickeling the object

file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))