day 49 -- file handling
file handling is built in in python

 recieve two arguments 1. file name 2. mode 
mode can be the w r or r or a
f = open("myfile.txt", "r")
text = f.read()
print(text)
f.close()

f = open("myfile.txt", "w")
f.write("hello world its 1st")
f.close()


f = open("myfile.txt", "a")
f.write("hello world")
f.close()

use r while opening the binarry files like the images





 