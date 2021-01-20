import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('red')
        self.penup()
        self.pensize(1)
        self.speed(0)
        self.got_to_random_pos()

    def got_to_random_pos(self):
        x, y = self.get_random_pos()
        self.goto(x, y)

    def get_random_pos(self):
        x = random.randint(-550, 550)
        y = random.randint(-350, 350)
        return x, y
