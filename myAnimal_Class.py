#
## Tom
#
## my Animal
#
## Class for animals to show polymorphism and inheritance

class Animal():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getWeight(self):
        return self.weight

    def setWeight(self,weight):
        self.weight = weight

    def speak(self):
        #print("Sound")
        pass


# main 
myAnimal = Animal("Bob", 40)
print(myAnimal.getName(),myAnimal.getWeight())


# Let's set up an example of inheritance
#   we want the Cat class to inherit the animal functionality
#   here we will add color, and reference animal

class Cat(Animal):

    def __init__(self, name, weight, color):
        Animal.__init__(self, name, weight)
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    # NOTE!!! All these methods have unique names! ...except

    # speak is overwriting the method in Animal, this is called polymorphism
    def speak(self):
        print("Meow!")

# main 2
cat1 = Cat("Felix",50,"black")
print(cat1.getColor(),cat1.getName())

cat1.speak()
