import unittest
from unittest.mock import MagicMock
from src.blackjack import Blackjack


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.blackjack = Blackjack()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.blackjack.deck_cards)
        self.assertEqual(number_of_cards, 56)


    def test_card_generating(self):
        self.blackjack.card_generating("player")


    def test_generate_player_cards(self):
        # The actual test

        self.blackjack.first_game = True
        self.blackjack.dealers_cards = "10"
        self.blackjack.cards_score_manager("Player", "10", 21)

        self.assertEqual(self.blackjack.player_score, 21)

    def test_ace_value_generator(self):
        self.blackjack.player_score = 10
        self.blackjack.player_cards = []
        self.blackjack.dealers_cards = []
        self.blackjack.first_game = False
        self.blackjack.dealers_score = 9
        self.blackjack.ace_value_generator("Player")
        self.assertEqual(self.blackjack.ace_test_value, 11)













if __name__ == '__main__':
    unittest.main()
