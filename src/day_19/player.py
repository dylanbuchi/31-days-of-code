class Player:
    def __init__(self, balance):
        self.balance = balance
        self.turtle_color = None
        self.current_bet = 0

    def set_player_bet(self, bet_amount):
        self.current_bet = bet_amount
        self.balance -= bet_amount
        self.balance_is_zero()

    def balance_is_zero(self):
        if self.balance <= 0:
            self.balance = 0
            return True
        return False

    def set_player_turtle_color(self, color):
        self.turtle_color = color

    def player_wins(self):
        self.balance += self.current_bet * 2
