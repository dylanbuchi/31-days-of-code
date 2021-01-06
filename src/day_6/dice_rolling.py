import random
import sys
import time

from collections import Counter

# Dice Rolling Simulator


def play_again():
    user_choice = input("Press enter to roll the dice again!")
    if user_choice != '':
        sys.exit()
    else:
        main()


def ask_user_how_many_dices():
    try:
        dices_to_roll = int(input("How many dices would you like to roll?\n"))
    except ValueError:
        # recursive calls until the user enters a correct input
        print('Please enter a valid number')
        ask_user_how_many_dices()
    else:
        return dices_to_roll


def print_dice(dice_value):
    number = 'o '
    string = '-----\n|' + number[dice_value < 1] + ' ' + number[
        dice_value < 3] + '|\n|' + number[dice_value < 5]
    print(string + number[dice_value & 1] + string[::-1])


def get_lucky_numbers(results):
    max_val = max(results.values())
    lucky_numbers = []

    # grab the keys from the max values
    for dice, total in results.items():
        if max_val == total:
            lucky_numbers.append(str(dice))

    return ' and '.join(lucky_numbers) if len(
        lucky_numbers) == 2 else ', '.join(lucky_numbers)


def print_stats(results):
    sorted_dices = list(sorted(results.items()))

    print(" STATS ".center(20, '*'))

    for dice, total in sorted_dices:
        print(f"Dice {dice}:\ntotal: {total} times\n")

    if len(results) > 3:
        lucky_numbers = get_lucky_numbers(results)
        numbers = make_word_plural('number', lucky_numbers)
        print(f"Your lucky {numbers} {str(lucky_numbers)}\n")


def make_word_plural(word, condition):
    # make a word plural if condition is more than 1
    return f"{word}s are" if len(condition) > 1 else f"{word} is"


def roll_dice(time_to_roll=0):
    dices = ask_user_how_many_dices()
    results = Counter()

    for dice in range(1, dices + 1):
        dice_value = random.randrange(6)
        results[dice_value + 1] += 1

        print(f"Rolling dice number #{dice}...:\n")
        time.sleep(time_to_roll)
        print_dice(dice_value)

    print_stats(results)


def main():
    try:
        # int argument in seconds to change the speed
        # for each dice roll default is 0 seconds
        roll_dice(1)
        play_again()

    except (KeyboardInterrupt):
        print('Exit Program')


if __name__ == "__main__":
    main()