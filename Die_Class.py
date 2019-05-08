#
## Tom
#
#
## Learning Classes
#
# The die example


# ________________________ #

# First let's ask, what would a die have?
#
#       # of sides
#       a value, or the side facing up

# And what behavior?
#
#       well, you roll it
#       a way to see the face up side

# ________________________ #



# Ok let's give this a shot!

from random import randrange

class MyDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

# Main Program

d1 = MyDie(6)
print(d1.getValue())

d1.roll()
print(d1.getValue())

d2 = MyDie(20)
for i in range(20):
    d2.roll()
    print(d2.getValue())
