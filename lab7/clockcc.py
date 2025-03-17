import pygame
import sys
import math
from datetime import datetime

pygame.init()

background = pygame.image.load('clock.png')
sec_hand = pygame.image.load('sec_hand.png')
min_hand = pygame.image.load('min_hand.png')

width, height = background.get_size()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Clock')

def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.now()
    seconds = now.second
    minutes = now.minute

    sec_angle = -seconds * 6
    min_angle = -minutes * 6

    screen.blit(background, (0, 0))

    blit_rotate_center(screen, sec_hand, (width//2, height//2), sec_angle)
    blit_rotate_center(screen, min_hand, (width//2, height//2), min_angle)

    pygame.display.flip()

    pygame.time.Clock().tick(60)