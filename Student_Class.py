#
## Tom
#
#
## Learning Classes
#
# The student example

# This program reads in student data, makes objects
#   of the students and then finds the best GPA

# A class to represent a student

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def QPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours


# A Function to take in stufent record and make an object of it

def makeStudent(infoStr):
    # infoStr is a tab seprated line w/ name, hours, qpoints
    # returns a student object

    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

# Main

def main():
    # open the input file for reading
    filename = input("enter the filename :")
    infile = open(filename, 'r')

    # set the best var to the first line
    best = makeStudent(infile.readline())

    # process file
    for line in infile:
        s = makeStudent(line)
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    # print the info to the screen
    print("The best student is ", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())

# Run
if __name__ == '__main__':
    main()
