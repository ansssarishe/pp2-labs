import pygame as pg
import sys
from settings import * 
from camera import *
from map import *
from raycasting import *


class Game:
    def __init__(self): #initializing everythin
        pg.init()
        self.screen = pg.display.set_mode(RES, pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        pg.display.set_caption("Raycasting demo mini map")

    def new_game(self): #assigns variable objects for new game
        self.map = Map(self) 
        self.camera = Camera(self)
        self.raycasting = RayCasting(self)
        
    def update(self):
        self.raycasting.update()
        self.camera.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(60)
        
    def draw(self):
        self.screen.fill("black")
        self.map.draw()
        self.camera.draw()
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
                
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()