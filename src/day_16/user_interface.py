from colorama import Fore, init
from tic_tac_toe import TicTacToe
import random


class UserInterface:
    def __init__(self):
        self.players_symbols = {}
        self.player_count = 1

    def ask_player_name(self):
        player_name = input(f"Player {self.player_count}: ").strip().title()
        assert len(player_name)

        if player_name in self.players_symbols:
            print(Fore.RED +
                  "This name is already taken! Please choose another one")
            return self.ask_player_name()

        self.players_symbols[player_name] = ''
        self.player_count += 1
        return player_name

    def check_player_names(self, player):
        return player in self.players_symbols

    def create_error_message(self, error_message):
        return Fore.RED + error_message

    def handle_exception(self, function, error_message):
        try:
            return function()
        except (AssertionError, ValueError):
            print(error_message)
            return self.handle_exception(function, error_message)

    def ask_player_to_choose_symbol(self, player):
        symbol = ''
        if player == 'Bot':
            symbol = random.choice(['o', 'x']).upper()
        else:
            symbol = input(
                f"\n{player}, Choose a symbol for the game: ").upper().strip()
            assert not symbol.isdigit() and len(symbol) == 1
        if (self.check_symbols(symbol)):
            print(Fore.RED +
                  "This symbol is taken, please choose another one\n")
            return self.ask_player_to_choose_symbol(player)
        else:
            self.players_symbols[player] = symbol
        return symbol

    def ask_player_a_position(self, player):
        if player == 'Bot':
            return random.randint(1, 9)
        else:
            pos = input(f"Choose a position: ").strip()
            assert 1 <= int(pos) <= 9
            return int(pos)

    def print_symbol(self, player, symbol):
        print(f"{player} plays with {symbol}\n")

    def check_symbols(self, symbol):
        return symbol in self.players_symbols.values()
