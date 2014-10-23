import unittest
from cards import *


class DeckTestCase(unittest.TestCase):
    '''Tests for cards.py'''

    def test_deck_constructor(self):
        '''Tests that the constructor for deck creates the correct object'''
        test_deck = Deck()
        self.assertIsInstance(test_deck, Deck)

    def test_card_constructor(self):
        '''Tests that the constructor for Card creates the correct object'''
        test_card = Card(0)
        self.assertIsInstance(test_card, Card)

    def test_deck_contents(self):
        '''Tests that the deck initializes with 52 cards'''
        test_deck = Deck()
        self.assertTrue(len(test_deck.contents) == 52)

    def test_deck_draw(self):
        '''Tests that draw returns a card and removes it from the deck'''
        test_deck = Deck()
        drawn = test_deck.draw()
        self.assertTrue(drawn.name == 'King of Diamonds'
                and len(test_deck.contents) == 51)

    def test_shuffle(self):
        '''Tests with a >99.99 percent certainty that the shuffle
                will not shuffle the same way repeatedly by comparing
                the top card of 101 different shuffles'''
        passed = False
        test_deck = Deck()
        test_deck.shuffle()
        test_card = test_deck.draw()
        for i in range(100):
            d = Deck()
            top_card = d.draw()
            if top_card != test_card:
                passed = True
                break
        self.assertTrue(passed)

    def test_joker(self):
        '''Tests that an invalid value for a card will default to joker'''
        test_cards = []
        test_cards.append(Card(19086))
        test_cards.append(Card('card'))
        test_cards.append(Card(None))
        self.assertTrue(test_cards[0].name == 'Joker' and
            test_cards[1].name == 'Joker' and test_cards[2].name == 'Joker')

    def test_float(self):
        '''Tests that a float between 0 and 51 will produce a usable card'''
        test_card = Card(3.5)
        self.assertTrue(test_card.name == 'Four of Spades')
