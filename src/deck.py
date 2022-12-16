import random




class Deck:



    def __init__(self):
        self.JQK = ['Jack','Queen','King']




        self.cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ,10,10,10,10,10, 11, 11, 11, 11]
        self.deck_cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ,10,10,10,10,10, 11, 11, 11, 11]


    def generate_player_cards(self):
        self.player_one_cards = []
        self.player_two_cards = []
        self.random_in_number = []

        self.random_in_number = self.select_random()
        self.player_one_cards.append(self.random_in_number)
        self.deck_cards.remove(self.random_in_number)
        self.random_in_number = []

        self.random_in_number = self.select_random()
        self.player_one_cards.append(self.random_in_number)
        self.deck_cards.remove(self.random_in_number)
        self.random_in_number = []

        self.random_in_number = self.select_random()
        self.player_two_cards.append(self.random_in_number)
        self.deck_cards.remove(self.random_in_number)
        self.random_in_number = []

        self.random_in_number = self.select_random()
        self.player_two_cards.append(self.random_in_number)
        self.deck_cards.remove(self.random_in_number)
        self.random_in_number = []

        print(self.player_one_cards)
        print(self.player_two_cards)
        print(self.deck_cards)
        print(self.cards)



    def select_random(self):
        self.card = []
        self.card = random.choice(self.deck_cards)
        return self.card
        #print(random.choice(self.cards))

    def ten_card_generator(self):
        self.jacks = 4
        self.queens = 4
        self.kings = 4
        if self.ten_card == 'Jack' and self.jacks >= 2:
            self.jacks = self.jacks - 1
        else:
            self.jacks = self.jacks - 1
            self.cards.remove(10)

        if self.ten_card == 'Queen' and self.queens >= 2:
            self.queens = self.queens - 1
        else:
            self.queens = self.queens - 1
            self.cards.remove(10)

        if self.ten_card == 'King' and self.kings >= 2:
            self.kings = self.kings - 1
        else:
            self.kings = self.kings - 1
            self.cards.remove(10)
    def ace_card_generator(self, choice):
       self.aces = 4
       if choice == 'eleven' and self.aces >= 2:
           self.aces = self.aces - 1
       else:
           self.aces= self.aces- 1
           self.cards.remove(11)

       if choice == 'one' and self.aces >= 2:
           self.aces = self.aces - 1
       else:
           self.aces = self.aces - 1
           self.cards.remove(11)

    def num_cards_generator(self):
        self.two = 4
        self.three = 4
        self.four = 4
        self.five = 4
        self.six = 4
        self.seven = 4
        self.eight = 4
        self.nine = 4





    def card_deducting(self):

        if self.card == 10:
            self.ten_card = [ ]
            self.ten_card = random.choice(self.JQK)

        if self.card == 1:
            self.ace_card_generator('one')

        if self.card == 11:
            self.ace_card_generator('eleven')



