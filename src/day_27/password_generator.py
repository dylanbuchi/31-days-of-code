import random


class PasswordGenerator:
    def __init__(self):

        self.lower_letters_list = [chr(i) for i in range(97, 123)]
        self.letters_list = [i.upper() for i in self.lower_letters_list
                             ] + self.lower_letters_list

        self.numbers_list = [i for i in range(10)]
        self.symbols_list = [
            '!',
            '#',
            '$',
            '%',
            '&',
            '(',
            ')',
            '*',
            '+',
            '.',
            '-',
            '=',
        ]

    def append_random_character_to_password_from(self, lst, random_number,
                                                 password_list):
        for _ in range(random_number):
            password_list.append(str(random.choice(lst)))

    def generate_password(self):
        password_list = []

        letters_count = random.randint(8, 10)
        symbols_count = random.randint(2, 4)
        numbers_count = random.randint(2, 4)

        self.append_random_character_to_password_from(self.letters_list,
                                                      letters_count,
                                                      password_list)
        self.append_random_character_to_password_from(self.symbols_list,
                                                      symbols_count,
                                                      password_list)
        self.append_random_character_to_password_from(self.numbers_list,
                                                      numbers_count,
                                                      password_list)

        random.shuffle(password_list)

        return ''.join(password_list)
