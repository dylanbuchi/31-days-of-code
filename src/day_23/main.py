import pandas
import os
import time

from functools import partial
from turtle import Turtle, Screen

IMAGE_PATH = os.path.abspath('./src/day_23/data/blank_states_img.gif')
DATA_PATH = os.path.abspath('./src/day_23/data/50_states.csv')


def display_score(pen, score):
    pen.goto(-200, 210)
    pen.write(f"Score: {score}/50", font=('Arial', 12, 'normal'))


def display_lives(pen, lives):
    pen.goto(80, 220)
    pen.write(f"Lives left: {lives} ", font=('Arial', 8, 'normal'))


def get_states_data():
    return pandas.read_csv(DATA_PATH)


def create_screen():
    screen = Screen()
    screen.bgpic(IMAGE_PATH)
    screen.setup(width=700, height=500)
    screen.title("US States Quiz")
    screen.listen()
    return screen


def get_state_name_coordinate_dict(states_data):
    state_name_coordinates = {}

    states_names = states_data['state'].tolist()
    states_x = states_data['x'].tolist()
    states_y = states_data['y'].tolist()

    for i in range(len(states_names)):
        state_name_coordinates[states_names[i]] = (states_x[i], states_y[i])

    return state_name_coordinates


def get_state_names(states_data):
    states_names = states_data['state'].tolist()
    return states_names


def create_pen():
    pen = Turtle()
    pen.penup()
    pen.hideturtle()
    pen.speed(0)
    return pen


def play_US_state_quiz(screen):
    score = 0
    lives = 3

    pen = create_pen()
    pen_score = create_pen()
    pen_game_over = create_pen()
    pen_lives = create_pen()

    states_data = get_states_data()
    states_names = get_state_names(states_data)
    state_name_coordinates = get_state_name_coordinate_dict(states_data)

    while states_names and lives:
        pen_lives.clear()
        display_lives(pen_lives, lives)

        user_state_name = ask_user_to_guess_state(screen)

        if check_user_response(user_state_name, states_names):
            screen.onclick(partial(write_to_map, pen, user_state_name))
            x, y = state_name_coordinates[user_state_name]
            write_to_map(pen, user_state_name, x, y)
            states_names.remove(user_state_name)
            score += 1
        else:
            lives -= 1

        pen_score.clear()

        display_score(pen_score, score)

    if not lives:
        pen_lives.clear()
        display_lives(pen_lives, lives)

        pen_score.clear()
        display_game_over(pen_game_over)
        display_score(pen_score, score)
        time.sleep(2)
        pen_game_over.clear()
        display_remaining_states(pen, states_names, state_name_coordinates)


def display_remaining_states(pen, states_names, state_name_coordinate):
    for name in states_names:
        x, y = state_name_coordinate[name]
        write_to_map(pen, name, x, y)


def display_game_over(pen):
    pen.goto(0, 0)
    pen.write('Game Over', align='center', font=("Arial", 20, 'normal'))


def check_user_response(user_state, states):
    return user_state in states


def main():
    screen = create_screen()
    play_US_state_quiz(screen)
    screen.mainloop()


def ask_user_to_guess_state(screen):
    user_choice = screen.textinput(title="",
                                   prompt="Enter state name:").title().strip()
    return user_choice


def write_to_map(pen, user_state_name, x, y):
    pen.goto(x, y)
    pen.write(user_state_name, font=('Arial', 5, 'normal'))


if __name__ == "__main__":
    main()