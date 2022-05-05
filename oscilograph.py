import pygame as pg
from math import sin, cos, pi

def position(radius, a, b):
    return radius*sin(a*theta) + 450, radius*cos(b*theta) + 450

def drawShape(p):
    pg.draw.lines(win,(255, 255, 255), False, p)

if __name__ == '__main__':
    win = pg.display.set_mode((900,900))

    run = True
    show_render = False
    a = 6
    b = 3
    theta = 0
    points = [position(400, a, b)]

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        points += [position(400, a, b)]
        if show_render:
            drawShape(points)
            pg.display.update()

        theta += .001
        if int(theta / pi) == 2 and not show_render:
            drawShape(points)
            pg.display.update()
            theta = 10
        win.fill((0,0,0))