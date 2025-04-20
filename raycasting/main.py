import pygame as pg
import sys
from settings import * 
from camera import *
from map import *


class Game:
    def __init__(self): #initializing everythin
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1

    def new_game(self): #assigns variable objects for new game
        self.map = Map(self) 
        self.camera = Camera(self)

if __name__ == '__main__':
    game = Game()
    game.run()