set1 ={1,2,3,4,5,5,5}
print(set1)
print(type(set1))


#add
set1.add(6)
print(set1)

#update
set1.update([7,8,2])
print(set1)

#remove
set1.remove(8)
print(set1)

#discard
set1.discard(7)
#set1.discard(9) #no error

#pop
set1.pop()
print(set1)

#clear
# set1.clear()
# print(set1)

#copy
set2 = set1.copy()
print(set2)

#union
set3 = {2,11,12,13}
print(set1.union(set3))

#intersection
print(set1.intersection(set3))

#difference
print(set1.difference(set3))

#example
set4 = {1,2,3,4,5}
set5 = {4,5,6,7,8}
set6 = {1,2,3,4,5,6,7,8}

print(set4.union(set5).intersection(set6))