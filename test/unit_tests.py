import unittest

from src.blackjack import Blackjack


class DeckTestCase(unittest.TestCase):
    """ DUE TO MY METHOD NOT HAVING ANY RETURN VALUE, I HAVE SELECTED PRINT STATEMENTS IN EACH METHOD IN
    BLACKJACK CLASS TO TEST IF THE UNIT TEST OUTPUTS ARE CORRECT"""

    def setUp(self):  # this method will be run before each test
        self.bl_test = Blackjack()
        self.bl_test.players_hand = []
        self.bl_test.dealers_hand = []

        self.bl_test.tests = True

    def tearDown(self):  # this method will be run after each tests
        self.bl_test.players_hand = []
        self.bl_test.dealers_hand = []
        self.bl_test.player_score = 0
        self.bl_test.dealers_score = 0

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        """The test will test if the deck cards have correct amount of cards in variable """

        self.number_of_cards = len(self.bl_test.deck_cards)
        self.assertEqual(self.number_of_cards, 56)

    def test_card_generating(self):
        """The test will check if the method "card_generating" generated random card from the deck,
         assigned it to either dealer or player and removed it from the deck """

        self.bl_test.card_generating("player")

    def test_cards_score_manager(self):
        """The test will check if the method "card_score_manager"  correctly determined if the Dealer or Player have won
        based on the card value and current value of the players or dealers hand

        The code below is to check if the method informs the player with card value of 21 that hey have won the game.

        THE  METHOD also checks if the variables were assigned correcly.
        """

        self.bl_test.first_game = False

        self.bl_test.cards_score_manager("Dealer", "10", 20)

        self.assertEqual(self.bl_test.dealers_score, 20)

    def test_ace_value_generator(self):
        """The test will check that if the card drawn is either 11 or 1, the method will assign either 1 or 11 which is
        determined based on the players or dealers current combined card score

        If is 10 or below the Ace will be assigned value of 11 but if it is 11 or more it will be assigned value of 11

        """
        self.bl_test.player_score = 10
        self.bl_test.first_game = False
        self.bl_test.dealers_score = 9
        self.bl_test.ace_value_logic("Player")
        self.assertEqual(self.bl_test.ace_test_value, 11)
        print("ace card: ", self.bl_test.player_score)

    def test_dealers_hand_rules(self):
        """The test will check if the game rules work correctly after the firs two hands have been handed to the player
        and the dealer
        It will check if it is a blackjack or a tie.
        """

        self.bl_test.dealers_hand = ["jack", "10"]
        self.bl_test.players_hand = ["king", "11"]

        self.bl_test.player_score = 20
        self.bl_test.dealers_score = 21

        self.bl_test.dealers_hand_rules()

    def test_players_hand_rules(self):
        """The test will check if the game rules work when player press hit.
        To test output we need to pre set dealers score and the pass argument ( players score ) to the method
        to see if the output is correct.
             """

        self.bl_test.dealers_score = 20
        self.bl_test.player_hand_rules(21)

    def test_initial_hand_rules_check(self):
        """The test will check if the output is correct based on the score of dealer and player which was added after
        first two playing cards has been drawn """

        self.bl_test.dealers_score = 21
        self.bl_test.player_score = 20
        self.bl_test.initial_hand_rules_check()

    def test_generate_two_initial_cards(self):
        """The tests will check the method which generates first two cards for the player and the dealer and then
        assigns them to their decks.

        Once they are assigned they are also removed from the main deck

        """

        self.bl_test.generate_two_initial_cards()

        self.assertEqual(len(self.bl_test.dealers_hand), len(self.bl_test.players_hand))

        self.assertEqual(len(self.bl_test.deck_cards), 51)

    def test_ace_reduction(self):
        """ Test which tests if the ace_reduction method works correctly """
        self.bl_player_score = 30

        self.bl_test.dealers_hand = ["10", "King", "2"]
        self.bl_test.players_hand = ["Ace 11", "Ace 1", "10"]

        self.bl_test.ace_reduction()
