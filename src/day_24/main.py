import pandas
import os
import random
import sys
import re

from functools import partial
from tkinter import TclError
from colorama import Fore, init
from turtle import Turtle, Screen

FILE_PATH = os.path.abspath(
    os.path.join(os.getcwd(), 'src/day_24/data/nato_phonetic_alphabet.csv'))


def get_phonetic_alphabet_data_dict_dict_from(file_path):
    return pandas.read_csv(file_path, index_col=0, squeeze=True).to_dict()


def get_phonetic_alphabet_list(screen):
    user_word = get_user_input(screen)
    phonetic_alphabet_data_dict = get_phonetic_alphabet_data_dict_dict_from(
        FILE_PATH)
    words = create_phonetic_alphabet_words_list_from(
        user_word, phonetic_alphabet_data_dict)
    return words


def main():
    try:
        init(autoreset=True)
        screen = create_screen()
        pen = create_pen()

        phonetic_alphabet_list = get_phonetic_alphabet_list(screen)
        display_phonetic_alphabet(pen, phonetic_alphabet_list)

        screen.listen()
        screen.onclick(partial(run_again, pen))
        screen.mainloop()

    except (TclError):
        sys.exit()


def run_again(pen, x, y):
    pen.goto(x, y)
    pen.clear()
    main()


def write_to_screen(word, directions, pen, pen_color, font_specs):
    x, y = directions
    font, size, style = font_specs
    pen.goto(x, y)
    pen.color(pen_color)
    pen.write(f"{word}", font=(font, size, style))


def display_phonetic_alphabet(pen, phonetic_alphabet_list):
    y = 150
    x = -380
    white_color = 255, 255, 255

    for word in phonetic_alphabet_list:

        if check_word_passed_y_screen_limit(y) or word == ' ':
            x, y = change_directions(x, y)

        colors = get_random_rgb_colors()
        first_letter = word[0]

        write_to_screen(word=first_letter,
                        directions=(x, y),
                        pen=pen,
                        pen_color=white_color,
                        font_specs=('Consolas', 21, 'bold'))

        temp_x = x + 30

        write_to_screen(word=word[1:],
                        directions=(temp_x, y),
                        pen=pen,
                        pen_color=colors,
                        font_specs=('Consolas', 20, 'italic'))

        y -= 50


def check_word_passed_y_screen_limit(y):
    return y < -300


def change_directions(x, y):
    """change (x, y) coordinates"""
    x += 200
    y = 200
    return x, y


def create_pen():
    """Create a Turtle object to write on the screen"""
    pen = Turtle()
    pen.penup()
    pen.hideturtle()
    pen.speed(0)
    return pen


def clear_pen(pen):
    pen.clear()


def create_screen():
    screen = Screen()
    screen.setup(width=900, height=600)
    screen.title("NATO Phonetic Alphabet")
    screen.bgcolor('black')
    screen.colormode(255)
    return screen


def get_random_rgb_colors():
    rgb = []
    for _ in range(3):
        color = random.randint(50, 250)
        rgb.append(color)
    return tuple(rgb)


def get_user_input(screen):
    user_word = None
    try:
        user_word = screen.textinput(title="",
                                     prompt="Enter a word").upper().strip()
        assert re.match(r'^[a-z A-Z]+$', user_word) is not None

    except (AssertionError, AttributeError):
        if user_word is None:
            # when the user clicks the Cancel button it will exit without error
            sys.exit()

        print(f"{Fore.RED}Only letters allowed!\n")
        return get_user_input(screen)
    else:
        return user_word


def create_phonetic_alphabet_words_list_from(user_input, data_dict):
    words = [data_dict[i] for i in list(user_input)]
    return words


if __name__ == "__main__":
    main()
