import pygame as pg
import sys
import math
import random

pg.init()

# Constants
framespersec = pg.time.Clock()
fps = 30

CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


RESOLUTION = (1000, 1000)
CENTER = (RESOLUTION[0] / 2, RESOLUTION[1] / 4 + 50)  # Pivot point higher on the screen

SCREEN = pg.display.set_mode(RESOLUTION)
SCREEN.fill(BLACK)
pg.display.set_caption("Simple Pendulum")

# Pendulum parameters
l1 = 200  # Length of the pendulum arm in pixels
l2 = 100
m1 = 20   # Mass of the pendulum bob (used for drawing)
m2 = 15
gravity = 4  # Gravitational acceleration

# Initial conditions
angle1 = random.random() * math.pi  # Initial angle (45 degrees in radians)
angle2 = random.random() * math.pi
angular_velocity1 = 0  # Initial angular velocity
angular_velocity2 = 0
angular_acceleration1 = 0  # Initial angular acceleration
angular_acceleration2 = 0

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pg.draw.circle(screen, CYAN, (int(self.x), int(self.y)), self.radius)

def main():
    global angle1, angular_velocity1, angular_acceleration1, angle2, angular_acceleration2, angular_velocity2

    # Create a transparent surface for the trail
    trail_surface = pg.Surface(RESOLUTION, pg.SRCALPHA)
    trail_surface.fill((0, 0, 0, 0))  # Fully transparent

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        # Physics calculations for the double pendulum
        num1 = -gravity * (2 * m1 + m2) * math.sin(angle1)
        num2 = -m2 * gravity * math.sin(angle1 - 2 * angle2)
        num3 = -2 * math.sin(angle1 - angle2) * m2
        num4 = angular_velocity2**2 * l2 + angular_velocity1**2 * l1 * math.cos(angle1 - angle2)
        den1 = l1 * (2 * m1 + m2 - m2 * math.cos(2 * angle1 - 2 * angle2))
        angular_acceleration1 = (num1 + num2 + num3 * num4) / den1

        num1 = 2 * math.sin(angle1 - angle2)
        num2 = (angular_velocity1**2 * l1 * (m1 + m2))
        num3 = gravity * (m1 + m2) * math.cos(angle1)
        num4 = angular_velocity2**2 * l2 * m2 * math.cos(angle1 - angle2)
        den2 = l2 * (2 * m1 + m2 - m2 * math.cos(2 * angle1 - 2 * angle2))
        angular_acceleration2 = (num1 * (num2 + num3 + num4)) / den2

        # Update angular velocities and angles
        angular_velocity1 += angular_acceleration1
        angular_velocity2 += angular_acceleration2
        angle1 += angular_velocity1
        angle2 += angular_velocity2

        # Apply damping
        angular_velocity1 *= 1
        angular_velocity2 *= 1

        # Calculate the position of the pendulum bobs
        x1 = CENTER[0] + l1 * math.sin(angle1)
        y1 = CENTER[1] + l1 * math.cos(angle1)
        x2 = CENTER[0] + l1 * math.sin(angle1) + l2 * math.sin(angle2)
        y2 = CENTER[1] + l1 * math.cos(angle1) + l2 * math.cos(angle2)

        # Draw everything
        SCREEN.fill(BLACK)

        # Fade the trail by reducing its alpha value
        trail_surface.fill((0, 0, 0, 5), special_flags=pg.BLEND_RGBA_SUB)

        # Add the current position of ball2 to the trail
        pg.draw.circle(trail_surface, CYAN, (int(x2), int(y2)), 2)

        # Blit the trail surface onto the main screen
        SCREEN.blit(trail_surface, (0, 0))

        # Draw pendulum arms and balls
        pg.draw.line(SCREEN, WHITE, CENTER, (x1, y1), 3)  # First pendulum arm
        pg.draw.circle(SCREEN, WHITE, CENTER, 5)  # Pivot point
        ball1 = Ball(x1, y1, m1)
        ball1.draw(SCREEN)

        pg.draw.line(SCREEN, WHITE, (x1, y1), (x2, y2), 3)  # Second pendulum arm
        ball2 = Ball(x2, y2, m2)
        ball2.draw(SCREEN)

        pg.display.flip()
        framespersec.tick(fps)

main()

