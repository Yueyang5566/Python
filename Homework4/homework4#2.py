import os
filename="file1.txt"
f = open(filename, "r")
if "password=" in f.read():
        print("The file is not safety!")
else:
        print("The file is safety!")
       
