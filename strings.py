#string methods and functions

name = "Vinayak Shukla"

print(name.upper()) #make string uppercase
print(name.lower()) #make string lowercase
print(name.swapcase()) #swap case of string

print(name.startswith("V")) #check if string starts with given
print(name.endswith("a")) #check if string ends with given

print(name.find("a")) #find index of given string
print(name.index("a")) #find index of given string and raise error if not found

print(name.replace("a", "x")) #replace given string with given

print(name.split(" ")) #split string into list with given separator
print(name.join(["A", "B", "C"])) #join list into string with given separator

