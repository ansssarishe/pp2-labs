from pygame.examples.go_over_there import delta_time
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
            
        self.check_wall_collision(dx, dy)
        
        if keys[pg.K_LEFT]:
            self.angle -= CAMERA_ANGULAR_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += CAMERA_ANGULAR_SPEED * self.game.delta_time
        self.angle %= math.tau
        
    def check_wall(self, x , y):
        return(x, y) not in self.game.map.world_map
        
    def check_wall_collision(self, dx, dy):
        scale = CAMERA_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
            
    def draw(self):
        #pg.draw.line(self.game.screen, "cyan", (self.x * MINIMAP_SIZE, self.y * MINIMAP_SIZE), (self.x * MINIMAP_SIZE + WIDTH * math.cos(self.angle), self.y * MINIMAP_SIZE + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, "green", (self.x * MINIMAP_SIZE, self.y * MINIMAP_SIZE), 15 * (MINIMAP_SIZE / 45))
            
    def update(self):
        self.movement()
        
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)