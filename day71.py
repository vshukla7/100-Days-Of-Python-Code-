# dir dict and help method 
# dict is a attribute of python

a = [1 , 2 , 3, 4 , 5]

# print(dir(a))
# print(a.__add__)

class Person:
    def __init__(self , name = None , age = None ):
        self.name = "John"
        self.age = 30


p = Person()
p.name = "vinayak"
p.age = 15
print(p.__dict__)

print(help(p))