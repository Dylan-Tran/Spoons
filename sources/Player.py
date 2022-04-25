# -*- coding: utf-8 -*-

from sources.Strategy import decision_dictionary, strat
from functools import reduce

class Player(object):
    
    def __init__(self, strategy):
        self.hand = []
        self.history = []
        self.strat = decision_dictionary[strategy]
        self.freq = []
        self.unique = []
        
    def __repr__(self):
        return f"Hand: {str(self.hand)}" #\nPlayer History: {str(self.history)}"
        
    def add_card(self, next_card) -> None:
        if next_card not in self.unique:
            self.unique += [next_card]

        if len(self.hand) < 4:            
            self.hand.append(next_card)
        else:
            print("error")
    
    def move(self, next_card) -> int:
        (self.hand, self.history, self.freq, discard_card) = strat(self.hand, self.history, self.freq, next_card, self.strat)
        return discard_card
    
    def win(self) -> bool:
        return self.hand.count(self.hand[0]) == 4

    def getFreq(self):
        return self.freq

    def getUnique(self):
        return self.unique