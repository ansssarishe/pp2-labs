from pygame.examples.go_over_there import delta_time_ove
from settings import *
import pygame as pg
import math


class Camera:
    def __init__(self, game):
        self.game = game
        self.x, self.y = CAMERA_POS
        self.angle = CAMERA_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = CAMERA_SPEED * self.game.delta_time #in case of frame stutters the speed of camera remains unchanged
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        