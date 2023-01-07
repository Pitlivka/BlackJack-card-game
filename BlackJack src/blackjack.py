
import random
import sys
from tkinter import *



import tkinter.messagebox

import os


FONT_STYLE = ("Montserrat", 18, "bold")

class Blackjack_Layout():



    def __init__(self):
        """Init method wit window constructor TK variables (buttons,labels,background)  , and other variables needed to run game"""


        self.window = Tk()
        self.window.title("Blackjack")
        self.window.geometry("1440x900")
        self.window.resizable(False, False)

        self.filename = PhotoImage(file="BlackJackBackground.png", master = self.window)
        self.background_label = Label(self.window, image=self.filename)
        self.background_label.place(x=0, y=0)


        self.tests = False
        self.card_name = " "
        self.dealers_hand = []
        self.players_hand = []
        self.initial_dealers_score = 0
        self.dealers_score = 0
        self.player_score = 0

        self.cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8,
                           8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'King', 'King', 'King', 'King', 'Queen', 'Queen', 'Queen',
                           'Queen', 'Jack', 'Jack', 'Jack', 'Jack', 11, 11, 11, 11]

        self.deck_cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8,
                           8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'King', 'King', 'King', 'King', 'Queen', 'Queen', 'Queen',
                           'Queen', 'Jack', 'Jack', 'Jack', 'Jack', 11, 11, 11, 11]


        """Button which when pressed calles an script which will hide start game buttonn and initiate labels 
        and new buttons ( hit and stand) """

        self.start_game = Button(self.window, text='Start game', command=lambda: self.call_report("generate_cards"))
        self.start_game.place(x=700, y=700, width=100, height=100)

        self.player_live_score = Label(self.window, font=FONT_STYLE, borderwidth=3, relief="solid")
        self.player_live_score.config(text='Players score ', bg="#D8DADA", fg="black")
        self.player_live_score.place(x=900, y=450, width=250, height=100)

        self.player_live_deck = Label(self.window, font=FONT_STYLE, borderwidth=3, relief="solid")
        self.player_live_deck.config(text='Players deck ', bg="#D8DADA", fg="black")
        self.player_live_deck.place(x=300, y=450, width=500, height=100)

        self.dealers_live_score = Label(self.window, font=FONT_STYLE, borderwidth=3, relief="solid")
        self.dealers_live_score.config(text='Dealers score ', bg="#D8DADA", fg="black")
        self.dealers_live_score.place(x=900, y=250, width=250, height=100)

        self.dealers_live_deck = Label(self.window, font=FONT_STYLE, borderwidth=3, relief="solid")
        self.dealers_live_deck.config(text='Dealers deck ', bg="#D8DADA", fg="black")
        self.dealers_live_deck.place(x=300, y=250, width=500, height=100)

        self.inf_label = Label(self.window, font=FONT_STYLE, borderwidth=3, relief="solid")
        self.inf_label.config(text='Blackjack ', bg="#D8DADA", fg="black")
        self.inf_label.place(x=500, y=100, width=500, height=100)

    def run(self):
        self.window.mainloop()
