#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#initiyaliziruem
pygame.init()
 
#fps
FPS = 60
FramePerSec = pygame.time.Clock()
 
#store colors for the future
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#other variables we will need later
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  # Coin counter
COIN_THRESHOLD = 10  #interval for speed up after coin pickup

#fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
#creating white screen, where everything will be placed
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 #class for enemy cars
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)   #random spawn
 
      def move(self):
        global SCORE #global variable that used in few classes in future
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600): #if car leaves the screen and succesfully dodged
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0: #for the player to be inside screen and move
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite): #class for coins
    def __init__(self):
        super().__init__()
        # Randomly decide if the coin is small or big
        if random.choice([True, False]):  # 50% chance for small or big coin
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (20, 20))  # small coin
            self.weight = 1  # small coin gives 1 coin
        else:
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (35, 35))  # big coin
            self.weight = 5  # big coin gives 5 coins

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

    def move(self): #coins move same as cars
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
                   
#sprites       
P1 = Player()
E1 = Enemy()
 
#sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#sprite group for coins
coins = pygame.sprite.Group()
C1 = Coin()
coins.add(C1)
all_sprites.add(C1)

coll = 0
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1500)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #checking if thershold(enough coins) passed to increase speed
    if COINS >= COIN_THRESHOLD:
        SPEED += 0.5  # increase the speed of the enemy
        COIN_THRESHOLD += 10  # updating threshold
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_collected = font_small.render(f"Coins: {COINS}", True, BLACK)
    collisions = font_small.render(f"Collisions: {coll}", True, BLACK) #sdfsdfsdf
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coins_collected, (SCREEN_WIDTH - 120, 10))
    DISPLAYSURF.blit(collisions, (100, 10))
 
    #moving and redrawing
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # collisions
    if pygame.sprite.spritecollideany(P1, coins):
        for coin in coins:
            if pygame.sprite.collide_rect(P1, coin):  #checking if coin is collected
                COINS += coin.weight  # coin counter +
                coin.kill()  # self explanotary
                break  
        # creating new coin
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
 
    #checks if player died
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          coll += 1

          #time.sleep(0.5)
                    
          #DISPLAYSURF.fill(RED)
          #DISPLAYSURF.blit(game_over, (30,250))
          
          for enemy in enemies:
              enemy.kill()
          E1 = Enemy()
          enemies = pygame.sprite.Group()
          enemies.add(E1)
          all_sprites.add(E1)
          #time.sleep(2)
          #pygame.quit()
          #sys.exit()     #gg   
         
    pygame.display.update()
    FramePerSec.tick(FPS)