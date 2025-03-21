#Function

def add():   
    print("Hello World")
    a=input("Enter the first number: ")
    b=input("Enter the second number: ")
    c=int(a)+int(b)
    print("The sum of the two numbers is: ",c)


#add()

#example 
def greet():
    name=input("Enter your name: ")
    print("Hello",name)

greet()


#type of functions

#1. Function with no arguments and no return value
def add():
    a=10
    b=20
    c=a+b
    print(c)

add()

#2. Function with arguments and no return value
def add(a,b):
    c=a+b
    print(c)

add(10,20)

#3. Function with no arguments and return value
def add():
    a=10
    b=20
    c=a+b
    return c

result=add()
print(result)

#4. Function with arguments and return value
def add(a,b):
    c=a+b
    return c

result=add(10,20)
print(result)

#5. Function with default arguments
def add(a=10,b=20):
    c=a+b
    return c

result=add() #a=10, b=20 #default value of a is 10 and b is 20  
print(result)

result=add(30) #a=30, b=20  #default value of b is 20
print(result)

result=add(30,40) #a=30, b=40 #default value of b is 40
print(result)

#6. Function with variable length arguments
def add(*a): #*a is a tuple
    c=0
    for i in a: #i is a variable
        c=c+i #c=0+10=10, c=10+20=30, c=30+30=60, c=60+40=100, c=100+50=150
    return c

result=add(10,20,30,40,50) #10,20,30,40,50 are arguments
print(result) #150 

result=add(10,20,30) #10,20,30 are arguments
print(result) #60

result=add(10,20) #10,20 are arguments
print(result) #30

#7. Function with keyword arguments
def add(a,b): #a=10, b=20
    c=a+b
    return c

result=add(b=20,a=10) #a=10, b=20
print(result) #30

#8. Function with keyword arguments and default arguments
def add(a=10,b=20): #a=10, b=20
    c=a+b
    return c

result=add(b=30) #a=10, b=30
print(result) #40

result=add(a=30) #a=30, b=20
print(result)   #50

result=add() #a=10, b=20
print(result)

result=add(30,40)   #a=30, b=40
print(result)

result=add(30)  #a=30, b=20
print(result)

result=add(30,40)
print(result)

#9. Function with keyword arguments and variable length arguments
def add(**a): #**a is a dictionary
    c=0
    for i in a.values(): #i is a variable
        c=c+i #c=0+10=10, c=10+20=30, c=30+30=60, c=60+40=100, c=100+50=150
    return c

result=add(a=10,b=20,c=30)  #a=10, b=20, c=30
print(result) #60

result=add(a=10,b=20) #a=10, b=20
print(result)   #30


#10. Function with keyword arguments and default arguments
print("Function with keyword arguments and default arguments")
def add(a=10,b=20,**c): #c is 40, d is 50
    e=0
    for i in c.values():
        e=e+i
    return e    

result=add(a=10,b=20,c=30,d=40) #a=10, b=20, c=30, d=40
print(result) #70


#11. Function with keyword arguments and variable length arguments
def add(**a): #**a is a dictionary
    c=0
    for i in a.values(): #i is a variable
        c=c+i #c=0+10=10, c=10+20=30, c=30+30=60, c=60+40=100, c=100+50=150
    return c

result=add(a=10,b=20,c=30)  #a=10, b=20, c=30
print(result) #60


#12. Function with keyword arguments and default arguments
def add(a=10,b=20,**c): #c is 40, d is 50
    e=0
    for i in c.values():
        e=e+i
    return e

result=add(a=10,b=20,c=30,d=40) #a=10, b=20, c=30, d=40
print(result) #70