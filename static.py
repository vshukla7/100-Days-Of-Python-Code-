# day 65

class math :
    def __init__ (self , num) :
        self.num = num
    def addtonum(self , x) :
        self.num = self.num + x
        return self.num
    @staticmethod
    def add(x , y) :
        return x + y
a = math(10) 
print(a.add(5 , 10))