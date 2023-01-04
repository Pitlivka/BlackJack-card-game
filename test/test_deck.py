import unittest
from src.blackjack import Blackjack


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.blackjack = Blackjack()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.blackjack.cards)
        self.assertEqual(number_of_cards, 56)




if __name__ == '__main__':
    unittest.main()
