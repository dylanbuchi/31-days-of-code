import random
import os
import sys

from functools import partial
from colorama import Fore, init

from tic_tac_toe import TicTacToe
from user_interface import UserInterface


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_player_pos(player, ui):
    error_message = ui.create_error_message('Please enter a correct position!')
    return ui.handle_exception(partial(ui.ask_player_a_position, player),
                               error_message)


def get_player_symbol(player, ui):
    clear_console()
    error_message = ui.create_error_message(
        'Please enter a correct symbol! Numbers are not allowed')
    return ui.handle_exception(partial(ui.ask_player_to_choose_symbol, player),
                               error_message)


def get_player_name(ui):
    clear_console()
    error_message = ui.create_error_message(
        'Please enter a correct symbol! Numbers are not allowed')
    return ui.handle_exception(ui.ask_player_name, error_message)


def player_plays(player, player_symbol, game_board, userinterface, rounds):
    clear_console()
    print(f"Round {rounds}:\n")
    game_board.print_board()
    print(f"\n{player}, It's your turn: \n")
    p1_pos = get_player_pos(player, userinterface)

    while game_board.check_position_is_taken(p1_pos):
        clear_console()
        print(Fore.RED + "This position is already taken")
        game_board.print_board()
        p1_pos = get_player_pos(player, userinterface)

    game_board.put_player_symbol(player_symbol, p1_pos)


def get_winner(game_board, scores):
    if (game_board.check_winner()):
        winner = game_board.get_winner_name_by_symbol()
        scores[winner] += 1
        print(f"\n{winner} wins!")
        return


def play_game(p1_name, p2_name, userinterface, scores, rounds):
    clear_console()

    players_symbols = userinterface.players_symbols

    has_won = False
    game_board = TicTacToe(players_symbols)

    players = [p1_name, p2_name]
    index = random.randint(0, 1)

    first_player = players.pop(index)
    other_player = players.pop()

    p1_symbol = players_symbols[first_player]
    p2_symbol = players_symbols[other_player]

    while True:
        player_plays(first_player, p1_symbol, game_board, userinterface,
                     rounds)
        has_won = game_board.check_winner()

        if has_won:
            clear_console()
            game_board.print_board()
            get_winner(game_board, scores)
            break

        if (game_board.is_board_full()):
            clear_console()
            game_board.print_board()
            print("\nIt's a draw!")
            break

        player_plays(other_player, p2_symbol, game_board, userinterface,
                     rounds)
        has_won = game_board.check_winner()

        if has_won:
            clear_console()
            game_board.print_board()
            get_winner(game_board, scores)
            break

        if (game_board.is_board_full()):
            print("\nIt's a draw!")
            break

        clear_console()
    print_scores(scores)
    rounds += 1
    play_again(p1_name, p2_name, userinterface, scores, rounds)


def play_again(p1_name, p2_name, userinterface, scores, rounds):
    choice = input("\nPress enter to play again!").strip()
    if not choice:
        play_game(p1_name, p2_name, userinterface, scores, rounds)
    else:
        sys.exit()


def print_scores(scores):
    for k, v in scores.items():
        print(f"\n{k}, score: {Fore.BLUE} {v}")


def user_interface():
    user_interface = UserInterface()

    p1_name = get_player_name(user_interface)
    p2_name = get_player_name(user_interface)

    p1_symbol = get_player_symbol(p1_name, user_interface)
    p2_symbol = get_player_symbol(p2_name, user_interface)

    user_interface.print_symbol(p1_name, p1_symbol)
    user_interface.print_symbol(p2_name, p2_symbol)

    scores = {p1_name: 0, p2_name: 0}
    rounds = 1
    play_game(p1_name, p2_name, user_interface, scores, rounds)


def main():
    try:
        user_interface()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    init(autoreset=True)
    main()
