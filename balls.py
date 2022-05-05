import pygame as pg
import random

def draw_shape(polypoles, t):
    for i in range(1200 // t):
        for j in range(700 // t):
            potential = 0
            for monopole in polypoles:
                if monopole.x == i * t and monopole.y == j * t:
                    continue
                potential += monopole.radius / ((monopole.x - i * t)**2 + (monopole.y - j * t)**2)**.5
            if 1 < potential < 1.1:
                pg.draw.rect(win, (255, 255, 255), (i * t, j * t, t, t))

def move_ball(monopole):
    if monopole.x + monopole.radius + monopole.direction[0] >= 1200:
        monopole.direction[0] *= -1
    if monopole.y + monopole.radius + monopole.direction[1] >= 700:
        monopole.direction[1] *= -1
    if monopole.x - monopole.radius + monopole.direction[0] <= 0:
        monopole.direction[0] *= -1
    if monopole.y - monopole.radius + monopole.direction[1] <= 0:
        monopole.direction[1] *= -1
    monopole.x += monopole.direction[0]
    monopole.y += monopole.direction[1]
    

class pole:
    def __init__(self, x, y, r, d):
        self.x = x
        self.y = y
        self.radius = r
        self.direction = d

n = 3
dipole = tuple(pole(random.randint(200, 1000), random.randint(200, 500), 5 * random.randint(20, 80) / n, [random.randint(-40, 40), random.randint(-40, 40)]) for i in range(n))

run = True
win = pg.display.set_mode((1200, 700))

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    draw_shape(dipole, 1)
    for i in range(n):
        move_ball(dipole[i])

    pg.time.delay(10)
    pg.display.update()
    win.fill((0, 0, 0))
