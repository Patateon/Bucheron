import pygame
import numpy as np
from game import *
from agent import *

pygame.init()

# RNGESUS
rng = np.random.default_rng()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Forest-Farming")

vel=20      #size of the block or speed pac bc he travels by block

nbblock_x=SCREEN_WIDTH//vel     
nbblock_y=SCREEN_HEIGHT//vel

game=Game(nbblock_y,nbblock_x,0.8,2,[[2,2],[17,4]])
game.initGame()

def create_level(game, nbblock_x, nbblock_y):
    for j in range(nbblock_x):
        for i in range(nbblock_y):
            pass 



running = True
delay = 16
tick = 0

while running:

    start = pygame.time.get_ticks()
    tick += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((0,0,0))
   
   
    create_level(game, nbblock_x, nbblock_y, vel)

    timeTaken = pygame.time.get_ticks()-start
    actualDelay = delay - timeTaken
    pygame.time.delay(actualDelay)

    pygame.display.update()


pygame.quit()
