from turtle import Turtle
from functools import partial


class Frog(Turtle):
    def __init__(self, shape):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.go_to_starting_position()
        self.lvl = 1

    def reset_lvl(self):
        self.lvl = 1

    def go_to_starting_position(self):
        self.goto(0, -350)

    def _move(self):
        y = self.ycor() + 20
        self.goto(0, y)

    def move(self, screen):
        """move the frog on up arrow key press"""
        screen.onkey(self._move, 'Up')

    def frog_passed_lvl(self, limit):
        if self.ycor() >= limit:
            self.go_to_starting_position()
            self.lvl += 1
            return True
        return False
