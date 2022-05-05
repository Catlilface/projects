import pygame as pg
from math import sin, cos, acos
import random

win = pg.display.set_mode((900,900))

run = True

class Player:
    def __init__(self, x, y, dvx, dvy):
        self.x = x
        self.y = y
        self.R = 10
        self.dvx = dvx
        self.dvy = dvy
        self.buffer = [(int(x), int(y))]*5;

    def render(self):
        for i in range(len(self.buffer)):
            pg.draw.circle(win, (63*i, 63*i, 63*i), self.buffer[i], self.R)

    def physics(self):
        if self.x + self.dvx * dt > 900 or self.x + self.dvx * dt < 0:
            self.dvx *= -1
        if self.y + self.dvy * dt > 900 or self.y + self.dvy * dt < 0:
            self.dvy *= -1


        self.x += self.dvx * dt
        self.y += self.dvy * dt

        self.buffer.append((int(self.x), int(self.y)))
        self.buffer.pop(0)

N = 1092
balls = [Player(900*random.random(), 900*random.random(), 100*random.random(), 100*random.random()) for i in range(N)]
dt = .1

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for ball in balls:
        ball.render()
        ball.physics()

    pg.time.delay(16)
    pg.display.update()