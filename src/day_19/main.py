import os
import random
import sys
import time

from turtle import Turtle, Screen
from player import Player


def get_player_bet_amount(player, app):
    player.set_player_bet(
        int(
            app.numinput(title="Place your bet!",
                         prompt="Bet amount",
                         minval=1,
                         maxval=player.balance)))


def get_player_turtle_color(player, app, colors):
    colors = get_colors()
    turtle_colors = ', '.join([i for i in colors])

    try:
        color = (app.textinput(
            title="Choose a turtle",
            prompt=f"Which turtle will win the race !?\n{turtle_colors}")
                 ).lower().strip()
        assert color in colors
        player.set_player_turtle_color(color)
    except AssertionError:
        get_player_turtle_color(player, app, colors)


def move_turtles(turtles, max_distance):
    for turtle in turtles:
        move_turtle_randomly(turtle, max_distance)
        if turtle_has_passed_finish_line(turtle):
            return turtle
    return False


def move_turtle_randomly(turtle, max_distance):
    n = random.randint(0, max_distance)
    turtle.forward(n)


def place_turtle_to_pos(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)


def get_turtles(colors):
    turtles = []
    for color in colors:
        turtle = Turtle(shape='turtle')
        turtle.color(color)
        turtle.turtlesize(2)
        turtles.append(turtle)
    return turtles


def get_colors():
    return [
        'red',
        'blue',
        'yellow',
        'green',
        'orange',
        'white',
    ]


def setup_app(app):
    app.listen()
    app.title("Turtle Race")
    app.setup(width=600, height=600)
    app.bgpic("src/day_19/images/race.gif")
    app.bgcolor('black')


def move_turtles_to_starting_positions(turtles):
    x = -230
    y = -200

    for turtle in turtles:
        place_turtle_to_pos(turtle, x, y)
        y += 80


def check_user_won_bet(winner_color, player):
    if winner_color == player.turtle_color:
        player.player_wins()
        return True
    return False


def play_again(app, player):
    app.reset()
    app.bgpic("src/day_19/images/race.gif")
    response = app.textinput(
        title="Play", prompt=f"Do you want to play again?").lower().strip()
    if response == 'yes':
        race(app, player)
    else:
        say_bye(app)


def turtle_has_passed_finish_line(turtle):
    return turtle.xcor() >= 190


def race(app, player):
    current_balance_coordinates = (130, 260)
    winner_coordinates = (-230, 200)

    balance_pen = set_pen('white', current_balance_coordinates)
    winner_pen = set_pen('white', winner_coordinates)

    display_user_balance(balance_pen, player)

    colors = get_colors()
    turtles = get_turtles(colors)

    get_player_turtle_color(player, app, colors)
    get_player_bet_amount(player, app)

    move_turtles_to_starting_positions(turtles)

    while True:
        winner = move_turtles(turtles, max_distance=20)
        if winner:
            balance_pen.clear()
            display_winner(winner_pen, winner)
            winner_color = winner.pencolor()
            check_user_won_bet(winner_color, player)
            display_user_balance(balance_pen, player)
            time.sleep(3)
            break

    if player.balance_is_zero():
        say_bye(app)
    else:
        play_again(app, player)


def display_user_balance(pen, player):
    pen.write(f"Balance: ${player.balance}", font=("Arial", 10, "normal"))


def say_bye(app):
    app.reset()
    pen = set_pen('white')
    pen.write('Bye bye', font=('Arial', 20, 'normal'))
    time.sleep(3)
    sys.exit()


def set_pen(color, coordinates=(-230, 200)):
    x, y = coordinates
    pen = Turtle()
    pen.pendown
    pen.goto(x, y)
    pen.pendown
    pen.hideturtle()
    pen.color(color)
    return pen


def get_winner_message(color):
    return f"{color.title()} turtle wins the race!"


def display_winner(pen, winner, coordinates=(-230, 220)):
    color = winner.pencolor()
    pen = set_pen('white', coordinates)
    pen.write(get_winner_message(color), font=('Arial', 12, 'normal'))


def main():
    try:
        player = Player(balance=100)
        app = Screen()
        setup_app(app)
        race(app, player)
        app.mainloop()
    except:
        sys.exit()


if __name__ == "__main__":
    main()