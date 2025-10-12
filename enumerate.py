# day 42
mark = [12, 56, 98 , 11 , 0]

index = 0 

for marks in mark:
    print(marks)
    if(index==2):
        print("vinayak to topper hai")
    index +=1

 # ab ye enumerate kya hai 
 # ye ek built in python function hai jo ek hi time per hame 
 # value ke saat sath index ko return karta hai

for index , marks in enumerate(mark):
    print(index , marks)

# we can start the enumerate index from any value 
for index , marks in enumerate(mark , start = 1):
    print(index , marks)