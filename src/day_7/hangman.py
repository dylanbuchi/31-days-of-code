import random
import pickle
import sys
import os

from colorama import init, Fore


def hangman_pic():
    return [
        '''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\\  |
    / \\  |
        |
    ========='''
    ]


def get_file_path(*paths):
    return os.path.join(os.getcwd(), ''.join(list(paths)))


def save_player_score_to(file_name, player_name, score):
    scores = get_players_scores_from(file_name)

    with open(get_file_path(file_name), 'wb') as scores_file:
        scores[player_name] = score
        pickle.dump(scores, scores_file)


def create_scores_file(file_name):
    if not os.path.isfile(file_name):
        with open(get_file_path(file_name), 'wb') as scores_file:
            pickle.dump({}, scores_file)


def get_players_scores_from(file_name):
    with open(get_file_path(file_name), 'rb') as scores_file:
        try:
            data = pickle.load(scores_file)
        except EOFError as error:
            return {}
        return data


def get_words_list():
    with open(os.path.join(os.getcwd(), 'words.txt')) as words_file:
        words = words_file.read().strip().split()
    return words


def get_string_word(word):
    return ''.join(word).upper()


# def check_keyboardInterrupt(callback):
#     # check if the player exits the terminal with (control + C) or other if true he can exit without error
#     try:
#         return callback()
#     except KeyboardInterrupt as error:
#         print("Exit program")
#         sys.exit()


def remove_player(name, players_scores, file_name):
    del players_scores[name]
    with open(get_file_path(file_name), 'wb') as scores_file:
        pickle.dump(players_scores, scores_file)


def remove_last_player(players_scores, file_name):
    players_scores.popitem()
    with open(get_file_path(file_name), 'wb') as scores_file:
        pickle.dump(players_scores, scores_file)


def ask_player_letter():
    letter = input("Enter a letter:\n").strip().upper()[:1]
    return letter


def make_word_plural_or_singular(condition, word):
    plural_word = word

    if word.endswith('s'):
        plural_word = word + 'es'
    else:
        plural_word = word + 's'

    word = plural_word if condition > 1 else word
    return word


def print_guesses_left(player_guesses):
    guess_color = Fore.YELLOW if int(player_guesses) > 3 else Fore.RED
    print(
        f'You have {guess_color + str(player_guesses)} {make_word_plural_or_singular(player_guesses, "guess")} left!'
    )


def play_again(file_name, player_name):

    choice = input(f"{player_name}, type 'y' to play again or 'n' to exit"
                   ).lower().strip()

    if choice == 'y':
        play_game(file_name, player_name)


def get_player_name():
    return input("Enter your name to save your score:\n").title().strip()


def print_leaderboard(scores):

    if (scores):
        names_scores_sorted = sorted(scores.items(),
                                     key=lambda x: x[1],
                                     reverse=True)
        placement = 1

        print(Fore.YELLOW + "LEADERBOARD".center(40, '*'))
        print()
        print(Fore.YELLOW + "TOP 3 PLAYERS".center(40, '*'), "\n")

        for name, score in names_scores_sorted:

            score_color = Fore.CYAN if score > 0 else Fore.RED
            placement_color = Fore.YELLOW if placement <= 3 else Fore.WHITE
            name_color = Fore.GREEN if placement <= 3 else Fore.WHITE

            if placement == 4:
                print(Fore.YELLOW + "******".center(40, '*'))

            print(
                f"# {placement_color + str(placement)}: {name_color+ name} - {score_color + str(score)} {Fore.WHITE + make_word_plural_or_singular(score, 'point')}"
            )

            placement += 1

        print(Fore.YELLOW + "******".center(40, '*'))


def play_game(file_name, player_name):
    players_scores = get_players_scores_from(file_name)
    print_leaderboard(players_scores)

    hangman_pic_index = 0
    wrong_letters = []
    score = 0

    if players_scores and player_name in players_scores:
        score = players_scores[player_name]

    words_list = get_words_list()
    correct_word = random.choice(words_list).upper()

    player_guesses = 6
    word_to_guess_list = ['_' for _ in range(len(correct_word))]

    print(f'The secret word has {len(correct_word)} letters\n')

    while player_guesses:

        player_letter = ask_player_letter()

        if player_letter and player_letter in correct_word:
            indexes = [
                i for i, letter in enumerate(correct_word)
                if letter == player_letter
            ]
            for i in indexes:
                word_to_guess_list[i] = player_letter
        else:
            wrong_letters.append((player_letter))
            wrong_letters = list(set(wrong_letters))
            player_guesses -= 1
            hangman_pic_index += 1

        word_to_guess_string = get_string_word(word_to_guess_list)

        for ch in word_to_guess_string:
            word_color = Fore.WHITE if ch == '_' else Fore.CYAN
            print(f"    {word_color + ch} ".center(1), end='')
        print("\n")
        print(hangman_pic()[hangman_pic_index], '\n')
        print_guesses_left(player_guesses)

        print(f"Wrong letters: {Fore.RED + ' '.join(wrong_letters)}\n")

        if (word_to_guess_string == correct_word):
            print(f'You win! The word is {Fore.CYAN + correct_word}\n')
            break

    if (not player_guesses):
        print(
            f'Sorry! You lost! No more guesses left! The word was {Fore.CYAN + correct_word}\n'
        )

    score += player_guesses

    save_player_score_to(file_name, player_name, score)

    play_again(file_name, player_name)


def main():
    os.chdir(os.getcwd() + "/src/day_7")

    try:
        file_name = 'players-scores'
        create_scores_file(file_name)

        player_name = get_player_name()
        play_game(file_name, player_name)

    except KeyboardInterrupt:
        print("Exit Program")
        sys.exit()


if __name__ == "__main__":
    # for the color to reset at each print

    init(autoreset=True)
    main()