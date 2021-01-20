from tkinter.constants import LEFT
from turtle import Turtle, down
from functools import partial

# Constant Variables
DOWN_VAL = 270
UP_VAL = 90
LEFT_VAL = 180
RIGHT_VAL = 0

KEYS = 'wasd'
PADDING = 23
# -----------------------------------------------------------------------------------


class Snake:
    def __init__(
        self,
        body_color='lime green',
        head_color='green yellow',
        shape='square',
        size=20,
        body_length=3,
    ):
        self.snake_body = []
        self.speed = 0.12
        self._create_snake_body(body_color, head_color, shape, size,
                                body_length)
        self._place_snake_to_starting_position()
        self.snake_head = self.snake_body[0]
        self.count_eaten = 0
        self.score = 0
        self.play_again = False

    def change_snake_head_color(self, color='green yellow'):
        self.snake_head.color(color)

    def change_snake_body_color(self, color='lime green'):
        for body in self.snake_body[1:]:
            body.color(color)

    def _create_snake_body(self, color, head_color, shape, size, body_length):
        for i in range(body_length):
            turtle = self._create_body_part(shape, head_color, size, color, i)
            self.snake_body.append(turtle)

    def _create_body_part(self, shape, head_color, size, color, index=-1):
        turtle = Turtle(shape=shape)
        turtle.color(head_color) if index == 0 else turtle.color(color)
        turtle.pensize(size)
        turtle.speed(0)
        turtle.penup()
        return turtle

    def _place_snake_to_starting_position(self, coords=(0, 0)):
        x, y = coords
        for body in self.snake_body:
            body.goto(x, y)
            x -= PADDING

    def eat(self, food: Turtle):
        if self.snake_head.distance(food) <= 25:
            self.count_eaten += 1
            self.grow()
            self.score += 1
            print('Yummy!')
            return True
        return False

    def grow(self):
        body_part = self.snake_body[-1].clone()
        body_part2 = self.snake_body[-1].clone()
        self.snake_body.extend([body_part, body_part2])

        if self.count_eaten % 2 == 0:
            self.speed -= 0.02
        if self.speed <= 0.02:
            self.speed = 0.02

    def move(self, command, degree=0):
        for i in range(len(self.snake_body) - 1, 0, -1):
            pos = 0
            if (i >= 0):
                pos = self.snake_body[i - 1].pos()
                x, y = pos
                self.snake_body[i].goto(x, y)
        commands = {
            'w': self.snake_head.setheading,  # up
            'a': self.snake_head.setheading,  # left
            's': self.snake_head.setheading,  # down
            'd': self.snake_head.setheading,  # right
        }
        if (command in commands):
            move_function = commands[command]
            if command == 'w':
                if self.snake_head.heading() != DOWN_VAL:
                    move_function(degree)
            elif command == 'a':

                if self.snake_head.heading() != RIGHT_VAL:
                    move_function(degree)
            elif command == 's':
                if self.snake_head.heading() != UP_VAL:
                    move_function(degree)
            elif command == 'd':
                if self.snake_head.heading() != LEFT_VAL:
                    move_function(degree)

        self.snake_head.forward(PADDING)

    def get_player_key(self, app):
        W, A, S, D = KEYS

        app.onkey(partial(self.move, W, UP_VAL), W)
        app.onkey(partial(self.move, A, LEFT_VAL), A)
        app.onkey(partial(self.move, S, DOWN_VAL), S)
        app.onkey(partial(self.move, D, RIGHT_VAL), D)

    def check_player_passed_game_boundaries(self, coords):
        x, y = coords
        if self.snake_head.xcor() >= x or self.snake_head.xcor(
        ) <= -x or self.snake_head.ycor() >= y or self.snake_head.ycor() <= -y:
            return True
        for body in self.snake_body[1:]:
            if self.snake_head.distance(body) <= 20:
                return True
