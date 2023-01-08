import random
from tkinter import *

font_style_labels = ("Helvetica", 15, "bold")
font_style_header = ("Helvetica", 40, "bold")
red = "#b30000"
black = "#000000"
blue = "#6699ff"
green = "#009933"
white = "#ffffff"
gray = "#d2d3cb"
light_yellow = "#eff2c6"
light_blue = "#d2d3cb"




class Blackjack_Layout:




    def __init__(self):
        """Init method wit window constructor TK variables (buttons,labels,background) ,
        and other variables needed to run game"""

        self.window = Tk()
        self.window.title("Blackjack")
        self.window.geometry("1440x900")
        self.window.resizable(False, False)

        self.filename = PhotoImage(file="BlackJackBackground.png", master=self.window)
        self.background_label = Label(self.window, image=self.filename)
        self.background_label.place(x=0, y=0)
        self.first_go = False
        self.tests = False
        self.card_name = " "
        self.dealers_hand = []
        self.players_hand = []
        self.initial_dealers_score = 0
        self.dealers_score = 0
        self.player_score = 0
        self.card = []
        self.ace_test_value = 0

        self.deck_cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8,
                           8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'King', 'King', 'King', 'King', 'Queen', 'Queen', 'Queen',
                           'Queen', 'Jack', 'Jack', 'Jack', 'Jack', 11, 11, 11, 11]

        """Button which when pressed calles an script which will hide start game buttonn and initiate labels 
        and new buttons ( hit and stand) """

        self.start_game = Button(self.window, text='Start the game', font=font_style_header, bg=gray, fg=black,
                                 command=lambda: self.call_report("generate_cards"))
        self.start_game.place(x=550, y=625, width=400, height=100)

        self.player_live_score = Label(self.window, font=font_style_labels, borderwidth=3, relief="solid")
        self.player_live_score.config(text='Players score ', bg=light_yellow, fg="black")
        self.player_live_score.place(x=900, y=450, width=250, height=100)

        self.player_live_deck = Label(self.window, font=font_style_labels, borderwidth=3, relief="solid")
        self.player_live_deck.config(text='Players deck ', bg=light_yellow, fg="black")
        self.player_live_deck.place(x=300, y=450, width=500, height=100)

        self.dealers_live_score = Label(self.window, font=font_style_labels, borderwidth=3, relief="solid")
        self.dealers_live_score.config(text='Dealers score ', bg=light_yellow, fg="black")
        self.dealers_live_score.place(x=900, y=250, width=250, height=100)

        self.dealers_live_deck = Label(self.window, font=font_style_labels, borderwidth=3, relief="solid")
        self.dealers_live_deck.config(text='Dealers deck ', bg=light_yellow, fg="black")
        self.dealers_live_deck.place(x=300, y=250, width=500, height=100)
        self.inf_label = Label(self.window, font=font_style_labels, borderwidth=3, relief="solid")

    def run(self):
        self.window.mainloop()

    def call_report(self, param):
        pass


