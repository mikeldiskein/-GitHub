import turtle as t
from random import choice, randrange
import time
from math import tan, radians, sqrt

SQUARE = 1000

horizon_figure_number = 5
vertical_figure_number = 5
t.Screen().screensize(600, 600)

y_between = 500 / vertical_figure_number
x_between = 500 / horizon_figure_number
main_coordinates = []
for y in range(-250, 251, int(y_between)):
    for x in range(-250, 251, int(x_between)):
        main_coordinates.append((x, y))


def side_calculate(side_number):  # side length calculating
    return (SQUARE * 4 * tan(radians(180 / side_number)) / side_number) ** 0.5


def angle_calculate(side_number):  # calculating an angle between figure sides
    return 180 * (side_number - 2) / side_number


def coordinates_for_concrete_figure():
    figure_coord = choice(main_coordinates)
    main_coordinates.remove(figure_coord)
    return figure_coord


class Triangle:
    def __init__(self):
        self.side_number = 3
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(3):
            t.forward(self.side)
            t.left(180 - self.angle)
        t.end_fill()
        t.setheading(0)


class Square:
    def __init__(self):
        self.side_number = 4
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(4):
            t.forward(self.side)
            t.left(180 - self.angle)
        t.end_fill()
        t.setheading(0)


class Pentagon:
    def __init__(self):
        self.side_number = 5
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(5):
            t.forward(self.side)
            t.left(180 - self.angle)
        t.end_fill()
        t.setheading(0)


class Hexagon:
    def __init__(self):
        self.side_number = 6
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(6):
            t.forward(self.side)
            t.left(180 - self.angle)
        t.end_fill()
        t.setheading(0)


class Heptagon:
    def __init__(self):
        self.side_number = 7
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(7):
            t.forward(self.side)
            t.left(180 - self.angle)
        t.end_fill()
        t.setheading(0)


class Octagon:
    def __init__(self):
        self.side_number = 8
        self.side = side_calculate(self.side_number)
        self.angle = angle_calculate(self.side_number)

    def draw(self):
        t.begin_fill()
        for _ in range(8):
            t.forward(self.side)
            t.left(180 - self.angle)
        t.end_fill()
        t.setheading(0)


draws = [Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon]


def time_track(func):
    begin = time.time()
    func(draws)
    end = time.time()
    print(f'Программа выполнялась {end - begin - 5.0} секунд (без учёта преднамеренной задержки)')


@time_track
def run(lst):
    for _ in range(len(main_coordinates)):
        t.colormode(255)
        t.tracer(2)
        t.speed(5)
        t.Screen().bgcolor('white')
        color = randrange(256), randrange(256), randrange(256)
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        t.goto(coordinates_for_concrete_figure())
        t.pendown()
        figure = choice(lst)
        figure.__init__(figure)
        figure.draw(figure)
    time.sleep(5.0)
















