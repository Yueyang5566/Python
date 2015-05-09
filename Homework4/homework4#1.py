import os
import fnmatch
print("Current Direcotry:",os.getcwd())
print("The file name could be: fortune1.txt,fortune2.txt,fortune3.txt,fortune4.txt,fortune5.txt,fortune6.txt,fortune7.txt,fortune8.txt,fortune9.txt,fortune10.txt,fortune11.txt,fortune12.txt,fortune13.txt,fortune14.txt,fortune15.txt,fortune16.txt,fortune17.txt,fortune18.txt.")
file=input("Trying to find the file name:")
start_dir="fortune1"
for dirpath, dirs, files in os.walk(start_dir):
    for single_file in files:
        if fnmatch.fnmatch(single_file,file):
            print("Finding......", file)
            print(os.path.join(dirpath, single_file))
       
