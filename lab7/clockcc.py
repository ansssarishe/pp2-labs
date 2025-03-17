import pygame
import sys
from datetime import datetime

pygame.init()

background = pygame.image.load('lab7/images/clock.png')
sec_hand = pygame.image.load('lab7/images/sec_hand.png')
min_hand = pygame.image.load('lab7/images/min_hand.png')

width, height = background.get_size()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Clock')

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.now()
    seconds = now.second + now.microsecond / 1e6
    minutes = now.minute + seconds / 60
    hours = now.hour % 12 + minutes / 60

    sec_angle = -seconds * 6
    min_angle = -minutes * 6
    hour_angle = -hours * 30

    screen.blit(background, (0, 0))

    center_x, center_y = width // 2, height // 2
    rotated_sec_hand, sec_hand_rect = rot_center(sec_hand, sec_angle, center_x, center_y)
    rotated_min_hand, min_hand_rect = rot_center(min_hand, min_angle, center_x, center_y)

    screen.blit(rotated_sec_hand, sec_hand_rect.topleft)
    screen.blit(rotated_min_hand, min_hand_rect.topleft)

    
    current_time = now.strftime("%H:%M:%S")
    pygame.display.set_caption(f"Clock - {current_time}")

    pygame.display.flip()

    pygame.time.Clock().tick(60)