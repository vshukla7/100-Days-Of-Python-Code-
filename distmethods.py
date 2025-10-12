# here in day 34 lets lern about dist methods

ep1 = {122:"vinayak" , 123:"vivek" , 124:"manas"}
print(ep1)
ep2 = {125:"rohit" , 126:"shubham" , 127:"ashish"}

ep1.update(ep2)
print(ep1)

ep1.pop(123)
print(ep1)

ep1.popitem()       # revok last element
print(ep1)

# ep1.clear()

del ep1 #delete entire dictionary
del ep1[122] #delete specific element 