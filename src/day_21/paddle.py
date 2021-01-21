from turtle import Turtle
from functools import partial
import random
import time

# constant variables
KEYS = ('Up', 'Down')


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(4, 0.2, 15)
        self.penup()

    def place_paddle_to(self, coords: tuple):
        x, y = coords
        self.goto(x, y)

    def bot_move(self, ball, limits_Y):
        n = random.randint(0, 20)
        ball_x, ball_y = ball.pos()
        x, y = self.pos()
        up_limit, down_limit = limits_Y

        if y >= ball_y:
            y -= n
        else:
            y += n
        self.goto(x, y)

    def move_up_down(self, game_screen, limits_Y):
        UP, DOWN = KEYS
        for key in KEYS:
            game_screen.onkey(partial(self._move, key, limits_Y), key)

    def _move(self, key, limits_Y):
        x, y = self.pos()
        up_limit, down_limit = limits_Y
        UP, DOWN = KEYS

        if key == UP:
            if y >= up_limit - 20:
                y -= 100
                self.goto(x, y)
            self.goto(x, y + 48)
        else:
            if y <= down_limit + 25:
                y += 100
                self.goto(x, y)
            self.goto(x, y - 48)
