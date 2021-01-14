# Higher Lower Game
import sys
import random
import os

from colorama import init, Fore
from typing_extensions import IntVar
from logo import LOGO, VS_LOGO
from game_data import GAME_DATA


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_answer(string):
    try:
        answer = input(string).upper().strip()[:1]
        assert answer in 'AB' and answer

    except (AssertionError):
        print(Fore.RED + 'Please enter a valid answer')
        return get_user_answer(string)

    else:
        return answer


def get_random_choices(data):
    compared_data = random.choice(data)
    against_data = random.choice(data)

    # to not compare the same data
    while compared_data == against_data:
        compared_data = random.choice(data)
        against_data = random.choice(data)

    return compared_data, against_data


def get_game_data():
    return GAME_DATA.copy()


def play_again():
    choice = input("Press enter to play again")
    return main() if not choice else sys.exit()


def get_highest_followers_count(data_1, data_2):
    return max(data_1, data_2)


def play_higher_lower():
    score = 0
    player_is_right = True
    starting = True
    compared_data = against_data = ''
    game_data = get_game_data()

    while player_is_right:
        if (starting):
            compared_data, against_data = get_random_choices(game_data)
        else:
            while compared_data == against_data:
                against_data = random.choice(game_data)

        compared_info = get_data_info(compared_data)
        against_info = get_data_info(against_data)

        compared_followers = compared_info.pop()
        against_followers = against_info.pop()

        results = {'A': compared_followers, 'B': against_followers}

        print_data_info(compared_info, 'Compare A: ')
        print(VS_LOGO)
        print_data_info(against_info, 'Compare B: ')

        user_answer = get_user_answer(
            f"\nWho has more followers? Type 'A ' or 'B': ")

        correct_answer = get_highest_followers_count(compared_followers,
                                                     against_followers)
        user_result = results[user_answer]

        if (user_result) == correct_answer:
            clear_console()
            print()
            score += user_result
            compared_data = against_data
            starting = False
            print(Fore.CYAN + "Correct!")
            print(f"\nScore: {score}\n")

        else:
            clear_console()
            print(Fore.RED + f"Wrong Answer!")
            print(f"Score: {str(score)}")
            play_again()
            break


def get_data_info(data):
    name = data['name']
    description = data['description']
    country = data['country']
    follower_count = data['follower_count']

    return [name, description, country, follower_count]


def print_data_info(data, string):
    name, description, country = data
    an_or_a = 'an' if description[0][0] in 'AEIOU' else 'a'
    color_string = Fore.RED if 'A' in string else Fore.CYAN
    print(
        f"{color_string + string} {Fore.YELLOW + name}, {an_or_a} {description}, from {country}."
    )


def main():
    init(autoreset=True)
    print(Fore.MAGENTA + LOGO)
    try:
        play_higher_lower()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    print(os.getcwd())
    main()
