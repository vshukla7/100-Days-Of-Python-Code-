# super keyword 

class parentclass:
    def __init__(self):
        print("this is parent class constructor")
    
    def parentmethod(self):
        print("this is parent class method")

class childclass(parentclass):
    def __init__(self):
        super().__init__()
        print("this is child class constructor")
    
    def childmethod(self):
        super().parentmethod()
        print("this is child class method")

c = childclass()
c.childmethod()
