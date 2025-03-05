class Car:

    def __init__(self,carName,no_of_wheels, no_of_airbags,mileage):
        print("This is constructor")
        self.carName = carName
        self.no_of_wheels = no_of_wheels
        self.no_of_airbags = no_of_airbags
        self.mileage = mileage  


    def __del__(self):
        print("This is destructor",self)
            
    def __str__(self):
        return f"{self.carName}({self.no_of_wheels},{self.no_of_airbags},{self.mileage})"   

    def moveForward(self,speed):
        print("Car is moving forward at speed of ",speed)

    def moveBackward(self):
        print("Car is moving backward")


#create object car 1
c1 = Car("BMW",4,2,20)
print(c1)
c1.moveForward(100)
c1.moveBackward()

#create object car 2
# c2 =Car("Suzuki",4,4,30)
# c2.moveForward(75)

