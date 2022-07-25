import turtle
import turtle as t
from math import sin, cos
import random as r

t.Screen().bgcolor('black')
# t.Screen().bgpic('hubble2019_01.png')
t.Screen().screensize(1500, 750)
# t.speed(10)
t.tracer(8, 0)
t.colormode(255)
t.hideturtle()


def get_coordinates(planet):
    if planet == 'Mercury':
        return -450, -5
    elif planet == 'Venera':
        return -390, -7
    elif planet == 'Earth':
        return -326, -10
    elif planet == 'Mars':
        return -256, -10
    elif planet == 'Jupyter':
        return -86, -100
    elif planet == 'Saturn':
        return 154, -70
    elif planet == 'Uran':
        return 354, -50
    elif planet == 'Neptune':
        return 554, -40


def stars():
    t.color('white')
    for _ in range(400):
        t.penup()
        t.pensize(r.uniform(0, 0.01))
        t.goto(r.randint(-750, 750), r.randint(-500, 500))
        t.pendown()
        t.dot()
    t.penup()


planets = {
    'Mercury': ('Mercury', 5, 'brown', get_coordinates('Mercury')),
    'Venera': ('Venera', 7, 'orange', get_coordinates('Venera')),
    'Earth': ('Earth', 10, 'blue', get_coordinates('Earth')),
    'Mars': ('Mars', 10, 'red', get_coordinates('Mars')),
    'Jupyter': ('Jupyter', 100, 'brown', get_coordinates('Jupyter')),
    'Saturn': ('Saturn', 70, 'gray', get_coordinates('Saturn')),
    'Uran': ('Uran', 50, 'blue', get_coordinates('Uran')),
    'Neptune': ('Neptune', 40, 'violet', get_coordinates('Neptune'))
}


class Solar:
    def __init__(self):
        self.radius = 500
        self.color = (255, 0, 0)
        self.blot_number = r.randint(1, 50)

    def blot(self):
        t.goto(r.randint(-750, -300), r.randint(-375, 375))
        t.dot(r.randint(1, 4), 'black')

    def draw(self):
        t.goto(-1000, -500)
        t.pencolor(self.color)
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(radius=self.radius)
        t.end_fill()
        for _ in range(self.blot_number):
            self.blot()


class Planet:
    def __init__(self, name, radius, color, coordinates):
        self.name = name
        self.radius = radius
        self.color = color
        self.coordinates = coordinates

    def draw(self):
        t.setheading(0)
        t.goto(self.coordinates)
        t.pendown()
        t.pencolor(self.color)
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(radius=self.radius)
        t.end_fill()
        t.penup()
        t.right(90)
        t.forward(20)
        t.pencolor('white')
        t.write(self.name, align='center', font=('Times New Roman', 10, 'italic'))


class SaturnRing:
    def __init__(self):
        pass

    def draw(self):
        pass


cm = turtle.Turtle()

cm.hideturtle()
# cm.speed(10)


class Comet:
    def __init__(self):
        self.size = 30
        self.color = 'white'
        self.tail_length = 15
        self.tail_color = 'orange'

    def tail(self):
        width = self.size - 10
        length = self.tail_length
        cm.pencolor(self.tail_color)
        cm.penup()
        cm.forward(width/2)
        cm.pendown()
        while width != 0:
            cm.pensize(width)
            cm.forward(length)
            width -= 1

    def draw(self):
        cm.setheading(0)
        cm.dot(self.size, self.color)
        self.tail()


def main():
    stars()
    solar = Solar()
    solar.draw()
    for key, val in planets.items():
        planet = Planet(name=val[0], radius=val[1], color=val[2], coordinates=val[3])
        planet.draw()
    for i in range(1, 1101):
        cm.penup()
        cm.goto(500 - i, 300)
        comet = Comet()
        cm.pendown()
        comet.draw()
        t.tracer(50)
        cm.clear()

    t.mainloop()


if __name__ == '__main__':
    main()

