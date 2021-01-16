import sys
from colorama import Fore, init


class TicTacToe:
    def __init__(self, player_symbols):
        self.board = self.create_board()
        self.player_symbols = player_symbols
        self.symbols_counts = {k: 0 for k in self.player_symbols.values()}
        self.symbol_winner = 'None'
        self.board_positions = {
            1: [0, 0],
            2: [0, 1],
            3: [0, 2],
            4: [1, 0],
            5: [1, 1],
            6: [1, 2],
            7: [2, 0],
            8: [2, 1],
            9: [2, 2]
        }

        self.winning_positions = [
            # rows
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            # cols
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            # diagonals
            [[0, 0], [1, 1], [2, 2]],
            [[2, 0], [1, 1], [0, 2]],
        ]

    def create_board(self):
        return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def get_board(self, board):
        return (Fore.YELLOW +
                "\n---------\n".join([" | ".join(i) for i in board]))

    def check_position_is_taken(self, pos):
        row, col = self.board_positions[pos]
        return not self.board[row][col] == ' '

    def put_player_symbol(self, player_symbol, pos):
        row, col = self.board_positions[pos]
        self.board[row][col] = player_symbol

    def is_board_full(self):
        for row, col in self.board_positions.values():
            board_item = self.board[row][col]
            if (board_item.isspace()):
                return False
        return True

    def print_board(self):
        print(self.get_board(self.board))

    def get_winner_name_by_symbol(self):
        symbols_players = {k: v for (v, k) in self.player_symbols.items()}
        if self.symbol_winner in symbols_players:
            winner = symbols_players[self.symbol_winner]
            return winner

    def check_winner(self):
        p1_list = []
        p2_list = []

        p1_symbol, p2_symbol = self.player_symbols.values()

        for winning_position in self.winning_positions:
            for pos in winning_position:
                row, col = pos
                item = self.board[row][col]
                if item == p1_symbol:
                    p1_list.append(1)
                elif item == p2_symbol:
                    p2_list.append(1)

            if len(p1_list) == 3:
                self.symbol_winner = p1_symbol
                return True

            if len(p2_list) == 3:
                self.symbol_winner = p2_symbol
                return True

            p1_list.clear()
            p2_list.clear()

        return False
