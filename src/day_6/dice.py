import random
import time

from collections import Counter


class Dice:
    def __init__(self, rolling_time=0):
        self.rolling_time = rolling_time
        self.stats = Counter()

    def print_dice(self, dice_value):
        number = 'o '
        string = '-----\n|' + number[dice_value < 1] + ' ' + number[
            dice_value < 3] + '|\n|' + number[dice_value < 5]
        print(string + number[dice_value & 1] + string[::-1])

    def roll_dices(self, dices_number):
        dices = dices_number
        self.rolling_a_dice(dices)

    def rolling_a_dice(self, dices):
        for dice in range(1, dices + 1):
            dice_value = random.randrange(6)
            self.stats[dice_value + 1] += 1

            print(f"Rolling dice number #{dice}...:\n")
            time.sleep(self.rolling_time)
            self.print_dice(dice_value)

    def get_dice_stats(self):
        return self.stats