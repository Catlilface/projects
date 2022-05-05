import pygame as pg
from math import sin, cos, pi

win = pg.display.set_mode((1200,900))

run = True

def drawBranch(x, y, height, angle):
    pg.draw.line(win, (255, 255, 255), (x, y), (x + height*sin(angle), y - height*cos(angle)))
    if height > 1:
        drawBranch(x + height*sin(angle), y - height*cos(angle), height / 1.5, angle + pi / 6)
        drawBranch(x + height*sin(angle), y - height*cos(angle), height / 1.5, angle - pi / 3)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    drawBranch(600, 900, 300, 0)

    pg.time.delay(16)
    pg.display.update()
    win.fill((0,0,0))