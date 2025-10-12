dict = {
    "name" : "vinayak",
    "age" : 20,
    "gender" : "male",
    "role": "student",
    22 : "vinayak"
}
print(dict[22])

# we can give the corrosponding key to any value and it will print the corrosponding value like this -

print(dict["name"])
print(dict["age"])
print(dict["gender"])
# print the entire dictionary
print(dict)

# also can get the value of any key like this and use further 
print(dict.get("name"))

# -use in code 
if dict.get("role") == "student":
    print("he is a student and his name is ", dict.get("name"))
else:
    print("he is not a student")


# difference print(dict["age"]) and print(dict.get("age"))

# print(dict["height"]) 
# this will return the error because height is not a key

# print(dict.get("height"))      
# this will return the `none` because height is not a key

# Accessing multiple values from a dictionary
print(dict.keys())

for key in dict.keys():
    print(key)
