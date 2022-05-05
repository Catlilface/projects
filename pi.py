import random
import pygame as pg

win = pg.display.set_mode((900,900))

run = True

overall = 0
inside = 0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    dot = (random.random()*2, random.random()*2)
    if (dot[0]-1)**2 + (dot[1]-1)**2 <= 1:
        inside += 1
        pg.draw.circle(win, (0, 255, 0), (int(dot[0]*450), int(dot[1]*450)), 2)
    else:
        pg.draw.circle(win, (255, 0, 0), (int(dot[0]*450), int(dot[1]*450)), 2)

    overall += 1

    if inside:
        pi_eval = inside / overall * 4

    pg.draw.circle(win, (255, 255, 255), (450, 450), 450, 10)

    if overall % 100 == 0:
        pg.display.update()
        print(f'Pi ~= {pi_eval}')