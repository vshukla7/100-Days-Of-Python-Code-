# day 73 = dunder methods (also called magic methods) are special methods in Python that have double underscores at the beginning and end of their names. They allow you to define how your objects behave with built-in operations and functions. Here are some commonly used dunder methods:

class Point:
    name = "Point"
    def __len__(self):
        i = 0
        for i in self:
            i += 1
        return i
    
e = Point()
print(e) 