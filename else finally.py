f1=open("shivam.txt")

try:  # try to do some work
    f = open("does.txt")  # try to open file does
    #f2 = open("shivam1.txt") # if only this is present then else fun will run
except Exception as e: # if try fun fails or gives any error then exception fun will run
    print(e)
    print("we are in exception fun")
# their are many different error fun and we can make different error error fun more then one


else:  # if fun exception fun does not run then this fun will run and if exception fun runs then it will not run
    print("This will run only when if except is not running.")

finally:   #it will run at any cost
    print("run this anyway....")
    f1.close()