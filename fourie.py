import pygame as pg
from math import sin, cos, pi

win = pg.display.set_mode((900,900))

run = True

n = 1
theta = 0
points = list()
m = 2

def drawShape(p):
    pg.draw.aalines(win,(255, 255, 255), False, p)

def cycle(number_of_cycles, radius, x, y, angle):
    posx = radius*sin(angle) + x
    posy = radius*cos(angle) + y
    if number_of_cycles > 1:
        pg.draw.circle(win, (50, 50, 50), (int(x), int(y)), int(radius), True)
        pg.draw.circle(win, (255, 255, 255), (int(posx), int(posy)), 4)
        return cycle(number_of_cycles - 1, radius, posx, posy, angle)
    else:
        pg.draw.circle(win, (50, 50, 50), (int(x), int(y)), int(radius), True)
        pg.draw.circle(win, (255, 255, 255), (int(posx), int(posy)), 4)
        return posx, posy

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    points += [cycle(m, 200, 450, 450, theta)]
    if len(points) > 2:
        drawShape(points)

    theta += .01
    if int(theta / pi) == 2:
        theta = 0
        m += 1
        points = list()
    pg.time.delay(16)
    pg.display.update()
    win.fill((0,0,0))