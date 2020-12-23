import random
import player


class Blackjack:
    bets = [5, 10, 25, 50, 100]
    human = player.Player('Player', bets)
    computer = player.Player('Dealer', bets)

    def draw_gameplay(self):
        dealer_cards = self.computer.cards
        player_cards = self.human.cards
        length = len(dealer_cards)
        print('')
        print(f'Dealer: {dealer_cards[:length - 1]}, * = {sum(dealer_cards)}')
        print(f' You  : {player_cards} = {sum(player_cards)}')
        print('')

    def pick_card(self):
        ace = random.randint(1, 11)
        jack = queen = king = 10
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace]
        return deck[random.randint(0, 13)]

    def place_bet(self):
        while True:
            user_input = input('put your bet (5,10,25,50,100): ')
            money = self.human.money

            if user_input.isdigit() and int(user_input) in self.bets and int(user_input) <= money:
                self.human.bet = int(user_input)
                break
            else:
                print('Try again')

    def compare(self):
        dealer_cards = sum(self.computer.cards)
        player_cards = sum(self.human.cards)
        if player_cards == dealer_cards:
            print('')
            print('PUSH')
            return True
        elif player_cards < dealer_cards:
            print(self.human.bet)
            print('')
            print('LOSE')
            return True

    def dealer_roll(self):
        computer = self.computer
        while True:
            self.computer.hit(self.pick_card())
            self.draw_gameplay()
            if computer.check_blackjack_and_bust() or self.compare():
                return True
            else:
                continue

    def hit_or_stand(self):
        game_on = True
        while game_on:
            choice = input('H for hit or S for stand:').capitalize()
            if self.human.check_blackjack_and_bust() or self.computer.check_blackjack_and_bust():
                game_on = False
            if choice == 'H':
                self.human.hit(self.pick_card())
                self.draw_gameplay()
                if self.human.check_blackjack_and_bust():
                    game_on = False
            elif choice == 'S':
                if self.compare() or self.dealer_roll():
                    game_on = False

    def play(self):
        self.place_bet()
        self.computer.cards = [self.pick_card(), self.pick_card()]
        self.human.cards = [self.pick_card(), self.pick_card()]
        self.draw_gameplay()
        self.hit_or_stand()


Blackjack().play()
