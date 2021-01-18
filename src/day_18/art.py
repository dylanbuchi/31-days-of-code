import random
import colorgram

from turtle import Turtle, Screen


def create_pen(shape, color, speed):
    pen = Turtle()
    pen.shape(shape)
    pen.color(color)
    pen.speed(speed)

    return pen


def get_colors_from_image(image_path, n_colors):
    colors_list = []

    for color_object in colorgram.extract(image_path, n_colors):
        r, g, b = color_object.rgb
        colors_list.append((r, g, b))
    return colors_list


def get_random_unique_color(colors):
    color = random.choice(colors)
    return color


def draw_art(pen):
    image_path = 'src/day_18/images/dots.jpg'
    n_colors = 35
    colors = get_colors_from_image(image_path, n_colors)
    n = 10
    x = -280
    y = -200

    move_pen(pen, x, y)

    while n:
        for _ in range(10):
            color = get_random_unique_color(colors)
            print(color)
            pen.color(color)

            move_forward(pen, 50)
            pen.dot(20)
        y += 50
        move_pen(pen, x, y)
        n -= 1


def move_forward(pen, distance):
    pen.penup()
    pen.forward(distance)
    pen.pendown()


def move_pen(pen, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def main():
    app = Screen()
    app.colormode(255)

    pen = create_pen('classic', 'black', 'fast')
    pen.hideturtle()

    draw_art(pen)

    app.mainloop()


if __name__ == "__main__":
    main()