class Blackjack(Blackjack_Layout):

    def restart(self):
        self.draw.place_forget()
        self.stand_bttn.place_forget()
        self.restart_game = Button(self.window, text='NEW GAME', command=lambda: self.call_report("restart"))
        self.restart_game.place(x=700, y=700, width=100, height=100)


    def run_script(self, go):
        """Method which if called with "generate_cards" argument, will invoke method "generate_players_cards" which draws
        two cards for player and dealer when the game starts

        if the argument is "players_go" the method will run method "card_generatin" every time the player presses the
        HIT button"""

        if go == "restart":
            self.inf_label.config(text='New Game', bg="black", fg="white")

            self.restart_game.place_forget()

            self.tests = False
            self.card_name = " "
            self.dealers_hand = []
            self.players_hand = []
            self.initial_dealers_score = 0
            self.dealers_score = 0
            self.player_score = 0
            self.deck_cards = self.cards

            self.call_report("generate_cards")



        if go == "generate_cards":

            self.generate_player_cards()



            self.draw = Button(self.window, text='HIT', relief="solid", command=lambda: self.call_report("players_go"))
            self.draw.place(x=350, y=600, width=350, height=100)

            self.stand_bttn = Button(self.window, text='STAND', relief="solid", command=lambda: self.dealers_hand_rules())
            self.stand_bttn.place(x=800, y=600, width=350, height=100)

        if go == "players_go":
            self.card_generating("Player")
            self.update_labels("player")

    def call_report(self, go):
        """method which listens to calls if the button hit or start game is pressed"""
        self.run_script(go)

    def card_generating(self, player):
        """Method which generates random cards from the deck and then based on the cards value and player who plays it,
        it invokes method "cards_score_manager" which deals with game rules.

        Current method generates random card from the deck_cards and then automatically removes it from the deck_cards so
        it can not be drawn again.

        Method also prints in output what card was generated and what are the remaining cards in deck.

        If the randomly generated card is either 1 or 11, another method is called to deal with the ACE value based on the Dealers
        or Players current deck_score.
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

    def ace_value_selector(self, player, value):
        """This method is called by the "ace_value_logic" method and it calles "cards_score_manager" method with correct
        ace value which will then update the values of the game variables

        It also removes 1 and 11 every time ACE card is drawn.

        """

        if value == 11:
                self.cards_score_manager(player, 11, 11)
                print('ACE:', self.deck_cards)
                self.deck_cards.remove(1)
                self.deck_cards.remove(11)
        if value == 1:
                self.cards_score_manager(player, 1, 1)
                print('ACE:', self.deck_cards)
                self.deck_cards.remove(1)
                self.deck_cards.remove(11)

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
            self.initial_check()


        if player == "Player" and self.first_game == False:
            self.player_score = self.player_score + card_value
            self.players_hand.append(card)
            print("players deck: " + str(self.players_hand))
            self.player_game_rules(self.player_score)


        if player == "Dealer" and self.first_game == True:
            self.dealers_score = self.dealers_score + card_value
            self.dealers_hand.append(card)
            print("Dealers deck: " + str(self.dealers_hand))
            self.update_labels("player")
            self.initial_check()



        if player == "Dealer" and self.first_game == False:
            self.dealers_score = self.dealers_score + card_value
            self.dealers_hand.append(card)
            print("Dealers deck: " + str(self.dealers_hand))
            self.dealers_hand_rules()

    def player_game_rules(self, score):
        """Method which is  called everytime the player presses the HIT and it checks if the Players score
        is smaller, equal or larger than 21

        If it is equal to 21 it informs player that they have won and if it is larger then it informs palyer that they
        have lost.
        """

        if score < 21:
            self.update_labels("dealer")
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("Score below 21 ")
            self.inf_label.config(text='Score below 21 ', bg="white", fg="black")


        if score == 21:
            self.update_labels("dealer")
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("Game state", "Player has WON")
            self.inf_label.config(text='player has WON ', bg="#00b300", fg="black")
            self.player_live_score.config( bg="#00b300", fg="black")
            self.player_live_deck.config(bg="#00b300", fg="black")
            self.restart()


        if score > 21:
            self.update_labels("dealer")
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            print("Game state", "Player has lost the game")
            self.inf_label.config(text='Player has lost the game ', bg="#800000", fg="white")
            self.restart()


    def dealers_hand_rules(self):

        """Method which is called if it is dealers turn after player has hit HIT button and it decides based on
        the dealers cards current score if to keep drawing ( depending on if the score is below 17 or not ) and it also checks
        if the dealer has BlackJack , or if it is a TIE , lost or won."""

        while self.dealers_score < 17:
            self.dealers_turn()
        else:
            if self.dealers_score == 21 and self.player_score != 21 and len(self.dealers_hand) == 2:
                self.update_labels("dealer")
                self.inf_label.config(text='BLACKJACK!! Dealer has WON ', bg="#001a00", fg="white")
                self.dealers_live_deck.config(bg="#001a00", fg="white")
                self.dealers_live_score.config(bg="#001a00", fg="white")
                print("Players score:", self.player_score)
                print("Dealers score:", self.dealers_score)
                print("Dealer has WON")
                self.restart()


            if self.dealers_score == self.player_score and self.dealers_score >= 17 :
                self.update_labels("dealer")

                self.inf_label.config(text='Its a tie (push) ', bg="#00b3b3", fg="black")
                self.dealers_live_deck.config(bg="#800080", fg="white")
                self.dealers_live_score.config(bg="#800080", fg="white")

                print("Players score:", self.player_score)
                print("Dealers score:", self.dealers_score)
                print("Its a tie")
                self.restart()


            if self.dealers_score >= 17 and self.dealers_score < self.player_score :
                self.update_labels("dealer")

                self.inf_label.config(text='Dealer has lost.', bg="#800000", fg="black")
                self.dealers_live_deck.config(bg="#800000", fg="white")
                self.dealers_live_score.config(bg="#800000", fg="white")
                print("Players score:", self.player_score)
                print("Dealers score:", self.dealers_score)
                print("Dealer has lost")
                self.restart()


            if self.dealers_score >= 17 and self.dealers_score > self.player_score and self.dealers_score < 22:
                self.update_labels("dealer")

                self.inf_label.config(text='Dealer has Won', bg="#D8DADA", fg="black")
                print("Players score:", self.player_score)
                print("Dealers score:", self.dealers_score)
                print("Dealer has Won")
                self.restart()


            if self.dealers_score > 21:
                self.update_labels("dealer")

                self.inf_label.config(text='Dealer has lost', bg="red", fg="black")
                print("Players score:", self.player_score)
                print("Dealers score:", self.dealers_score)
                print("Dealer has lost")
                self.restart()


    def initial_check(self):
        """ Methods which checks and compares the scores after the first two cards has been generated before players go"""

        if self.player_score == 21 and self.dealers_score != 21:
            self.update_labels("dealer")
            self.inf_label.config(text='BLACKJACK!! Player has WON', bg="#001a00", fg="white")
            self.player_live_score.config(bg="#001a00", fg="white")
            self.players_live_deck.config(bg="#001a00", fg="white")
            print("Blackjack Player has won")
            self.restart()


        if self.player_score > 21:
            self.update_labels("dealer")
            self.inf_label.config(text='Player has LOST', bg="#800000", fg="white")
            print("Player has lost")
            self.restart()

        if self.player_score == 21 and self.dealers_score == 21:
            self.update_labels("dealer")
            self.inf_label.config(text='Its a tie (push)', bg="#800080", fg="black")
            print("Its a tie")
            self.restart()

        if self.player_score < 21:
            self.inf_label.config(text='Score below 21 ', bg="#D8DADA", fg="red")



    def dealers_turn(self):
        """Method run by the "dealers_hand_rules" method on loop until the dealers card deck score is 17 or larger"""

        self.card_generating("Dealer")

    def update_labels(self,turn):
        """Method which updates the labels on the window screen of the program.

        If it is called with argument "player" then it means that player is still playing an therefore the dealers
        cards or score can not be revealed yet.

        If it is called with argument "dealer" then it means that the player has either pressed STAND, has lost or won and
        the dealers score and dealers deck cards are then automatically revealed.

        """


        if turn == "player":
            self.player_live_score.config(text='Players score : ' + str(self.player_score), bg="#D8DADA", fg="red")
            self.player_live_deck.config(text='Players deck : ' + str(self.players_hand), bg="#D8DADA", fg="red")

            self.dealers_live_score.config(text='Dealers score : ' + str(self.initial_dealers_score), bg="#D8DADA",
                                           fg="black")
            self.dealers_live_deck.config(text='Dealers deck : ' + (str(self.dealers_hand[0])) + ' , Hidden Card',
                                          bg="#D8DADA",
                                          fg="black")
        if turn == "dealer":
            self.player_live_score.config(text='Players score : ' + str(self.player_score), bg="#D8DADA", fg="red")
            self.player_live_deck.config(text='Players deck : ' + str(self.players_hand), bg="#D8DADA", fg="red")

            self.dealers_live_score.config(text='Dealers score : ' + str(self.dealers_score), bg="#D8DADA", fg="black")
            self.dealers_live_deck.config(text='Dealers deck : ' + str(self.dealers_hand), bg="#D8DADA", fg="black")



    def generate_player_cards(self):
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
            self.card = []
        else:
            print(len(self.deck_cards))
            return random.choice(self.deck_cards)










if __name__ == "__main__":
    BlackJack = Blackjack()
    BlackJack.run()
