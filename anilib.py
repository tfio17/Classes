#
#
# Tom
#
# Review of classes
#

class Animal():

    aCount = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Animal.aCount += 1

    def getaCount(self):
        return Animal.aCount

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def speak(self):
        pass

    def __str__(self):
        aString = "AnimalObj:" + self.name + str(self.weight)
        return aString

    def __del__(self):
        print("An Animal has been destroyed: ",self.name)
        Animal.aCount -=1

class Cat(Animal):

    def __init__(self, name, weight, color):
        Animal.__init__(self, name, weight)
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def speak(self):
        print("Meow!")



class Dog(Animal):

    def __init__(self, name, weight, color):
        Animal.__init__(self, name, weight)
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def speak(self):
        print("Woof!")