class Blackjack(Blackjack_Layout):
    def restart(self):

        if not self.tests:
            self.draw.place_forget()
            self.stand_bttn.place_forget()
            self.restart_game = Button(self.window, text='NEW GAME', font=font_style_header, bg=gray, fg=black,
                                       command=lambda: self.call_report("restart"))
            self.restart_game.place(x=600, y=625, width=300, height=100)

        if self.tests:
            pass

    def run_script(self, go):
        """Method which is called depending on the state and situation of the game.
        If called with argument "restart": the game will reset all its variables and call function to draw new set of
        two cards per player.

        If called with argument "generate_cards" the method will enable new HIT and STAND buttons in GUI and initiate
        new cards for player and the dealer.

        If called with argument "player_go" it will draw a card for player and update players score and the main deck
        while also eventually call method to check state of game based on the rules.

        If called with argument "dealer_go" , the cards for the Dealer will keep being draw automatically until the
        dealers card score is 17 or larger. If the score is larger than 17 then the dealer game rules method will be
        called which checks the scores and determines who has or has not won the game or if it is a tie.

        The last argument "initiate" is automaticaly called right after first two cards has been drawn and checks if
        there already is an Blackjack for the player or an TIE if the player and dealer both have score 21.

        """

        if go == "restart":
            self.restart_game.place_forget()
            self.deck_cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8,
                               8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'King', 'King', 'King', 'King', 'Queen', 'Queen',
                               'Queen',
                               'Queen', 'Jack', 'Jack', 'Jack', 'Jack', 11, 11, 11, 11]

            self.card_name = " "
            self.dealers_hand = []
            self.players_hand = []
            self.initial_dealers_score = 0
            self.dealers_score = 0
            self.player_score = 0
            self.call_report("generate_cards")

        if go == "generate_cards":
            self.inf_label = Label(self.window, font=font_style_labels, borderwidth=3, relief="solid")
            self.inf_label.place(x=280, y=50, width=900, height=150)

            self.draw = Button(self.window, text='HIT', relief="solid", font=font_style_header, bg=gray, fg=black,
                               command=lambda: self.call_report("players_go"))
            self.draw.place(x=350, y=650, width=350, height=100)

            self.stand_bttn = Button(self.window, text='STAND', relief="solid", font=font_style_header, bg=gray,
                                     fg=black, command=lambda: self.call_report("dealer_go"))
            self.stand_bttn.place(x=800, y=650, width=350, height=100)

            self.generate_two_initial_cards()

        if go == "players_go":
            self.card_generating("Player")
            self.update_labels("player")
            self.ace_reduction()

        if go == "dealer_go":
            while self.dealers_score < 17:
                self.card_generating("Dealer")

            else:
                self.dealers_hand_rules()

        if go == "initiate":
            self.initial_hand_rules_check()

    def call_report(self, go):
        """method which listens to calls if the button hit or start game is pressed"""
        self.run_script(go)

    def card_generating(self, player):
        """Method which generates random cards from the deck and then based on the cards value and player who plays it,
        it invokes method "cards_score_manager" which deals with game rules.

        Current method generates random card from the deck_cards and then automatically removes it from the
        deck_cards so it can not be drawn again.

        Method also prints in output what card was generated and what are the remaining cards in deck.

        If the randomly generated card is either 1 or 11, another method is called to deal with the ACE value based on
        the dealers or the players current deck_score.
         """

        self.card = []
        self.card = self.select_random_card()

        print("Drawn card: ", self.card)

        if self.card == 1:
            self.ace_value_logic(player)

        if self.card == 11:
            self.ace_value_logic(player)

        if self.card == 'King':
            self.deck_cards.remove(self.card)
            self.card_name = "KING"
            self.cards_score_manager(player, self.card_name, 10)
            print("The card is KING for", player, "\n  Remaining cards in deck:", self.deck_cards)

        if self.card == 'Queen':
            self.deck_cards.remove(self.card)
            self.card_name = "QUEEN"
            self.cards_score_manager(player, self.card_name, 10)
            print("The card is QUEEN for " + player + "\n  Remaining cards in deck:", self.deck_cards)

        if self.card == 'Jack':
            self.deck_cards.remove(self.card)
            self.card_name = "JACK"
            self.cards_score_manager(player, self.card_name, 10)
            print("The card is JACK for" + player + "\n  Remaining cards in deck:", self.deck_cards)

        if self.card in range(2, 11, 1):
            self.deck_cards.remove(self.card)
            self.card_name = self.card
            self.cards_score_manager(player, self.card_name, self.card)
            print("The card is ", self.card_name, " for " + player + "\n Remaining cards in deck:", self.deck_cards)

    def ace_value_logic(self, player):
        """This method decides what will the value of ACE card be based on the current deck_cards value of either
        the player or the dealer

        If it is smaller or equal to 10 then the ACE value will be 11 and if it is 11 or higher then the value will be
        1.

        """
        self.ace_test_value = 0
        if player == "Dealer":
            if self.dealers_score <= 10:
                self.ace_value_selector(player, 11)
                self.ace_test_value = 11
            else:
                self.ace_value_selector(player, 1)
                self.ace_test_value = 1
        if player == "Player":
            if self.player_score <= 10:
                self.ace_value_selector(player, 11)
                self.ace_test_value = 11
            else:
                self.ace_value_selector(player, 1)
                self.ace_test_value = 1

    def ace_reduction(self):
        """Method which checks if the value of players card need Ace card updated.
        If the score is between 21 and 32 and the player has Ace card valued 11 in their deck
        it will change the Ace value to 1 to benefit the player.

        """
        if "Ace 11" in self.players_hand and 21 < self.player_score < 32:
            print(self.player_score)
            self.players_hand.remove("Ace 11")
            self.players_hand.append("Ace 1")
            self.player_score = self.player_score - 11
            self.update_labels("Dealer")
            self.player_hand_rules(self.player_score)
            print("new player score is ", self.player_score)
            print("nes players deck is :", self.players_hand)

        else:
            self.player_hand_rules(self.player_score)

    def ace_value_selector(self, player, value):
        """This method is called by the "ace_value_logic" method and it calles "cards_score_manager" method with correct
        ace value which will then update the values of the game variables

        It also removes 1 and 11 every time ACE card is drawn.
        """

        if value == 11:
            self.cards_score_manager(player, "Ace 11", 11)

            self.deck_cards.remove(1)
            self.deck_cards.remove(11)
            print('ACE:', self.deck_cards)
        if value == 1:
            self.cards_score_manager(player, "Ace 1", 1)

            self.deck_cards.remove(1)
            self.deck_cards.remove(11)
            print('ACE:', self.deck_cards)

    def cards_score_manager(self, player, card, card_value):
        """This method is most important as it is called every time card is drawn.

        The return depends on player , card drawn and its value.

        Every time thi method is called , the score of player or dealer is updated, depending on if it is called after
        the first two cards have been generated, or it is after that.

        Also the scores are updated based on if it is dealer or the player playing.

        """

        if player == "Player" and self.first_game == True:
            self.player_score = self.player_score + card_value
            self.players_hand.append(card)
            print("players deck: " + str(self.players_hand))
            self.update_labels("player")
            self.call_report("initiate")

        if player == "Player" and self.first_game == False:
            self.player_score = self.player_score + card_value
            self.players_hand.append(card)
            print("players deck: " + str(self.players_hand))

        if player == "Dealer" and self.first_game == True:
            self.dealers_score = self.dealers_score + card_value
            self.dealers_hand.append(card)
            print("Dealers deck: " + str(self.dealers_hand))
            self.update_labels("player")
            self.call_report("initiate")

        if player == "Dealer" and self.first_game == False:
            self.dealers_score = self.dealers_score + card_value
            self.dealers_hand.append(card)
            print("Dealers deck: " + str(self.dealers_hand))

    def player_hand_rules(self, score):
        """Method which is  called everytime the player presses the HIT and it checks if the Players score
        is smaller, equal or larger than 21

        If it is equal to 21 it informs player that they have won and if it is larger then it informs player that they
        have lost.
        """

        if score < 21:
            self.update_labels("player")
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("Score below 21 ")
            self.inf_label.config(text='Players turn', font=font_style_header, bg=gray, fg=red)

        if score == 21:
            self.update_labels("dealer")
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("Game state", "Player has WON")
            self.inf_label.config(text='Player has WON ', bg=green, fg=black)
            self.player_live_score.config(bg=green, fg=black)
            self.player_live_deck.config(bg=green, fg=black)
            self.player_live_score.config(bg=green, fg=black)
            self.player_live_deck.config(bg=green, fg=black)
            self.restart()

        if score > 21:
            self.update_labels("dealer")
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("Game state", "Player has lost the game")
            self.inf_label.config(text='Player is bust!! Dealer has WON!! ', bg=red, fg=white)
            self.player_live_score.config(bg=red, fg=black)
            self.player_live_deck.config(bg=red, fg=black)
            self.dealers_live_deck.config(bg=green, fg=black)
            self.dealers_live_score.config(bg=green, fg=black)
            self.restart()

    def dealers_hand_rules(self):

        """Method which is called if it is dealers turn after player has hit HIT button and it decides based on the
        dealers cards current score if to keep drawing ( depending on if the score is below 17 or not ) and it also
        checks if the dealer has BlackJack , or if it is a TIE , lost or won. """

        if self.dealers_score == 21 and self.player_score != 21 and len(self.dealers_hand) == 2:
            self.update_labels("dealer")
            self.inf_label.config(text='BLACKJACK!! Dealer has WON ', bg=green, fg=white)
            self.dealers_live_deck.config(bg=green, fg=black)
            self.dealers_live_score.config(bg=green, fg=black)
            self.player_live_score.config(bg=red, fg=black)
            self.player_live_deck.config(bg=red, fg=black)
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("BLACKJACK!! Dealer has WON")
            self.restart()

        if self.dealers_score == 21 and len(self.dealers_hand) > 2:
            self.update_labels("dealer")
            self.inf_label.config(text='BLACKJACK!! Dealer has WON ', bg=green, fg=white)
            self.dealers_live_deck.config(bg=green, fg=black)
            self.dealers_live_score.config(bg=green, fg=black)
            self.player_live_score.config(bg=red, fg=black)
            self.player_live_deck.config(bg=red, fg=black)
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("BLACKJACK!! Dealer has WON")
            self.restart()

        if 17 <= self.dealers_score < 21 and self.dealers_score > self.player_score:
            self.update_labels("dealer")
            self.inf_label.config(text='Dealer has Won! You lost', bg=red, fg=black)
            self.dealers_live_deck.config(bg=green, fg=black)
            self.dealers_live_score.config(bg=green, fg=black)
            self.player_live_score.config(bg=red, fg=black)
            self.player_live_deck.config(bg=red, fg=black)
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("Dealer has Won")
            self.restart()

        if self.dealers_score == self.player_score and self.dealers_score >= 17:
            self.update_labels("dealer")
            self.inf_label.config(text='Its a tie (push) ', bg=blue, fg=black)
            self.dealers_live_score.config(bg=blue, fg=white)
            self.player_live_score.config(bg=blue, fg=white)
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("Its a tie")
            self.restart()

        if 17 <= self.dealers_score < self.player_score:
            self.update_labels("dealer")
            self.inf_label.config(text='Dealer is bust! YOU WON', bg=green, fg=black)
            self.dealers_live_deck.config(bg=red, fg=black)
            self.dealers_live_score.config(bg=red, fg=black)
            self.player_live_score.config(bg=green, fg=black)
            self.player_live_deck.config(bg=green, fg=black)
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("Dealer has lost")
            self.restart()

        if self.dealers_score > 21:
            self.update_labels("dealer")
            self.inf_label.config(text='Dealer is bust! YOU WON', bg=green, fg=black)
            self.dealers_live_deck.config(bg=red, fg=black)
            self.dealers_live_score.config(bg=red, fg=black)
            self.player_live_score.config(bg=green, fg=black)
            self.player_live_deck.config(bg=green, fg=black)
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("Dealer has lost")
            self.restart()

    def initial_hand_rules_check(self):

        """ Methods which checks and compares the scores after the
        first two cards has been generated before players go"""

        if self.player_score == 21 and self.dealers_score != 21:
            self.update_labels("dealer")
            self.inf_label.config(text='BLACKJACK!! Player has WON', bg=green, fg=black)
            self.dealers_live_deck.config(bg=red, fg=black)
            self.dealers_live_score.config(bg=red, fg=black)
            self.player_live_score.config(bg=green, fg=black)
            self.player_live_deck.config(bg=green, fg=black)
            print("Blackjack Player has won")
            self.restart()

        if self.player_score > 21:
            self.update_labels("dealer")
            self.inf_label.config(text='Player is bust!! Dealer has won!', bg=red, fg=white)
            self.dealers_live_deck.config(bg=green, fg=black)
            self.dealers_live_score.config(bg=green, fg=black)
            self.player_live_score.config(bg=red, fg=black)
            self.player_live_deck.config(bg=red, fg=black)
            print("Player is bust!! Dealer has won!")
            self.restart()

        if self.player_score == 21 and self.dealers_score == 21:
            self.update_labels("dealer")
            self.inf_label.config(text='Its a tie (push) ', bg=blue, fg=black)
            self.dealers_live_score.config(bg=blue, fg=white)
            self.player_live_score.config(bg=blue, fg=white)
            print("Its a tie (push)")
            self.restart()

        if self.player_score < 21:
            self.inf_label.config(text="Players turn", font=font_style_header, bg=gray, fg=red)
            print("Score below 21 ")

    def dealers_turn(self):
        """Method run by the "dealers_hand_rules" method on loop until the dealers card deck score is 17 or larger"""
        self.card_generating("Dealer")

    def update_labels(self, turn):
        """Method which updates the labels on the window screen of the program.

        If it is called with argument "player" then it means that player is still playing an therefore the dealers
        cards or score can not be revealed yet.

        If it is called with argument "dealer" then it means that the player has either pressed STAND, has lost or won
        and
        the dealers score and dealers deck cards are then automatically revealed.

        """

        if turn == "player":
            self.player_live_score.config(text='Players score : ' + str(self.player_score), bg=light_yellow, fg=black)
            self.player_live_deck.config(text='Players deck : ' + str(self.players_hand), bg=light_yellow, fg=black)

            self.dealers_live_score.config(text='Dealers score : ' + str(self.initial_dealers_score), bg=light_yellow,
                                           fg=black)
            self.dealers_live_deck.config(text='Dealers deck : ' + (str(self.dealers_hand[0])) + ' , Hidden Card',
                                          bg=light_yellow, fg=black)
        if turn == "dealer":
            self.player_live_score.config(text='Players score : ' + str(self.player_score), bg=light_yellow, fg=black)
            self.player_live_deck.config(text='Players deck : ' + str(self.players_hand), bg=light_yellow, fg=black)

            self.dealers_live_score.config(text='Dealers score : ' + str(self.dealers_score), bg=light_yellow, fg=black)
            self.dealers_live_deck.config(text='Dealers deck : ' + str(self.dealers_hand), bg=light_yellow, fg=black)

    def generate_two_initial_cards(self):
        """Method which is called when the game starts , and it generates first two cards for the
        dealer and the player"""

        self.start_game.place_forget()
        self.first_game = True

        self.card_generating("Dealer")
        self.initial_dealers_score = self.dealers_score
        self.card_generating("Dealer")

        self.card_generating("Player")
        self.card_generating("Player")

        self.first_game = False

        print("Players initial two cards :", self.players_hand)
        print("Dealers initial two cards :", self.dealers_hand)
        print("Players initial score :", self.player_score)
        print("Dealers initial score :", self.dealers_score)

    def select_random_card(self):
        """ Method which randomly generates card from the deck cards and also checks if the deck is empty"""
        if len(self.deck_cards) == 0:
            print('the list is empty')

        else:
            print(len(self.deck_cards))
            return random.choice(self.deck_cards)


if __name__ == "__main__":
    BlackJack = Blackjack()
    BlackJack.run()
