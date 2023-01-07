import unittest

from src.blackjack import Blackjack


class DeckTestCase(unittest.TestCase):


    """ DUE TO MY METHOD NOT HAVING ANY RETURN VALUE, I HAVE SELECTED PRINT STATEMENTS IN EACH METHOD IN
    BLACKJACK CLASS TO TEST IF THE UNIT TEST OUTPUTS ARE CORRECT"""

    def setUp(self):  # this method will be run before each test
        self.bl_test = Blackjack()


    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        """The test will test if the deck cards have correct amount of cards in variable """


        self.number_of_cards = len(self.bl_test.deck_cards)
        self.assertEqual(self.number_of_cards, 56)
        print("cards in deck")



    def test_card_generating(self):
        """The test will check if the method "card_generating" generated random card from the deck,
         assigned it to either dealer or player and removed it from the deck """



        self.bl_test.card_generating("player")
        print("card_generating")


    def test_cards_score_manager(self):
        """The test will check if the method "card_score_manager"  correctly determined if the Dealer or Player have won
        based on the card value and current value of the players or dealers hand

        The code below is to check if the method informs the player with card value of 21 that hey have won the game.

        THE  METHOD also checks if the variables were assigned correcly.
        """

        self.bl_test.first_game = False

        self.bl_test.dealers_hand = []
        self.bl_test.cards_score_manager("Dealer", "10", 20)

        self.assertEqual(self.bl_test.dealers_score, 20)
        print("cards_score_manager:")



    def test_ace_value_generator(self):
        """The test will check that if the card drawn is either 11 or 1, the method will assign either 1 or 11 which is
        determined based on the players or dealers current combined card score

        If is 10 or below the Ace will be assigned value of 11 but if it is 11 or more it will be assigned value of 11

        """


        print("ace_value_generator:")

        self.bl_test.player_score = 10
        self.bl_test.players_hand = []
        self.bl_test.dealers_hand = []
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



        self.bl_test.player_score = 21
        self.bl_test.dealers_score = 21

        self.bl_test.players_hand = []
        self.bl_test.dealers_hand = []
        self.bl_test.dealers_hand_rules()
        print("dealers_hand_rules:")


