#
## Tom
#
#
## Learning Classes
#
# The Super class!

## Class variables, deconstructors, Override functions

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def getName(self):
        print(self.name)

    def getSalary(self):
        print(self.salary)

    def getEmpCount(self):
        print(Employee.empCount)

    def __del__(self):
        Employee.empCount -=1
        className = self.__class__.__name__
        print("An instance of", className, " was destroyed")

    def __str__(self):
        strname = "name:"+self.name+"-salary:"+str(self.salary)
        return strname


# ------------------------------ #

# main

a = Employee("Lars", 35000)
b = Employee("Fred", 50000)
c = Employee("Joe", 75000)

c.getEmpCount()

# decon

del c
a.getEmpCount()

# test overriding

MyString = 'lars'
print(str(MyString))

print(str(a))
d = Employee("julie",83000)
print(str(d))

'''

Class Variables --
        variables that can be accessed across objects that came
        from that class.  Class variables are often altered in
        constructors and deconstructors and can also be used to
        send messages between objects.

Deconstructors --
        The opposite of contructors.  This method is run when an
        object is deleted.

Overriding functions --
        When an inherited function does not have the desired
        behavior we can write our own function with the same
        name, telling Python that "If I instantiate an object
        with this class and you run this method use mine and
        not the inherited."

'''






