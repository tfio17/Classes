#
## Tom
#
## Unit 5 Assignment 1
#
#
## Deck of Cards Class
#

## Requirements:
#       Class for deck of cards
#           data for class will be the cards themselves
#           methods will be:
#
#               deal- method that returns the value of the card on top
#                       once dealt the card cannot be dealt again until
#                       the deck is shuffled
#
#               shuffle- method to return to the deck all dealt cards
#                       for a total of 52 (no Jokers) in random order
#
#               fan- method to simply list the cards in the deck, from
#                   top to bottom of the deck
#
#               isOrdered- method that returns True if the deck is in
#                           order and false if not in order
#                       - Note!!! - the deck does not need to be full
#                           to be in order
#
#               Order- method that sorts the deck so 2 of clubs low,
#                       ace of spades high, c,d,h,s for suits
#                   - Note!!! - order only done on full deck
#
#
## Let's Begin!!! ##

# get imports done, we will need these later
import random

class Card():

    cardCount = 0

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        Card.cardCount += 1

    def getcardCount(self):
        return Card.cardCount

    def show(self):
        print("{} of {}".format(self.face, self.suit))

    def getVal(self):
        suit_vals = {"Clubs": 1,
                     "Diamonds": 2,
                     "Hearts": 3,
                     "Spades": 4}
        face_vals = {'2': 2,
                     '3': 3,
                     '4': 4,
                     '5': 5,
                     '6': 6,
                     '7': 7,
                     '8': 8,
                     '9': 9,
                     '10': 10,
                     'Jack': 11,
                     'Queen': 12,
                     'King': 13,
                     'Ace': 14}
        val = int(suit_vals[self.suit]*face_vals[self.face])
        return val

    #def equals(self, nxt_card):

class Deck():
    
    deckCount = 0

    def __init__(self):
        self.cards = []
        self.initialize_deck()
        Deck.deckCount += 1
        
    def initialize_deck(self):

        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'Jack', 'Queen', 'King', 'Ace']

        for suit in suits:
            for face in faces:
                self.cards.append(Card(face,suit))


    def show(self):
        # this method is to check myself, will delete later maybe
        for card in self.cards:
            card.show()


    def shuffle(self):
        # we can think of cards[-1] as the "top" card cuz the deck is face down

        # this method will shuffle the deck
        #   first we iterate through our deck in reverse
        #   we generate a random value and swap card in
        #   position i with the card in position rand
        
        for i in range(len(self.cards)-1,0,-1):
            rand = random.randint(0,i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def deal(self):
        # we can think of cards[-1] as the "top" card cuz the deck is face down
        # we use the list method "pop(index)" to print a list item
        #   and then remove it from that list
        return self.cards.pop()

    def fan(self):
        for card in reversed(self.cards):
            card.show()

    def isOrdered(self):
        for i in range(len(self.cards)-2):
            nxt = i + 1
            card = self.cards[i]
            nxt_card = self.cards[nxt]
            if card.getVal() < nxt_card.getVal():
                i = i + 1
            else:
                return False

    def Order(self):
        while not self.isOrdered():
            for i in range(len(self.cards)-2):
                nxt = i + 1
                card = self.cards[i]
                nxt_card = self.cards[nxt]
                if card.getVal() < nxt_card.getVal():
                    self.cards[i], self.cards[nxt] = self.cards[nxt], self.cards[i]
                else:
                    print(i)
                    i = i + 1
                
                
            

# main

myDeck = Deck()
myDeck.shuffle()
print("***********************")
'''
myCard = myDeck.deal()
myCard.show()
myCard.getVal()
'''
print("***********************")
myDeck.fan()
print("***********************")
print(myDeck.isOrdered())
myDeck.Order()
print(myDeck.isOrdered())
myDeck.fan()
