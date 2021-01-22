from turtle import Turtle


class Car(Turtle):
    def __init__(self, shape, x, y):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.goto(x, y)
        self.speed = 4

    def run_over_frog(self, frog: Turtle):
        if self.distance(frog) < 48:
            return True
        return False
