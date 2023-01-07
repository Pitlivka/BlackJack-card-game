
import random
from tkinter import *

import tkinter.messagebox
from tkinter.simpledialog import SimpleDialog
import os



LARGE_FONT_STYLE = ("Times", 20, "bold")
DEFAULT_FONT_STYLE = ("Times", 25, "bold")
HEADER_FONT_STYLE = ("Montserrat", 40, "bold")
INF_FONT_STYLE = ("Montserrat", 18, "bold")

class Blackjack_Layout():


    def __init__(self):


        self.card_name = " "
        self.player_deck = []

        self.dealers_cards = []
        self.initial_dealers_score = 0
        self.dealers_score = 0

        self.count = 0
        self.player_score = 0

        self.player_cards = []

        self.cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8,
                      8, 9, 9, 9, 9, 10, 10, 10, 10, 'King', 'King', 'King', 'King', 'Queen', 'Queen', 'Queen', 'Queen',
                      'Joker', 'Jack', 'Jack', 'Jack', 11, 11, 11, 11]

        self.deck_cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8,
                           8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'King', 'King', 'King', 'King', 'Queen', 'Queen', 'Queen',
                           'Queen', 'Jack', 'Jack', 'Jack', 'Jack', 11, 11, 11, 11]


        self.window = Tk()

        self.window.geometry("1440x900")


        self.window.title("Blackjack")




        self.start_game = Button(self.window, text='Start game', command=lambda: self.call_report(False))
        self.start_game.place(x=700, y=700, width=100, height=100)










        self.player_live_score = Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
        self.player_live_score.config(text='Players score ', bg="#D8DADA", fg="red")
        self.player_live_score.place(x=900, y=450, width=250, height=100)

        self.player_live_deck = Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
        self.player_live_deck.config(text='Players deck ', bg="#D8DADA", fg="red")
        self.player_live_deck.place(x=300, y=450, width=500, height=100)

        self.dealers_live_score = Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
        self.dealers_live_score.config(text='Dealers score ', bg="#D8DADA", fg="black")
        self.dealers_live_score.place(x=900, y=250, width=250, height=100)

        self.dealers_live_deck = Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
        self.dealers_live_deck.config(text='Dealers deck ', bg="#D8DADA", fg="black")
        self.dealers_live_deck.place(x=300, y=250, width=500, height=100)





