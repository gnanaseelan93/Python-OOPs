class Car:

    def moveForward(self):
        print("Car is moving forward")

    def moveForward(self,speed):
        print("speed :",speed)    

'''
In Java method overloading -compail time polymorphism

int sum(int a,int b)
return a+b;

float sum(float a,flot b)
return a+b;

int sum (int a,int b,int c)
return a+b+c

sum(2,3)
sum(1,6,9)
sum(2.5,8.0)

'''    
#impliment overloading in python using *args. we can't directly do compail time polymorphism in python since here it taking dynamic data type 
#compail time polymorphism
class Summation:
    def summ(self,*args):
        ans=0
        for i in args:
            ans +=i
        return ans
    
s =Summation()
print(s.summ(6,8,6,8)) 


#Method overriting - Runtime polymorphism

class Father:

    def __init__(self):
        print("Father constructor")

    def sayHello(selft):
        print("Hello from father")

class child(Father):
    
    def __init__(self):
        print("Child constructor")

    def sayHello(self,name):
        print("Hello from child",name)

child =child()
child.sayHello("seelan")      


           
