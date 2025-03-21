tup1 =(175, 75, 40)
print(tup1[0])

#merge
tup2 = (100,20,3,40,5,6,70,8,9,10)
print(tup2+tup1) 

#multiplication
print(tup2*3)

# lengh of list
print(len(tup1))

# append
#tup1.append(11) #error

# insert
#tup1.extend(tup2) #error

#tup1.insert(2, 100) #error

#clear
#tup1.clear() #error

#count
print(tup2.count(40))

#indexof
print(tup2.index(40))

#min and max
print(min(tup2))
print(max(tup2))

#shorting
#tup2.sort(reverse=True) #error

#mutability
#tup2[0]=1000 #error

#remove
#tup2.remove(20) #error

#POP( element delete)
#tup2.pop(0) #error

#slicing
print(tup2[2:5])
print(tup2[2:])
print(tup2[:5])

#reverse
print(tup2[::-1])
#output


#convert tuple to list

lst =list(tup1)
print(lst)

#convert list to tuple
tup =tuple(lst)
print(tup)

#single element tuple
tup3 =(1,)
print(tup3)

#example
fruits = ('apple', 'banana', 'cherry', 'dates', 'elderberry')
print(fruits)
fruits +=('fig',) #add fig to tuple fruits 
print(fruits)



#traverse tuple
#method 1
for i in range(len(fruits)):
    print(fruits[i])

#method 2
for i in fruits:
    print(i)

#slicing 
String = "Hello, World!"
print(String[2:5])    #output: llo
print(String[0:5:2])    #output: Hlo 


print(fruits[2:5]) #output: ('cherry', 'dates', 'elderberry')


#example 
numbers = [2,5,1,8,4]
print(numbers[1:4]) #output: (3, 4, 5)

numbers[2:4] = [3,7] #replace 1,8 with 3,7
print(numbers)