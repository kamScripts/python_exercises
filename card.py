import random
class Card:
    """Represents single playing cards"""
    suite_names=('Clubs', 'Diamonds', 'Hearts', 'Spades')
    #First el. of list is None as there is no card with rank '0'.
    rank_names=(None, 'As', '2', '3', '4', '5', '6','7',
                 '8','9','10', 'Walet', 'Krolowa', 'Krol')
    def __init__(self, suite=0, rank=2):
        self.suite = suite
        self.rank = rank
    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suite_names[self.suite]}'
    #override less than behavior
    def __lt__(self,other):
        t1=self.suite, self.rank
        t2=other.suite, other.rank
        return t1<t2
class Deck:
    """Represents a deck playing cards"""
    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14):
                card=Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    #this type of method is called veneer as it is used to call other function
    def pop_card(self):
        return self.cards.pop()
    def add_card(self,card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def sort_deck(self):
        self.cards.sort()
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
class Hand(Deck):
    """Represents a hand of playing cards"""
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    
deck=Deck()
deck.shuffle()
print(deck)
print('*'*20)
deck.sort_deck()
print(deck)