class Blackjack(Blackjack_Layout):



    def hand_rules(self):

        while self.dealers_score < 17:
            self.dealers_turn()

        if self.dealers_score == 21 and self.player_score != 21:
            self.update_labels(False)
            tkinter.messagebox.showinfo("Game state", "BLACKJACK!! Dealer has WON")

            self.game_restart()

        if self.player_score == 21 and self.dealers_score != 21:
            self.update_labels(False)
            tkinter.messagebox.showinfo("Game state", "BLACKJACK!! Player has WON")
            self.game_restart()

        if self.dealers_score == self.player_score:
            self.update_labels(False)
            tkinter.messagebox.showinfo("Game state", "Its a tie (push)")
            self.game_restart()

        if self.dealers_score >= 17 and self.dealers_score < self.player_score:
            self.update_labels(False)
            tkinter.messagebox.showinfo("Game state", "Dealer has lost.")
            self.game_restart()

        if self.dealers_score >= 17 and self.dealers_score > self.player_score:
            self.update_labels(False)
            tkinter.messagebox.showinfo("Game state", "Dealer has Won")
            self.game_restart()

        if self.dealers_score > 21:
            self.update_labels(False)
            tkinter.messagebox.showinfo("Game state", "Dealer has lost.")
            self.game_restart()

    def dealers_turn(self):

        self.card_generating("Dealer")



    def run_script(self,boolean):



        if boolean == False:
            self.generate_player_cards()



            self.draw = Button(self.window, text='HIT',relief="solid",  command=lambda: self.call_report(True))
            self.draw.place(x=350, y=600, width=350, height=100)

            self.stand_bttn = Button(self.window, text='STAND', relief="solid", command=lambda: self.hand_rules())
            self.stand_bttn.place(x=800, y=600, width=350, height=100)

        if boolean == True:
            self.card_generating("Player")
            self.update_labels(True)


    def call_report(self,boolean):
        self.run_script(boolean)

    def update_labels(self,boolean):

        if boolean == True:
            self.player_live_score.config(text='Players score : ' + str(self.player_score), bg="#D8DADA", fg="red")
            self.player_live_deck.config(text='Players deck : ' + str(self.player_cards), bg="#D8DADA", fg="red")

            self.dealers_live_score.config(text='Dealers score : ' + str(self.initial_dealers_score), bg="#D8DADA",
                                           fg="black")
            self.dealers_live_deck.config(text='Dealers deck : ' + (str(self.dealers_cards[0])) + ' , Hidden Card',
                                          bg="#D8DADA",
                                          fg="black")
        if boolean == False:
            self.player_live_score.config(text='Players score : ' + str(self.player_score), bg="#D8DADA", fg="red")
            self.player_live_deck.config(text='Players deck : ' + str(self.player_cards), bg="#D8DADA", fg="red")

            self.dealers_live_score.config(text='Dealers score : ' + str(self.dealers_score), bg="#D8DADA", fg="black")
            self.dealers_live_deck.config(text='Dealers deck : ' + str(self.dealers_cards), bg="#D8DADA", fg="black")



    def generate_player_cards(self):

        self.first_game = True

        self.card_generating("Dealer")
        self.initial_dealers_score = self.dealers_score
        self.card_generating("Dealer")

        self.card_generating("Player")
        self.card_generating("Player")

        self.first_game = False


        self.start_game.place_forget()

        print("Players initial two cards :", self.player_cards)
        print("Dealers initial two cards :", self.dealers_cards)
        print("Players initial score :", self.player_score)
        print("Dealers initial score :", self.dealers_score)




    def select_random_card(self):
        if len(self.deck_cards) == 0:
            print('the list is empty')
            self.card = []
        else:
            print(len(self.deck_cards))
            return random.choice(self.deck_cards)

    def ace_value_generator(self, player):
        self.ace_test_value = 0
        if player == "Dealer":
            if self.dealers_score <= 10:
                self.ace_value_selector(player, 0)
                self.ace_test_value = 11
            else:
                self.ace_value_selector(player, 1)
                self.ace_test_value = 1
        if player == "Player":
            if self.player_score <= 10:
                self.ace_value_selector(player, 0)
                self.ace_test_value = 11
            else:
                self.ace_value_selector(player, 1)
                self.ace_test_value = 1

    def ace_value_selector(self, player, value):
        if value == 0:
                self.cards_score_manager(player, "11", 11)
                print('ACE:', self.deck_cards)
                self.deck_cards.remove(1)
                self.deck_cards.remove(11)
        if value == 1:
                self.cards_score_manager(player, "1", 1)
                print('ACE:', self.deck_cards)
                self.deck_cards.remove(1)
                self.deck_cards.remove(11)


    def card_generating(self, player):

        self.card = []
        self.card = self.select_random_card()

        print("Drawn card: " , self.card)

        if self.card == 1:
                self.ace_value_generator(player)


        if self.card == 11:
                self.ace_value_generator(player)


        if self.card == 'King':
            self.deck_cards.remove(self.card)
            self.card_name = "KING"
            self.cards_score_manager(player, self.card_name, 10)
            print("The card is KING for" , player , "\n  Remaining cards in deck:", self.deck_cards)


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
            print("The card is " , self.card_name , " for " + player + "\n Remaining cards in deck:", self.deck_cards)









    def game_restart(self):
        answer = tkinter.messagebox.askquestion('Ask Question', 'Would you like to start again?')
        if answer == 'yes':
            self.restart()
        if answer == 'no':
            self.shut_down()


    def cards_score_manager(self, player, card, card_value):


        if player == "Player" and self.first_game == True:
            self.player_score = self.player_score + card_value
            self.player_cards.append(card)
            print("players deck: " + str(self.player_cards))
            self.update_labels(True)
            self.initial_check()


        if player == "Player" and self.first_game == False:
            self.player_score = self.player_score + card_value
            self.player_cards.append(card)
            print("players deck: " + str(self.player_cards))
            self.game_rules(self.player_score, "Player")


        if player == "Dealer" and self.first_game == True:
            self.dealers_score = self.dealers_score + card_value
            self.dealers_cards.append(card)
            print("Dealers deck: " + str(self.dealers_cards))
            self.update_labels(True)
            self.initial_check()



        if player == "Dealer" and self.first_game == False:
            self.dealers_score = self.dealers_score + card_value
            self.dealers_cards.append(card)
            print("Dealers deck: " + str(self.dealers_cards))
            self.game_rules(self.dealers_score, "Dealer")


    def initial_check(self):
        if self.player_score == 21:
            self.update_labels(False)
            tkinter.messagebox.showinfo("Game state", "BLACKJACK!! Player has WON")
            self.game_restart()
        if self.player_score > 21:
            self.update_labels(False)
            tkinter.messagebox.showinfo("Game state",  "Player has LOST")
            self.game_restart()




    def game_rules(self, score, player):

        if score < 21 and player == "Dealer":
            self.update_labels(False)
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            self.hand_rules()


        if score < 21 and player == "Player":
            self.update_labels(False)
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)


        if score == 21:
            self.update_labels(False)
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            tkinter.messagebox.showinfo("Game state", player + " has WON")

            self.game_restart()


        if score > 21:
            self.update_labels(False)
            print("Players score:", self.player_score)
            print("Dealers score:", self.dealers_score)
            tkinter.messagebox.showinfo("Game state", player + " has lost the game")
            self.game_restart()

    def restart(self):
        self.window.destroy()
        os.startfile("blackjack.py")

    def shut_down(self):
        self.window.destroy()

    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    BlackJack = Blackjack()
    BlackJack.run()
