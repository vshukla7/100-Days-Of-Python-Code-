# Instance variables vs Class variables in Python day 66

class employee:
    company = "google"  # class variable]
    employeeCount = 0  # class variable
    def __init__(self, name, salary, role):  # constructor
        self.name = name  # instance variable
        self.salary = salary  # instance variable
        self.role = role  # instance variable
        employee.employeeCount += 1

emp1 = employee("harry", 100, "instructor")
emp2 = employee("rohan", 200, "student")

print(emp1.salary)  # 100
print(emp2.salary)  # 200

print(emp1.name)  # harry
print(emp2.name)  # rohan   

print(emp1.company)  # google
print(emp2.company)  # google

