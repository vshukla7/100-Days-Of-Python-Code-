# day 53 - map filter and reduce 


# map 
# filter 
# reduce    

# MAP - is used to apply any functiion to each item in an iterable and returns a map object
# after that we can convert that map obj in desired data type like list,tuple etc

# quick quiz make a simple programe which converts the list of the numbers into the list of the cube of the numbers

def cube(x): 
    return x**3

numbers = [1,2,3,4,5]
cubednumber = list(map(cube,numbers))

# print(cubednumber)


# FILTER - is used to filter the items in an iterable based on a condition and returns a filter object

def evenNumber(x):
    return x%2 == 0

numbers = [1,2,3,4,5]
evenNumbers = list(filter(evenNumber,numbers))
# print(evenNumbers)       


# REDUCE - is used to apply a function to each item in an iterable and returns a single value 

from functools import reduce
numbers = [1,2,3,4,5]
sumOfNumbers = reduce(lambda x,y:x+y,numbers)
print(sumOfNumbers)