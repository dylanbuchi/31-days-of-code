import time
import sys

from turtle import Turtle, Screen
from tkinter import TclError

from ball import Ball
from score import Score
from paddle import Paddle

LIMITS_Y = (250, -250)
LIMITS_X = (400, -400)


def create_screen():
    game_screen = Screen()
    game_screen.setup(width=800, height=600)
    game_screen.bgcolor('black')
    game_screen.tracer(0)
    game_screen.listen()
    game_screen.title('Pong Game')

    return game_screen


def move_bot(paddle):
    paddle.bot_move()


def display_score(score):
    return score


def check_winner(result, score):
    if result == 'right':
        score.left_score += 1
    elif result == 'left':
        score.right_score += 1
    score.update_score()


def ball_moves(ball, left_paddle, bot_paddle, score):
    ball.move_ball()
    ball.bounce_of_wall(LIMITS_Y)
    ball.bounce_paddle((left_paddle, bot_paddle))
    result = ball.ball_scored(score, LIMITS_X)
    check_winner(result, score)


def play_pong_game(game_screen):
    left_paddle = Paddle()
    bot_paddle = Paddle()
    ball = Ball()
    score = Score()

    bot_paddle.place_paddle_to((350, 0))
    left_paddle.place_paddle_to((-350, 0))

    while True:
        score
        left_paddle.move_up_down(game_screen, LIMITS_Y)
        bot_paddle.bot_move(ball, LIMITS_Y)

        ball_moves(ball, left_paddle, bot_paddle, score)

        time.sleep(ball.speed)
        game_screen.update()


def main():
    game_screen = create_screen()
    play_pong_game(game_screen)
    game_screen.mainloop()


if __name__ == "__main__":
    try:
        main()
    except TclError:
        sys.exit()
