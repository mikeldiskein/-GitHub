import turtle as t
from random import choice, randrange
import time
from math import tan, radians, sqrt

SQUARE = 43.301270189221945  # float-type

horizon_figure_number = 5
vertical_figure_number = 5
t.Screen().screensize(500, 500)


def side_calculate(side_number):  # side length calculating
    a = 4 * tan((radians(180)) / side_number)
    b = SQUARE * a
    x_square = b / 3
    return sqrt(x_square)


def angle_calculate(side_number):  # calculating an angle between figure sides
    return 180 * (side_number - 2) / side_number


def coordinates_list_calculate(horizon, vert):
    y_between = 500 / vert
    x_between = 500 / horizon
    main_coordinates = []
    for y in range(-250, 251, y_between):
        for x in range(-250, 251, x_between):
            main_coordinates.append((x, y))
    return main_coordinates


def coordinates_for_concrete_figure():
    coordinates = coordinates_list_calculate(horizon_figure_number, vertical_figure_number)
    figure_coord = choice(coordinates)
    del coordinates[coordinates.index(figure_coord)]
    return figure_coord


class Triangle:
    def __init__(self):
        self.side_number = 3
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.left(60)
        t.begin_fill()
        for _ in range(3):
            t.forward(self.side)
            t.right(self.angle)
        t.end_fill()


class Square:
    def __init__(self):
        self.side_number = 4
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(4):
            t.forward(self.side)
            t.left(self.angle)
        t.end_fill()


class Pentagon:
    def __init__(self):
        self.side_number = 5
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(5):
            t.forward(self.side)
            t.left(self.angle)
        t.end_fill()


class Hexagon:
    def __init__(self):
        self.side_number = 6
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(6):
            t.forward(self.side)
            t.left(self.angle)
        t.end_fill()


class Heptagon:
    def __init__(self):
        self.side_number = 7
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(7):
            t.forward(self.side)
            t.left(self.angle)
        t.end_fill()


class Octagon:
    def __init__(self):
        self.side_number = 8
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(8):
            t.forward(self.side)
            t.left(self.angle)
        t.end_fill()


draws = [Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon]


def time_track(func):
    begin = time.time()
    func(draws)
    end = time.time()
    print(end - begin)


@time_track
def run(lst):
    for _ in range(horizon_figure_number * vertical_figure_number):
        t.colormode(255)
        t.tracer(2)
        t.speed(5)
        t.Screen().bgcolor('white')
        color = randrange(256), randrange(256), randrange(256)
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        t.goto(coordinates_for_concrete_figure())
        figure = choice(lst)
        figure.draw(self=figure)















