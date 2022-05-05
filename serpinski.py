import random
import pygame as pg

pg.init()
win = pg.display.set_mode((900,900))

run = True

vertices = ((450, 140),
            (797, 740),
            (104, 740))

pg.draw.circle(win, (255, 0, 0), vertices[0], 5)
pg.draw.circle(win, (0, 255, 0), vertices[1], 5)
pg.draw.circle(win, (0, 0, 255), vertices[2], 5)

next_dot = (450, 540)
pg.draw.circle(win, (255, 255, 255), next_dot, 2)
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    vertex_choice = random.choice((0,1,2))
    next_dot = ((next_dot[0] + vertices[vertex_choice][0]) // 2, (next_dot[1] + vertices[vertex_choice][1]) // 2)
    pg.draw.circle(win, ((255, 0, 0),
                         (0, 255, 0),
                         (0, 0, 255))[vertex_choice], next_dot, 2)

    #pg.time.delay(1)
    pg.display.update()

