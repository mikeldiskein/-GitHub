import turtle as t
from random import randint, choice
import time
from math import tan, radians, sqrt

SQUARE = 43.301270189221945  # float-type

horizon_figure_number = int(input())
vertical_figure_number = int(input())
t.Screen().screensize(500, 500)


def side_calculate(side_number):  # side length calculating
    a = 4 * tan((radians(180)) / side_number)
    b = float(input()) * a
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
            t.right(60)
        t.end_fill()


class Square:
    def __init__(self):
        self.side_number = 4
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(3):
            t.forward(self.side)
            t.right(60)
        t.end_fill()









