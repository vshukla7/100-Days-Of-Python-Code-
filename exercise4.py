# day 40 -- secret code language 

input = input("enter the string : ")

output = ""
for char in input:
    if char == " ":
        output += ":"
    else:
        output += str(ord(char.lower())-97)
print(output)
