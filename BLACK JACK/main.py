import random
import player


class Blackjack:
    bets = [5, 10, 25, 50, 100, 250, 500]
    human = player.Player('Player', bets)
    dealer = player.Player('Dealer', bets)

    def print_game(self):
        dealer_cards = self.dealer.cards
        player_cards = self.human.cards
        length = len(dealer_cards)
        print(f'\nDealer: {dealer_cards[:length - 1]}, * = {sum(dealer_cards)}')
        print(f' You  : {player_cards} = {sum(player_cards)}\n')

    def take_card(self):
        ace = random.randint(1, 11)
        jack = queen = king = 10
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace]
        return deck[random.randint(0, 13)]

    def place_bet(self):
        while True:
            selected_bet = input('put a bet (5,10,25,50,100): ')
            money = self.human.money
            if selected_bet.isdigit() and int(selected_bet) in self.bets and int(selected_bet) <= money:
                self.human.bet = int(selected_bet)
                break
            else:
                print('Try again')

    def compare_cards(self):
        dealer_cards = sum(self.dealer.cards)
        player_cards = sum(self.human.cards)
        if player_cards == dealer_cards:
            print('\nPUSH')
            return True
        elif player_cards < dealer_cards:
            print('\nLOSE')
            return True

    def dealer_roll(self):
        computer = self.dealer
        while True:
            computer.hit(self.take_card())
            self.print_game()
            if computer.check_blackjack_and_bust() or self.compare_cards():
                return True
            else:
                continue

    def actions(self):
        game_on = True
        while game_on:
            choice = input('H for hit / S for stand:').capitalize()
            if self.human.check_blackjack_and_bust() or self.dealer.check_blackjack_and_bust():
                game_on = False
            if choice == 'H':
                self.human.hit(self.take_card())
                self.print_game()
                if self.human.check_blackjack_and_bust():
                    game_on = False
            elif choice == 'S':
                if self.compare_cards() or self.dealer_roll():
                    game_on = False

    def play(self):
        self.place_bet()
        self.dealer.cards = [self.take_card(), self.take_card()]
        self.human.cards = [self.take_card(), self.take_card()]
        self.print_game()
        self.actions()


Blackjack().play()
