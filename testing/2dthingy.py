import pygame as pg
import sys
import math


pg.init()

clock = pg.time.Clock()
delta_time = 1

RES = (1920, 1080)
PLAYER_ANG = math.radians(0)
FOV = 90
CAMERA_SPEED = 0.0035


screen = pg.display.set_mode(RES)
screen.fill("white")

class Camera:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def draw(self, screen):
        pg.draw.circle(screen, "cyan", (self.x, self.y), 60)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = CAMERA_SPEED




class RayCast:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, angle):
        x1 = self.x + math.sin(angle) * 200
        y1 = self.y + math.sin(angle) * 200
        pg.draw.line(screen, "black", (self.x, self.y), (x1, y1), 1)


while True:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            



    

    