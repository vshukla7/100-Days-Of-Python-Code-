# A Libreary system which show the name of book avilable and their total no 

class library:
    def __init__(self , book):
         self.book = [book] 

    def bookTotal(self):
        print(f"the total no of books are {len(self.book)}")
        print("ANd the name of book is :")
        for noOFbooks in self.book:
            print(noOFbooks)

a = library("HOw to build a startup")

a.bookTotal()