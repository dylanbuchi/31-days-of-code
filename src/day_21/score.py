from turtle import Turtle


class Score(Turtle):
    def __init__(self, color='white'):
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write_score(self.left_score)
        self.goto(100, 200)
        self.write_score(self.right_score)

    def write_score(self, score):
        self.write(score, align='center', font=('Roboto', 20, 'normal'))
