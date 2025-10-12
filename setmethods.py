# i am in 11th and its very easy i already do this in my notebook and the syllabus is also same

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.union(s2))  # Union of two sets
print(s1.intersection(s2))  # Intersection of two sets

# by this the main sets will not change
print(s1 , s2)
# use update function to update a set 
s1.update(s2)
print(s1)

#s1 is updated mainly the set s2 is not changed the content get murged in s1
print(s2)
s3 = s1.update(s2)
print(s3) # it will print none because update function does not return any value it just updates the set           


disjoint = s1.isdisjoint(s2) 
# it will return false because both sets have common elements
print(disjoint)

issuuper = s1.issuperset(s2) 
# it will return false because s1 does not have all the elements of s2
print(issuuper)
         
remove = s1.remove(8)
# it will remove 8 from s1

discard = s1.discard(7)
# it will remove 7 from s1

# agar kisi set me element nahi hai to remove function error dega lekin discard function error nahi dega

pop = s1.pop()
print(pop)
print(s1)
# it will remove a random element from s1

del s2 # this will delete the set on the spot

#agar set nahi sirf values ko delete karna hai to 

clear = s1.clear()
print(s1)