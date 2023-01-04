
import random
import tkinter
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter.simpledialog import SimpleDialog
import os



LARGE_FONT_STYLE = ("Times", 20, "bold")
DEFAULT_FONT_STYLE = ("Times", 25, "bold")
HEADER_FONT_STYLE = ("Montserrat", 40, "bold")
INF_FONT_STYLE = ("Montserrat", 18, "bold")


class Blackjack:

    def __init__(self):
        self.text2 = " "
        self.player_deck = []

        self.computer_cards = []
        self.computer_score = 0

        self.player_score = 0

        self.player_cards = []



        self.cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9,
                      9, 9, 9, 10, 10, 10, 10, 'King', 'King', 'King', 'King', 'Queen', 'Queen', 'Queen', 'Queen',
                      'Joker', 'Jack', 'Jack', 'Jack', 11, 11, 11, 11]

        self.deck_cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8,
                           8, 9, 9, 9, 9, 10, 10, 10, 10, 'King', 'King', 'King', 'King', 'Queen', 'Queen', 'Queen',
                           'Queen', 'Jack', 'Jack', 'Jack', 'Jack', 11, 11, 11, 11]

        self.window = Tk()

        self.window.geometry("1250x1250")

        self.window.title("Blackjack")



        self.start_game = Button(self.window, text='Start game', command=lambda: self.call_report(False))
        self.start_game.place(x=100, y=1000, width=150, height=40)


        self.draw = Button(self.window, text='HIT', command=lambda: self.call_report(True))
        self.draw.place(x=300, y=1000, width=150, height=40)

        self.draw = Button(self.window, text='STAND', command=lambda: self.hand_logic())
        self.draw.place(x=500, y=1000, width=150, height=40)


        self.turns_label = tk.Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
        self.turns_label.place(x=50, y=500, width=500, height=100)

        self.player_live_score = tk.Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
        self.player_live_score.place(x=50, y=75, width=500, height=100)

        self.player_live_deck = tk.Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
        self.player_live_deck.place(x=50, y=250, width=500, height=100)

        self.computer_live_score = tk.Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
        self.computer_live_score.place(x=700, y=75, width=500, height=100)

        self.computer_live_deck = tk.Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
        self.computer_live_deck.place(x=700, y=250, width=500, height=100)

        self.infLabel2 = tk.Label(self.window, font=INF_FONT_STYLE, borderwidth=3, relief="solid")
        self.infLabel2.place(x=50, y=800, width=500, height=100)


    def run_script(self,boolean):



        if boolean == False:



            self.turns_label.config(text="Two cards per player generated ", bg="#D21E1E", fg="black")
            self.generate_player_cards()

            self.update_labels()

            self.infLabel2.config(text=self.text2, bg="#D21E1E", fg="black")

            self.turns_label.config(text="Players turn", bg="#D21E1E", fg="black")


        if boolean == True:

            self.turns_label.config(text="Computers run ", bg="#D21E1E", fg="black")

            self.card_deducting("Player")


            self.update_labels()

            self.turns_label.config(text="Players turn", bg="#D21E1E", fg="black")



    def call_report(self,boolean):
            self.run_script(boolean)

    def update_labels(self):
        self.player_live_score.config(text='Player score : ' + str(self.player_score), bg="#D21E1E", fg="black")
        self.player_live_deck.config(text='Players deck : ' + str(self.player_cards), bg="#D21E1E", fg="black")

        self.computer_live_score.config(text='Computer score : ' + str(self.computer_score), bg="#D21E1E", fg="black")
        self.computer_live_deck.config(text='Computers deck : ' + (str(self.computer_cards[0])), bg="#D21E1E", fg="black")



    def stand(self):
        self.computer_turn()

    def computer_turn(self):

        self.card_deducting("computer")
        self.window.after(1000, self.update_labels())

        self.turns_label.config(text="Computer run", bg="#D21E1E", fg="black")





    def stand_choice(self, choice):
        if choice == "player":
            self.update()
        if choice == "computer":
            self.turns_label.config(text="Players turn", bg="#D21E1E", fg="black")



    def generate_player_cards(self):

        self.card_deducting("computer")
        self.card_deducting("computer")

        self.card_deducting("Player")
        self.card_deducting("Player")

        self.start_game.place_forget()

        print("player cards :", self.player_cards)
        print("computer cards :", self.computer_cards)
        print("player score :", self.player_score)
        print("computer score :", self.computer_score)

        print(self.deck_cards)
        print(self.cards)


    def select_random(self):
        if len(self.deck_cards) == 0:
            print('the list is empty')
            self.card = []
        else:
            print(len(self.deck_cards))
            return random.choice(self.deck_cards)

    def innitiate_game(self):
        self.generate_player_cards()


    def computer_ace_choice(self,player):
        if player == "computer":
            if self.computer_score <= 10:
                self.ace_value_selector(player, 0)
            else:
                self.ace_value_selector(player, 1)
        if player == "Player":
            if self.player_score <= 10:
                self.ace_value_selector(player, 0)
            else:
                self.ace_value_selector(player, 1)

    def card_deducting(self, player):

        self.card = []
        self.card = self.select_random()

        print(self.card)

        if self.card == 1:
            if player == "computer":
                self.computer_ace_choice(player)
            if player == "Player":
                self.computer_ace_choice(player)

        if self.card == 11:
            if player == "computer":
                self.computer_ace_choice(player)
            if player == "Player":
                self.computer_ace_choice(player)

        if self.card == 'King':
            self.deck_cards.remove(self.card)
            self.text2 = "KING"
            self.cards_catcher(player, self.text2, 10)
            print('KQJ', self.deck_cards)


        if self.card == 'Queen':
            self.deck_cards.remove(self.card)
            self.text2 = "QUEEN"
            self.cards_catcher(player, self.text2, 10)
            print('KQJ', self.deck_cards)


        if self.card == 'Jack':
            self.deck_cards.remove(self.card)
            self.text2 = "JACK"
            self.cards_catcher(player, self.text2, 10)
            print('KQJ', self.deck_cards)


        if self.card in range(2, 11, 1):
            self.deck_cards.remove(self.card)
            self.text2 = self.card
            self.cards_catcher(player, self.text2, self.card)
            print('two to ten:', self.deck_cards)


    def ace_value_selector(self, player, value):
        if value == 0:
            self.text2 = "11"
            self.cards_catcher(player, self.text2, 11)
            print('ACE:', self.deck_cards)
            self.deck_cards.remove(1)
            self.deck_cards.remove(11)


        if value == 1:
            self.text2 = "1"
            self.cards_catcher(player, self.text2, 1)
            print('ACE:', self.deck_cards)
            self.deck_cards.remove(1)
            self.deck_cards.remove(11)



    def show_message(self,player):
        dlg = SimpleDialog(self.window, title='Question!', text='What value of ACE?',
                           buttons=['11', '1'])
        answer = dlg.go()

        self.ace_value_selector(player,answer)
        print("answer: ", answer)


    def game_restart(self):
        answer = tkinter.messagebox.askquestion('Ask Question', 'Would you like to start again?')
        if answer == 'yes':
            self.restart()
        if answer == 'no':
            self.shut_down()

    def cards_catcher(self, player, card, card_value):
        if player == "Player":
            self.player_score = self.player_score + card_value
            self.player_cards.append(card)
            print("players deck: " + str(self.player_cards))
            self.game_brain(self.player_score, "Player")

        if player == "computer":
            self.computer_score = self.computer_score + card_value

            self.computer_cards.append(card_value)

            print("computers deck: " + str(self.computer_cards))
            self.game_brain(self.computer_score, "computer")

    def hand_logic(self):
        if self.player_score >= self.computer_score:
            while self.player_score >= self.computer_score:
                self.computer_turn()

        if self.player_score < self.computer_score:
            self.window.update()

            tkinter.messagebox.showinfo("Game state", "Computer has WON")
            self.game_restart()






    def game_brain(self, score, player):

        if score < 21 and player == "computer":
            self.update_labels()
            print("player score:", self.player_score)
            print("computer score:", self.computer_score)
            self.window.update()

        if score < 21 and player == "Player":
            self.update_labels()
            print("player score:", self.player_score)
            print("computer score:", self.computer_score)
            self.window.update()

        if score == 21:
            self.update_labels()
            print("player score:", self.player_score)
            print("computer score:", self.computer_score)
            tkinter.messagebox.showinfo("Game state", player + " has WON")
            self.window.update()
            self.game_restart()

        if score > 21:
            self.update_labels()
            print("player score:", self.player_score)
            print("computer score:", self.computer_score)
            tkinter.messagebox.showinfo("Game state", player + " has lost the game")
            self.window.update()
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
