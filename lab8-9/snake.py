# imports
import pygame, sys, random, time
from pygame.locals import *

# initializing pygame
pygame.init()

# fps setup
FPS = 10  # starting speed of the snake
FramePerSec = pygame.time.Clock()

# colors for the game
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
CELL_SIZE = 50  # size of each cell in the grid

# fonts for text
font = pygame.font.SysFont("Verdana", 20)
start_text = pygame.font.SysFont("Verdana", 40).render("Press any key to start", True, WHITE)
game_over = pygame.font.SysFont("Verdana", 60).render("Game Over", True, RED)

# creating the game screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# snake setup
snake_pos = [[100, 50], [80, 50], [60, 50]]  # starting position of the snake
snake_direction = "RIGHT"  # initial direction of movement

# food setup
food_types = [
    {"color": RED, "weight": 1, "timer": 5000},  # red food: 1 point, disappears after 5 seconds
    {"color": YELLOW, "weight": 3, "timer": 7000},  # yellow food: 3 points, disappears after 7 seconds
    {"color": PURPLE, "weight": 5, "timer": 10000},  # purple food: 5 points, disappears after 10 seconds
]
current_food = None  # the current food on the screen
food_spawn_time = None  # when the current food was spawned

# score and level tracking
SCORE = 0
LEVEL = 1
FOOD_TO_LEVEL_UP = 4  # how many foods to eat before leveling up

# function to generate a random position for food
def generate_food():
    # get all possible positions on the grid
    all_positions = {(x, y) for x in range(0, SCREEN_WIDTH, CELL_SIZE)
                     for y in range(0, SCREEN_HEIGHT, CELL_SIZE)}
    # remove positions occupied by the snake
    snake_positions = {tuple(pos) for pos in snake_pos}
    available_positions = list(all_positions - snake_positions)

    # if no positions are available, return None (game over condition)
    if not available_positions:
        return None

    # pick a random position from the available ones
    return random.choice(available_positions)

# function to spawn a new food
def spawn_food():
    global current_food, food_spawn_time
    food_pos = generate_food()  # get a random position for the food
    if food_pos is None:
        return None
    food_type = random.choice(food_types)  # pick a random food type
    current_food = {"pos": food_pos, "type": food_type}  # store the food's position and type
    food_spawn_time = pygame.time.get_ticks()  # record the time it was spawned
    return current_food

# function to show the start screen
def show_start_screen():
    DISPLAYSURF.fill(BLACK)  # fill the screen with black
    text_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # center the text
    DISPLAYSURF.blit(start_text, text_rect)  # display the start text
    pygame.display.update()

    # wait for the player to press any key
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                return  # exit the function when any key is pressed

# show the start screen
show_start_screen()

# spawn the first food
spawn_food()

# game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # handle controls
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP] and snake_direction != "DOWN":  # prevent reversing direction
        snake_direction = "UP"
    if pressed_keys[K_DOWN] and snake_direction != "UP":
        snake_direction = "DOWN"
    if pressed_keys[K_LEFT] and snake_direction != "RIGHT":
        snake_direction = "LEFT"
    if pressed_keys[K_RIGHT] and snake_direction != "LEFT":
        snake_direction = "RIGHT"

    # move the snake
    if snake_direction == "UP":
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - CELL_SIZE])
    if snake_direction == "DOWN":
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + CELL_SIZE])
    if snake_direction == "LEFT":
        snake_pos.insert(0, [snake_pos[0][0] - CELL_SIZE, snake_pos[0][1]])
    if snake_direction == "RIGHT":
        snake_pos.insert(0, [snake_pos[0][0] + CELL_SIZE, snake_pos[0][1]])

    # check if the snake eats the food
    if current_food and tuple(snake_pos[0]) == tuple(current_food["pos"]):
        SCORE += current_food["type"]["weight"]  # add the food's weight to the score
        current_food = None  # remove the food
        if SCORE % FOOD_TO_LEVEL_UP == 0:  # level up after eating enough food
            LEVEL += 1
            FPS += 2  # increase the speed
        spawn_food()  # spawn a new food
    else:
        snake_pos.pop()  # remove the tail if no food is eaten

    # check if the food timer has expired
    if current_food and pygame.time.get_ticks() - food_spawn_time > current_food["type"]["timer"]:
        current_food = None  # remove the food
        spawn_food()  # spawn a new food

    # check for collisions with walls
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= SCREEN_WIDTH or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= SCREEN_HEIGHT):
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (50, 150))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # check for collisions with itself
    if snake_pos[0] in snake_pos[1:]:
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (50, 150))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # draw everything
    DISPLAYSURF.fill(BLACK)  # clear the screen
    for pos in snake_pos:
        pygame.draw.rect(DISPLAYSURF, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))  # draw the snake
    if current_food:
        pygame.draw.rect(DISPLAYSURF, current_food["type"]["color"],
                         pygame.Rect(current_food["pos"][0], current_food["pos"][1], CELL_SIZE, CELL_SIZE))  # draw the food

    # display score and level
    score_text = font.render(f"Score: {SCORE}", True, WHITE)
    level_text = font.render(f"Level: {LEVEL}", True, WHITE)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(level_text, (SCREEN_WIDTH - 100, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)