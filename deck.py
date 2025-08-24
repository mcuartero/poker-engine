from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
    
    def build(self):
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        values = list(range(2, 15))

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None
    
    def __len__(self):
        return len(self.cards)