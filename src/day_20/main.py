import sys
import time

from turtle import Turtle, Screen
from snake import Snake
from food import Food

# Constants variables
SCORE_X_Y_COORDINATES = (0, 270)
GAME_OVER_X_Y_COORDINATES = (0, 100)

FONT_PEN_SETTINGS = ('ROBOTO', 30, 'normal')
FONT_SCORE_PEN_SETTINGS = ('ROBOTO', 15, 'normal')


def play_again(app, snake):
    pen = create_pen(GAME_OVER_X_Y_COORDINATES)
    choice = app.textinput("Play again",
                           "Do you want to play again?").lower().strip()

    snake.score = 0

    return main() if choice == 'yes' else pen.write(
        'BYE!', align='center',
        font=FONT_PEN_SETTINGS), time.sleep(2), app.bye()


def setup_app(app):
    app.setup(width=1200, height=800)
    app.bgcolor('#07470B')
    app.title('Snake Game')


def play_game(app, snake: Snake):
    apple = Food()
    pen_score = create_pen(SCORE_X_Y_COORDINATES)
    pen_game_over = create_pen(GAME_OVER_X_Y_COORDINATES)

    while True:
        app.update()
        if snake.check_player_passed_game_boundaries((580, 380)):
            display_user_score(pen_score, snake)
            display_game_over(pen_game_over)
            time.sleep(1)
            pen_game_over.clear()
            play_again(app, snake)
            break
        display_user_score(pen_score, snake)

        pen_score.clear()
        speed_time = snake.speed
        snake.move(snake.get_player_key(app))
        time.sleep(speed_time)
        if (snake.eat(apple)):
            apple.got_to_random_pos()


def ask_user_to_pick_snake_color_for(body_part, app):
    colors = [
        'red',
        'blue',
        'green',
        'white',
        'pink',
        'orange',
        'purple',
        'black',
    ]
    colors_text = ' - '.join(colors)
    try:
        color = app.textinput(
            title="Choose a color",
            prompt=
            f"Pick a color for the {body_part} of the snake\n{colors_text}"
        ).lower().strip()

        assert color in colors or color == ''
    except AssertionError:
        return ask_user_to_pick_snake_color_for(body_part, app)
    else:
        return color


def create_pen(coords):
    x, y = coords
    pen = Turtle()
    pen.penup()
    pen.goto(x, y)
    pen.color('white')
    pen.hideturtle()
    return pen


def display_user_score(pen, snake):
    pen.write(f"Score: {snake.score}",
              align="center",
              font=FONT_SCORE_PEN_SETTINGS)


def display_game_over(pen):
    pen.write(f"GAME OVER", align="center", font=FONT_PEN_SETTINGS)


def change_snake_colors(app, snake):
    body_color = ask_user_to_pick_snake_color_for('body', app)
    if body_color: snake.change_snake_body_color(body_color)

    head_color = ask_user_to_pick_snake_color_for('head', app)
    if head_color: snake.change_snake_head_color(head_color)


def main():
    app = Screen()
    app.reset()
    app.clear()

    setup_app(app)
    app.tracer(0)
    snake = Snake()

    change_snake_colors(app, snake)

    app.listen()
    play_game(app, snake)
    app.mainloop()


if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit()
