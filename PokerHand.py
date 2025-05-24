"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card1 import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""
    labels=['straight_flush', 'four_of_kind', 'full_house', 'flush',
            'three_of_kind', '2_pairs','pair' ]
    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            
    def rank_hist(self):
        self.ranks={}
        for card in self.cards:
            self.ranks[card.rank]=self.ranks.get(card.rank,0)+1
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()

        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    def same_rank(self, num):
        """Returns true if hand has same number of card as arg"""
        self.rank_hist()
        if num in self.ranks.values():
            return True
        return False

    def has_pair(self):
        return self.same_rank(2)
    def has_three_of_kind(self):
        return self.same_rank(3)
    def has_four_of_kind(self):
        return self.same_rank(4)
    def has_full_house(self):
        return self.same_rank(2) and self.same_rank(3)
    def has_2_pairs(self):
        self.rank_hist()
        prev=0
        for val in sorted(self.ranks.values()):
            if val == 2 and prev == 2:
                return True
            prev=val
        return False
    def has_straight(self):
        self.rank_hist()
        if len(self.ranks.keys()) < 5:
            return False

        s = sorted(self.ranks.keys())

        # Check for Ace-high straight first
        if 1 in s and set([10, 11, 12, 13]).issubset(set(s)):
            return True

        # Check for regular straights
        consecutive = 1
        for i in range(1, len(s)):
            if s[i] - s[i-1] == 1:
                consecutive += 1
                if consecutive >= 5:
                    return True
            else:
                consecutive = 1

        return False
    def has_straight_flush(self):
        d={}
        for c in self.cards:
            d.setdefault(c.suit, PokerHand()).add_card(c)
        for hand in d.values():
            if len(hand.cards) < 5:
                continue
            hand.rank_hist()
            if hand.has_straight():
                return True
        return False
    def classify(self):
        self.labels=[]
        for label in PokerHand.labels:
            f=getattr(self, 'has_'+ label)
            if f():
                self.labels.append(label)
            
if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()
    
    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        hand.classify()
        print(hand.labels)

