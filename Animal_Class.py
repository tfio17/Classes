#
## Tom
#
#
## Learning Classes
#
# The animals example

## The concept of inheritance

# Here we have a class for any animal

class Animal:
    animalCount = 0

    
    def __init__(self, name, weight):
        self.name = name
        self.weight = float(weight)
        Animal.animalCount +=1

    def talk(self):
        pass

    def getAnimalCount(self):
        return Animal.animalCount

    def getCount(self):
        pass

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = float(weight)

    def __del__(self):
        print("\n\n Animal has been removed!\n")
        Animal.animalCount -=1


# Now lets use inheritance to create a class for a dog

class Cat(Animal):
    
    catCount = 0
    
    def __init__(self, name):
        Animal.__init__(self, name, weight)
        self.cathater = cathater
        cat.catCount += 1

    def talk(self):
        print("\nMeow!\n")

    def getCount(self):
        print("The number of cats is: ", Cat.catCount)

    def __del__(self):
        print("\n\n Congrats! A cat has been removed!\n")
        Cat.catCount -=1
        
# -------------------------------- #

class Dog(Animal):

    dogCount = 0
    
    def __init__(self, name, weight, cathater):
        Animal.__init__(self, name, weight)
        self.cathater = cathater
        Dog.dogCount += 1

    def talk(self):
        print("\nWoof!\n")

    def getCount(self):
        print("The number of dogs is: ", Dog.dogCount)

    def getCathater(self):
        return self.cathater

    def setCathater(self, cathater):
        self.cathater = cathater

    def __del__(self):
        print("\n\n Nooooo! A dog has been removed!\n")
        Dog.dogCount -=1


# Main Program

def main():
    a = Animal('Joe', 200)
    print(a.getWeight())

    print(a.getWeight())
    a.setWeight(100)
    print(a.getWeight())

    b = Dog('Fido',300,False)
    print(b.getCathater())
    print(b.getName())
    print(b.getWeight())

    # more

    c = Cat("Belarus", 15)
    c.talk()

    print("Number of Cats: ", Cat.catCount())
    print("Number of Dogs: ", Dog.dogCount())

    b.talk()
    print("Number of Cats: ", Cat.catCount())
    print("Number of Dogs: ", Dog.dogCount())

    #del b
    print("Number of Cats: ", Cat.catCount())
    print("Number of Dogs: ", Dog.dogCount())

    e = Cat("Fluffy")
    e.talk()
    print("Number of Cats: ", Cat.catCount())
    print("Number of Dogs: ", Dog.dogCount())
    

if __name__ == '__main__':
    main()

