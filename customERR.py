# day 38 -- about custom errors

a = int(input("enter a number between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("enter a number between 5 and 9")

else:
    print("valid input")

# we create errors in python by raise keyword
# we can also create custom errors 


# defining custom exceptions in python

