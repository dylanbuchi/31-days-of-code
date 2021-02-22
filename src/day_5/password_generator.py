import random
import string


class PasswordGenerator:
    def __init__(
        self,
        letters_amount: int,
        symbols_amount: int,
        numbers_amount: int,
    ):
        self.letters_amount = letters_amount
        self.symbols_amount = symbols_amount
        self.numbers_amount = numbers_amount

        self.letters = list(string.ascii_letters)
        self.symbols = list(string.punctuation)
        self.numbers = [i for i in range(10)]

        self.password = []

    def generate_password(self):
        self._append_to_password_from(self.letters, self.letters_amount)
        self._append_to_password_from(self.symbols, self.symbols_amount)
        self._append_to_password_from(self.numbers, self.numbers_amount)

        random.shuffle(self.password)
        return ''.join(self.password)

    def _append_to_password_from(self, lst: list, amount: int):
        for _ in range(amount):
            ch = random.choice(lst)
            self.password.append(str(ch))
