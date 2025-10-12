class person :
    def __init__(self , name ,  role):
        print ("i execute all the time when i called")
        self.name = name
        self.role = role

    def info(self):
        print (f"{self.name} is a {self.role}")

# above code always returns the none value 

a = person("vinayak" , "homemade devloper")

a.info()
