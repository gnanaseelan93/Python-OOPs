class Vehicle: #parent class / super class / base class 
    no_of_wheels = 4

    def moveForward(self):
        print("Vehicle is moving forward")


class Car(Vehicle):#child class / sub class / derived class / extended class
    no_of_airbags = 3


class Maruthi(Car):#child class / sub class / derived class / extended class
    mileage = 25.0

class Bike(Vehicle):#child class / sub class
    no_of_helmet = 2

class Suzuki(Car):#child class / sub class
    mileage = 30.0


class SuzukiMaruthi(Maruthi,Suzuki):#child class / sub class
    touch_screen=True

print("Single level inheritance")
#Single level inheritance
c = Car()
print(c.no_of_airbags)  # 3
print(c.no_of_wheels)  # 4
c.moveForward()  # Vehicle is moving forward

print("Hirahy level inheritance")
#Hirahy level inheritance
b=Bike()
print(b.no_of_helmet) # 2
print(b.no_of_wheels) # 4
b.moveForward() # Vehicle is moving forward

print("Multi level inheritance")
#Multi level inheritance
C2 = Maruthi()
print(C2.no_of_airbags)  # 3
print(C2.no_of_wheels)  # 4 
print(C2.mileage)  # 25.0
C2.moveForward()  # Vehicle is moving forward

#=============================Multiple inheritance======================================================

class Father:
 hairColor = "White"
    
class Mother:
    eyeColor = "Black"
    hairColor = "Black"

class Child(Father, Mother):
    num_of_legs = 2

#Multiple inheritance
print("Multiple inheritance")
ch = Child();
print(ch.hairColor) # Black
print(ch.eyeColor) # Black
print(ch.num_of_legs) # 2


#Diamond problem
print("Diamond problem")
SM = SuzukiMaruthi()
print(SM.mileage) # 40.0
print(SM.no_of_airbags) # 3
print(SM.no_of_wheels) # 4
