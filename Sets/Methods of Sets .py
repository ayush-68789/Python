new_set = eval(input())

new_set.add(8)
print("Added : ", new_set)

new_set.remove(8)
print("Removed : ",new_set)

another_set = {3, 4, 5, 6, 7}
union = new_set.union(another_set)
print("union : ",union)

intersection = new_set.intersection(another_set)
print("intersection of sets : ",intersection)

'''
TERMINAL : 

{1,2,3,4,5}
Added :  {1, 2, 3, 4, 5, 8}
Removed :  {1, 2, 3, 4, 5}
union :  {1, 2, 3, 4, 5, 6, 7}
intersection of sets :  {3, 4, 5}        (if intersection is not found it returns --> set()   )

