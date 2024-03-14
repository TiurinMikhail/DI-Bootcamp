# Part 1 : Quizz :

# What is a class?
# It is a blueprint for Creating objects which are in the same class

# What is an instance?
# An instance is a specific occurrence of a class

# What is encapsulation?
#Encapsulation is the bundling of data and methods that operate on the data into a single unit, often referred to as a class

# What is abstraction?
# Abstraction in object-oriented programming (OOP) is the concept of simplifying complex systems by
# focusing on essential characteristics while hiding unnecessary details. It allows programmers to represent real-world objects more effectively by defining their essential properties and behaviors without concerning themselves with the internal implementation details

# What is inheritance?
# We could make subclasses, which inherit all default things from mother class

# What is multiple inheritance?
# The same as inheritance but now- one subclass can inherit from two or more mother classes


# What is polymorphism?

#Polymorphism allows objects of different classes to be treated as objects of a common superclass, enabling them to be used
# interchangeably


# What is method resolution order or MRO?
# Method Resolution Order (MRO) defines the order in which methods are resolved in a
# class hierarchy, especially in the context of multiple inheritance

# ----------------------------------------------------------------------------------------------

# Part 2: Create A Deck Of Cards Class.
import random as rd

class Card:
    suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
    value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J','Q','K']
    def __init__(self, suit, value):
        self.suit = suit.lower().capitalize()
        self.value = value.upper()

    def __str__(self):
        return f'{self.value} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = [Card(suit,value) for suit in Card.suits for value in Card.value]
        # for suit in Card.suits:
        #     for value in Card.value:
        #         self.cards.append(Card(suit, value))

    def __str__(self):
        list_cards = []
        for card in self.cards:
            list_cards.append(str(card))
        return '\n'.join(list_cards)

    def shuffle(self):
        if len(self.cards) == 52:
            rd.shuffle(self.cards)

    def deal(self):
        # random_card = rd.choice(self.cards)
        # print(str(random_card))
        if len(self.cards) == 0:
            print('The deck is over!')
        else:
            print(self.cards[0])
            self.cards.remove(self.cards[0])

deck1 = Deck()
print('--------------------')
deck1.shuffle()
print(deck1)

print('---------------------')

for _ in range(52):
    deck1.deal()
    print(len(deck1.cards))