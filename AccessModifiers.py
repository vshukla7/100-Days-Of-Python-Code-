# day 63

# now there are three types of the access modifiers in python 
# public access modifyers -- access publically 
# private access modifyers -- private for code 
# protected access modifyres  -- can accesee in parent and child class

# let's do it 

class  students ():
    def __init__(self):
        self.__name = "vinayak"

a = students ()
# print(a.__name) -- you can't access directlly 

# ?how to access 
# print(a._students__name) -- can access in this way 

#NOTE-- by single underscore you can't access directly and cant provide the full 
# any type of protection


