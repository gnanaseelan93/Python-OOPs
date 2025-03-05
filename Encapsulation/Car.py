class Car:

    def __init__(self,carName,no_of_wheels, no_of_airbags,mileage):
        print("This is constructor")
        #private variable for carName
        self.__carName = carName
        self.no_of_wheels = no_of_wheels
        self.no_of_airbags = no_of_airbags
        self.mileage = mileage  


    def __del__(self):
        print("This is destructor",self)
            
    def __str__(self):
        return f"{self.__carName}({self.no_of_wheels},{self.no_of_airbags},{self.mileage})"   

    def moveForward(self,speed):
        print("Car is moving forward at speed of ",speed)

    def moveBackward(self):
        print("Car is moving backward")

#getter method
    def getCarName(self):
        return "car name is : "+ self.__carName

#setter method
    def setCarName(self,carName):
        self.__carName = carName

        
#create object car 1
c1 = Car("BMW",4,2,20)

#access private varibale out side the class 
print(c1.getCarName())

#change private varibale out side the class 
c1.setCarName("Benze")
print(c1.getCarName())

#create object car 2
c2 = Car("Suzuki",4,4,30)
print(c2.getCarName())

