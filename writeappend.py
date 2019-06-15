"""
if we write an existing file then it will replace everthing in it and write what ever we write in it.
append adds the content in the file.
if there is no existing file the the write function also make the new file.
"""
f= open("shivam1.txt","w")
f.write("now i now how to write in file.")
f.close()
f = open("shivam1.txt","w")
f.write("this proves above statement.")
f.close()
f=open("shivam1.txt","a")
a=f.write("\nthis append the file.\n")
f.close()
print(a)# it prints no of characters we write in the file.
f=open("shivam1.txt","r+")#"r+" is used to open file in both read and write mode
print(f.read())
f.write("thaks for it")
f.close()
y = "shivam1"
f =open(y+".txt","r")
print(f.read())
f.close()