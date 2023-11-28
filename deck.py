# deck.py
import random
import pygame

# class represents individual playing cards, assigning values to each card based on Blackjack rules.
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self._assign_value()
        self.image = self._assign_image()

    def _assign_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'Ace':
            return 11  # Will be adjusted to 1 if necessary in hand evaluation
        else:
            return int(self.rank)
        
    def _assign_image(self):
            x = 'Assets/cards/' + self.rank + self.suit + '.png'
            imageResized = pygame.image.load(x)
            x = pygame.transform.scale(imageResized, (100, 140))
            return x

#class represents a deck of cards, allowing you to build a full deck, shuffle it, deal cards, and reset the deck.
#The deck is built by looping through the suits and ranks, creating a Card object for each combination.
#The shuffle method uses the random module to shuffle the deck.
#The deal_card method removes a card from the deck and returns it.
#The reset_deck method clears the deck and rebuilds it, then shuffles it.
class Deck:
    def __init__(self):
        self.cards = []
        self._build_deck()
        self.shuffle()

    def _build_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def reset_deck(self):
        self.cards = []
        self._build_deck()
        self.shuffle()