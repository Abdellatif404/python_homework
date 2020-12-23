class Player:
    bet = 0
    money = 2000
    cards = []

    def __init__(self, bets):
        self.bets = bets

    def hit(self, card):
        self.cards.append(card)

    def check_blackjack(self):
        if sum(self.cards) == 21:
            print(self.bet*2)
            print('BLACKJACK')
            return True

    def check_bust(self):
        if sum(self.cards) > 21:
            print(self.bet)
            print('BUST')
            return True
