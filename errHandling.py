# day 36 

a = input("enter a number")
print (f"the table of {a} is ")

try:
    a = int(a)
    for i in range (1,11):
        print(f"{a} x {i} = {a*i}")

except Exception as e: #method 1 
    print(e)

except ValueError: #method 2
    print("invalid input")

except TypeError: #method 3
    print("invalid input")
    
except: #mathod 4
    print("invalid input")


print("let us assume that this part of code must execute always")
print("end of code ...")


# code snippit example 

