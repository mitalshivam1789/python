# file IO basics
"""
"r"  open file for reading default mode
"w"  open file for writing
"x"  creates file if not exists
"a"  add more content to a file
"t"  text mode   default mode
"b"  binary mode
"+"  read and write

"""
f = open("shivam.txt","rt")
content = f.read()
print(content)
f.close()
f=open("shivam.txt")
content1 = f.read(10)
print(content1)
f.close()
f = open("shivam.txt")
content = f.readline()
content = f.readline()
print(content)

f.close()
f= open("shivam.txt")
print(f.readlines())
f.close()
f= open("shivam.txt")
#content = f.read()
for line in f:
    print(line)
#for line in content:
#    print(line)