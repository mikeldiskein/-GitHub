import turtle as t
import time

print('Write number of mp')
screen_size = int(input())
draw_size = screen_size - 100
t.Screen().screensize(screen_size, screen_size)
print('Write side length of the chess board')
board_side_length = int(input())
square_side = draw_size / board_side_length
t.color('black')
t.tracer(1000)
t.speed(10)


class Square:
    def __init__(self):
        self.side = square_side

    def draw(self):
        for _ in range(4):
            t.forward(self.side)
            t.left(90)


def sugar(func):
    begin = time.time()
    func()
    end = time.time()
    print(f'Program was running for {round(end - begin, 2)} seconds')


@sugar
def run():
    counter = 1
    between_square = int(draw_size / board_side_length)
    for y in range(-int(draw_size/2), int(draw_size/2), between_square):
        if counter % 2 != 0:
            flag = False
        else:
            flag = True
        for x in range(-int(draw_size/2), int(draw_size/2), between_square):
            t.penup()
            t.goto(x, y)
            t.pendown()
            if flag:
                t.fillcolor('white')
                flag = False
            else:
                t.fillcolor('black')
                flag = True
            t.begin_fill()
            square = Square()
            square.draw()
            t.end_fill()
        counter += 1


t.mainloop()







