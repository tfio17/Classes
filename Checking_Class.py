#
# Tom
#
# Checking Class
#

class checking:

    # Constructor
    def __init__(self, amt):
        print("You have created a checking account")
        self.balance = amt

    # getter for balance
    def getBalance(self):
        return self.balance

    # deposit method
    def deposit(self, amt):
        self.balance += amt
        print("The new balance is ", self.balance)

    # cut a check
    def cutCheck(self, amt):
        if amt > self.balance:
            print("Insufficent funds")
        else:
            self.balance -= amt
            print("You have cut a check for: ", amt)


# main
# create a variable called acct defined as a checking object, where amt=500
my_acct = checking(500)

# print balance
print(my_acct.getBalance())

# another account! Because checking is just a blueprint!
ur_acct = checking(1000)
print(ur_acct.getBalance())

# let's deposit some more money... in my account of course
my_acct.deposit(400)
print(my_acct.getBalance())

# Let's try cutting a check for too much money
my_acct.cutCheck(1000)

# Shit... well let's try that again
my_acct.cutCheck(200)
print(my_acct.getBalance())

# do we really need to use getBalance method?
print(my_acct.balance) # nah that is more of a convention so you can protect stuff



