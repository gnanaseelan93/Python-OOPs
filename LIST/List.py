 

LIST1 = [1,2,3,4,"HIU"]
print(LIST1[-1])

#merge
LIST2 = [100,20,3,40,5,6,70,8,9,10]
print(LIST2+LIST1)

#multiplication
print(LIST2*3)

# lengh of list
print(len(LIST2))

# append
LIST1.append(11)
print(LIST1)

# insert
LIST1.extend(LIST2)
print(LIST1)

LIST1.insert(2, 100)
print(LIST1)

#clear 
LIST1.clear()
print(LIST1)

#count
print(LIST2.count(2))

#indexof 
print(LIST2.index(20))

#min and max
print(min(LIST2))
print(max(LIST2))

#shorting 
print('before shorting',LIST2)
LIST2.sort(reverse=True)
print('after shorting',LIST2)

#mutability
LIST2[0]=1000
print(LIST2)

#remove
LIST2.remove(20)
print(LIST2)


#POP( element delete)
LIST2.pop(0) #if 0 is not given then it will remove last element
print(LIST2)



