import os
from datetime import datetime
#print(dir(os))
#print(os.getcwd()) # to get the current working directory
#os.chdir("C://") # changing current dir
#print(os.getcwd())
#print(os.listdir()) # give the list of all the files in the dir
#os.mkdir("directory_name") # use to make folder
#os.makedirs("dir1/dir2") # use to make directries means dir inside dir which is not in the folder
#print(os.listdir())
#os.rename("shivam.txt","code.txt") # use to rename a file only not a folder
#os.rmdir("directory_name") # delete the directory
#os.removedirs("dir1/dir2") # delete directories means dir inside dir
#print(os.listdir())
print(os.environ.get('Path'))
print(os.environ.get("HOME"))
#print(os.path.join("C://","\harry.txt"))
#print(os.path.exists("C://Program Files")) #checks either exists or not
#print(os.path.isdir("C://Program Files"))# use isfile to check file
#print(os.path.splitrxt("Program Files//file.txt"))#splits the extension and the file name
print(dir(os.path))
#print(os.stat("code.txt"))# use to print stat of the file
#print(os.stat("code.txt").st_size) # use to print the size of the file in bytes
#print(os.stat("code.txt").st_mtime) # gives the last time modified

#mod_time = os.stat("code.txt").st_mtime
#print(datetime.fromtimestamp(mod_time)) # way to get it in user readable form


#for dirpath, dirnames, filenames in os.walk("D://movies"): #to get the directories present in any folder
#    print("current path ", dirpath)
#    print("Directories ", dirnames)
#    print("files ",filenames)
#    print()




