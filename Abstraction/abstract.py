from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod #decorator
    def moveForward(self):
        pass
    @abstractmethod
    def moveBackward(self):
        pass
    @abstractmethod
    def fm(self):
        pass

class Swift(Car):

    def moveForward(self):
        print("Swift Moving forward")

    def moveBackward(self):
        print("Swift Moving backward")

    def fm(self):
        print("Swift plying fm")


class Celerio(Car):

    def moveForward(self):
        print("Celerio Moving forward")

    def moveBackward(self):
        print("Celerio Moving backward")

    def fm(self):
        print("Celerio plying fm")

swift = Swift()
swift.moveForward()
