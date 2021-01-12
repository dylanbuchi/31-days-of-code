# Number Guessing Game
import sys
import random

sys.path.append('src/day_9')

from logo import LOGO
from auction_program import clear_console
from colorama import init, Fore


def handle_exception(func, error_message):
    try:
        return func()
    except (AssertionError, ValueError):
        clear_console()
        print(Fore.RED + error_message)
        return handle_exception(func, error_message)


def get_player_guess():
    player_guess = int(input("Make a guess: ").strip())
    assert 1 <= player_guess <= 100
    return player_guess


def choose_difficulty():

    print(
        f"Choose a mode: {Fore.BLUE} (1)  Easy - {Fore.LIGHTGREEN_EX} (2) Hard - {Fore.RED} (3) Expert: "
    )
    choice = int(input().strip())
    mode = "Easy" if choice == 1 else "Hard" if choice == 2 else "Expert"
    print(f"{mode} mode activated! Good luck!\n")

    assert choice == 1 or choice == 2 or choice == 3
    return choice


def computer_picks_random_number(start, end):
    return random.randint(start, end)


def welcome():
    print("Welcome to the Number Guessing Game\n")


def get_player_attempts_by_difficulty(mode):
    # key: user difficulty choice choice, value: total attempts
    modes = {1: 10, 2: 5, 3: 3}
    return modes[mode]


def print_user_attempts(player_attempts):
    color = Fore.RED if player_attempts <= 3 else Fore.YELLOW
    word = 'attempts' if player_attempts > 1 else 'attempt'
    print(
        color +
        f"You have {str(player_attempts)} {word} remaining to guess the number\n"
    )


def play_again():
    choice = input("Press enter to play again!").strip()
    play_number_guessing_game() if not choice else sys.exit()


def play_number_guessing_game():
    start, end, count = 1, 100, 0

    welcome()
    target = computer_picks_random_number(start, end)
    mode = handle_exception(choose_difficulty, "Please enter a valid mode")
    player_attempts = get_player_attempts_by_difficulty(mode)
    print(f"I'm thinking of a number from {start} to {end}\n")

    while True:
        if player_attempts == 0:
            print(
                f"No more attempts left, the number was {Fore.BLUE + str(target)}"
            )
            break
        player_guess = handle_exception(
            get_player_guess, f"Please enter a valid number ({start} - {end})")

        if target > player_guess:
            print(Fore.GREEN + "Too Low")
        elif target < player_guess:
            print(Fore.YELLOW + "Too High")
        else:
            print(f"Correct! The number was {target}")
            break

        count += 1
        player_attempts -= 1
        print_user_attempts(player_attempts)

    play_again()


def main():
    init(autoreset=True)
    print(Fore.RED + LOGO)
    try:
        play_number_guessing_game()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
