import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x = 10
        self.y = 10
        self.speed = 0.04

    def move_ball(self):
        x, y = self.pos()
        x += self.x
        y += self.y
        self.goto(x, y)

    def bounce_of_wall(self, walls):
        up_wall, down_wall = walls
        if (self.ycor() >= up_wall + 30 or self.ycor() <= down_wall - 30):
            self.bounce_Y()

    def bounce_Y(self):
        self.y *= -1

    def bounce_X(self):
        self.x *= -1
        self.speed -= 0.005
        if self.speed <= 0.01:
            self.speed = 0.01

    def ball_scored(self, score, limits):
        right_limit, left_limit = limits
        if (self.xcor() >= right_limit + 30):
            self.reset_ball()
            return 'right'
        if (self.xcor() <= left_limit - 30):
            self.reset_ball()
            return 'left'

    def bounce_paddle(self, paddles):
        left_paddle, bot_paddle = paddles

        if self.distance(left_paddle) < 40 and self.xcor() < -340:
            self.bounce_X()
        elif self.distance(bot_paddle) < 40 and self.xcor() > 340:
            self.bounce_X()

    def is_ball_out_of_bounds(self, limits):
        right, left = limits
        if self.xcor() >= right or self.xcor() <= left:
            self.reset_ball()
            return True
        return False

    def reset_ball(self):
        self.goto(0, 0)
        self.speed = 0.04
        self.bounce_X()
