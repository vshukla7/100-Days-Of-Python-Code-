# day 61 -- the inheretance in python which helps to make the 
# old class into a upgraded version 

class students:
    def __init__(self, name , id):
        self.name = name 
        self.id = id 

    def showdetails(self):
        print(f"the student name is {self.name} and his id is {self.id}");

class inheratedclass(students):
    def conformation(self):
        print("new inhereted class is created")

a = students("vianyak" , 3001)
b = inheratedclass("manas", 420 )

# a.showdetails()
# b.showdetails()
b.conformation()