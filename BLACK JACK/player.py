class Player:
    bet = 0
    money = 5000
    cards = []

    def __init__(self, roll, bets):
        self.roll = roll
        self.bets = bets

    def hit(self, card):
        self.cards.append(card)

    def check_blackjack_and_bust(self):
        if sum(self.cards) == 21:
            self.money += self.bet*2
            print(f'{self.roll} BLACKJACK')
            print(f'your account balance: {self.money} (+{self.bet*2})')
            return True
        elif sum(self.cards) > 21:
            self.money -= self.bet
            print(f'{self.roll} BUST')
            print(f'your account balance: {self.money} (-{self.bet})')
            return True

