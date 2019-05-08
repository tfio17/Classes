#
## Tom
#
#
## Learning Classes
#
# Polymorphism

## The cuckoo bird

# demonstrate polymorphism

class Animal:
    def __init__(self, name=''):
        self.name = name

    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print("Meow!\n")

class Dog(Animal):
    def talk(self):
        print("Woof!\n")


a = Animal()
a.talk()

c = Cat("Missy")
c.talk()

d = Dog("Rocky")
d.talk()
