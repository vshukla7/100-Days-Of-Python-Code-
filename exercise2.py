#100 days of code with python exercise 1 - calculator

a = input("enter 1st no. ")
b = input("enter 2nd no. ")
c = input("enter operator ")

if c == '+':
    print(int(a)+int(b))
elif c == '-':
    print(int(a)-int(b))
elif c == '*':
    print(int(a)*int(b))
elif c == '/':
    print(int(a)/int(b))
else:
    print("Invalid operator")