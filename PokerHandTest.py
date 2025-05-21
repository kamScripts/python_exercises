import unittest
from Card1 import Card, Deck
from PokerHand import PokerHand


class Test(unittest.TestCase):
    
    def test_full_house(self):
        pk=PokerHand()
        pk.add_card(Card(0,2))
        pk.add_card(Card(1,2))
        pk.add_card(Card(1,6))
        pk.add_card(Card(3,10))
        pk.add_card(Card(2,6))
        pk.add_card(Card(2,6))
        pk.add_card(Card(0
                         ,12))
        self.assertTrue(pk.has_full_house(), 'error')
if __name__=='__main__':
    unittest.main()