import pygame as pg
import sys
import math


pg.init()

global dx, dy
dx = 5
dy = 5

framespersec = pg.time.Clock()
FPS = 30

RESOLUTION = (800, 800)

screen = pg.display.set_mode(RESOLUTION)
screen.fill("black")

waves = list()
particles = list()

class Object:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pg.draw.circle(screen, "white", (self.x, self.y), self.radius)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    

    def doppling(self, particles): 
        for angle in range(0, 361):
            radians = math.radians(angle)

            dx = math.cos(radians) * 5
            dy = math.sin(radians) * 5

            particle = Particle(self.x, self.y, dx, dy)
            particles.append(particle)
    
    def collision(self):
        global dx, dy
        if self.x >= 800 or self.x <= 0:
            dx *= -1
        if self.y >= 800 or self.y <= 0:
            dy *= -1

class Particle:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pg.draw.circle(screen, "cyan", (self.x, self.y), 2)

    def collision(self):
        if self.x >= 800 or self.x <= 0:
            self.dx *= -1
        if self.y >= 800 or self.y <= 0:
            self.dy *= -1


ball = Object(10, 400, 20)
count = 0



while True:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    ball.collision()
    screen.fill("black")
    ball.draw(screen)
    ball.move(dx, dy)  

    count += 5
    if count == 150:
        ball.doppling(particles)
        count -= 150

    for particle in particles:
        particle.update()
        particle.collision()
        particle.draw(screen)
    


    pg.display.flip()
    framespersec.tick(FPS)