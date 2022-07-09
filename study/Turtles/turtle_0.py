import turtle as t
from random import randrange, choice

t.Screen().colormode(255)
t.Screen().screensize(500, 500)
t.Screen().bgcolor('white')
t.tracer(2)
t.speed(5)


class Star:
    def __init__(self):
        self.side = randrange(10, 41)
        self.color_set = randrange(256), randrange(256), randrange(256)
        self.x = randrange(-500, 500)
        self.y = randrange(-500, 500)

    def draw(self):
        color = self.color_set
        t.pencolor(color)
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.left(36)
        for _ in range(5):
            t.forward(self.side)
            t.right(144)
        t.end_fill()


for _ in range(500):
    Star().draw()


t.mainloop()
