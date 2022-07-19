import turtle as t
from math import sin, cos
import random as r

t.Screen().bgcolor('black')
# t.Screen().bgpic('hubble2019_01.png')
t.Screen().screensize(1500, 750)
t.speed(10)
t.tracer(2)


def stars():
    t.color('yellow')
    for _ in range(400):
        t.penup()
        t.pensize(r.uniform(0, 0.01))
        t.goto(r.randint(-750, 750), r.randint(-500, 500))
        t.pendown()
        t.dot()


def get_coordinates(planet):
    pass


planets = {
    'Mercury': (5, 'brown', get_coordinates('Mercury')),
    'Venera': (7, 'orange', get_coordinates('Venera')),
    'Earth': (10, 'blue', get_coordinates('Earth')),
    'Mars': (10, 'red', get_coordinates('Mars')),
    'Jupyter': (100, 'brown', get_coordinates('Jupyter')),
    'Saturn': (70, 'gray', get_coordinates('Saturn')),
    'Uran': (50, 'blue', get_coordinates('Uran')),
    'Neptune': (40, 'violet', get_coordinates('Neptune'))
}


class Solar:
    def __init__(self):
        pass


class Planet:
    def __init__(self, name, radius, color, coordinates):
        self.radius = radius
        self.color = color
        self.name = name
        self.coordinates = coordinates

    def draw(self):
        t.circle(radius=self.radius)


class SaturnRing:
    def __init__(self):
        pass

    def draw(self):
        pass


stars()
t.mainloop()

