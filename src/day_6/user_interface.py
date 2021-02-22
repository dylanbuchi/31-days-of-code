import sys

from dice import Dice


class UserInterface():
    def run_app(self):
        try:
            dice = Dice(rolling_time=1)
            dices_to_roll = self.ask_user_how_many_dices()
            dice_stats = dice.get_dice_stats()

            dice.roll_dices(dices_to_roll)
            self.print_stats(dice_stats)
            self.play_again()
            
        except (KeyboardInterrupt):
            print('Exit Program')
            sys.exit()

    def ask_user_how_many_dices(self):
        try:
            dices_to_roll = int(
                input("How many dices would you like to roll?\n"))
        except ValueError:
            # recursive calls until the user enters a correct input
            print('Please enter a valid number')
            self.ask_user_how_many_dices()
        else:
            return dices_to_roll

    def print_stats(self, results):
        sorted_dices = list(sorted(results.items()))
        print(" STATS ".center(20, '*'))

        for dice, total in sorted_dices:
            print(f"Dice {dice}:\ntotal: {total}\n")

        if len(results) > 3:
            lucky_numbers = self.get_lucky_numbers(results)
            numbers = self.make_word_plural('number', lucky_numbers)
            print(f"Your lucky {numbers} {str(lucky_numbers)}\n")

    def get_lucky_numbers(self, results):
        max_val = max(results.values())
        lucky_numbers = []

        # grab the keys from the max values
        for dice, total in results.items():
            if max_val == total:
                lucky_numbers.append(str(dice))

        return ' and '.join(lucky_numbers) if len(
            lucky_numbers) == 2 else ', '.join(lucky_numbers)

    def make_word_plural(self, word, condition):
        # make a word plural if condition is more than 1
        return f"{word}s are" if len(condition) > 1 else f"{word} is"

    def play_again(self):
        user_choice = input("Press enter to roll the dice again!")
        if user_choice != '':
            sys.exit()
        else:
            self.run_app()


if __name__ == "__main__":
    ui = UserInterface()
    ui.run_app()