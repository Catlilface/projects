import random
import pygame as pg

pg.init()
win = pg.display.set_mode((900,900))

run = True

def draw_circle(x, y, r):
    pg.draw.circle(win, (255, 255, 255), (x, y), r, True)
    if r > 2:
        draw_circle(x + r // 2, y, r // 2)
        draw_circle(x - r // 2, y, r // 2)

m = 0
d = 0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    d += 10
    m -= 10

    draw_circle(450 + m, 450, 450 + d)

    if d == 450:
        m = 0
        d = 0


    pg.time.delay(10)
    pg.display.update()
    win.fill((0, 0, 0))
