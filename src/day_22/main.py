import os
import time
import random
from turtle import Screen

from car import Car
from frog import Frog
from display import Display

#  constants
IMAGES_PATH = os.path.join(os.getcwd(), 'src', 'day_22', 'images')
BACKGROUND = f"{IMAGES_PATH}/bg2.png"
CARS_IMAGE_PATH = f"{IMAGES_PATH}/cars/"
FROG_IMAGE = f"{IMAGES_PATH}/frog3.gif"

LIMIT_UP = 300

# -----------------------------------------------------


def get_cars_images_path():
    """return a list of the paths of every car image"""
    onlyfiles = [
        f"{CARS_IMAGE_PATH}{car_file}"
        for car_file in os.listdir(CARS_IMAGE_PATH)
        if os.path.isfile(os.path.join(CARS_IMAGE_PATH, car_file))
    ]
    return onlyfiles


def create_screen(title='Crossy Road Game',
                  width=600,
                  height=600,
                  color='white',
                  bg_image=BACKGROUND):
    screen = Screen()
    screen.tracer(0)
    screen.bgcolor(color)
    screen.bgpic(bg_image)
    screen.listen()
    screen.setup()
    screen.title(title)

    return screen


def set_screen_car_shapes(screen):
    """set the screen to add custom car images"""
    cars = get_cars_images_path()
    for car in cars:
        screen.addshape(car)


def teleport(car):
    """teleport the car when it goes out of bounds"""
    if car.xcor() >= 600:
        y = car.ycor()
        x = car.xcor()
        car.goto(-x, y)


def change_car_positions(cars):
    range_x_slots = [i for i in range(-280, 300, 80)]
    range_y_slots = [i for i in range(-280, 300, 120)]

    for car in cars:
        x = random.choice(range_x_slots)
        y = random.choice(range_y_slots)
        if range_y_slots:
            range_x_slots.remove(x)

        car.speed += 2
        car.goto(x, y)


def play_game(screen):
    frog = Frog(FROG_IMAGE)

    cars = create_cars()
    cars_2 = create_cars()
    cars.extend(cars_2)

    score = Display(color='white', x=-450, y=350)
    game_over = Display('white', 0, 0)

    while True:
        score.display_score(frog.lvl)

        for car in cars:
            car.forward(car.speed)
            frog.move(screen)
            teleport(car)

            if (frog.frog_passed_lvl(LIMIT_UP)):
                random_car = random.choice(cars)
                random_car.speed += 1

                change_car_positions(cars)
            if car.run_over_frog(frog):
                game_over.display_game_over()
                return

        screen.update()
        time.sleep(0.01)


def create_cars():
    car_paths = get_cars_images_path()
    cars = []

    range_x_slots = [i for i in range(-280, 280, 120)]
    range_y_slots = [i for i in range(-280, 300, 120)]

    for cp in car_paths:
        x = random.choice(range_x_slots)
        y = random.choice(range_y_slots)

        if range_y_slots:
            range_x_slots.remove(x)

        new_car = Car(cp, x, y)

        cars.append(new_car)

    return cars


def main():
    screen = create_screen()
    set_screen_car_shapes(screen)
    screen.addshape(FROG_IMAGE)
    play_game(screen)
    screen.mainloop()


if __name__ == "__main__":
    main()