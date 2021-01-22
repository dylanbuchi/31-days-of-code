from turtle import Turtle


class Display(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(x, y)

    def display_score(self, level):
        self.clear()
        self.write(f'Level: {level}', font=('Consolas', 15, 'normal'))

    def display_game_over(self):
        self.clear()
        self.write(f'Game Over',
                   align='center',
                   font=('Consolas', 20, 'normal'))
