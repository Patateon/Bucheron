import pygame
import numpy as np
from game import *
from agent import *
from grille import *
import state as STATE

# Constants
SCREEN_WIDTH =800
SCREEN_HEIGHT = 600
BLOCKX = 8
BLOCKY = 6

def create_level(screen, grid,sizeBlock):
    for x in range(BLOCKX):
            for y in range(BLOCKY):
                cell=grid.getCell((y,x))
                if cell == STATE.vide:
                    rectangle=pygame.rect.Rect(sizeBlock*x,sizeBlock*y,sizeBlock,sizeBlock)
                    pygame.draw.rect(screen,(0,255,0),rectangle)

if __name__ == "__main__":
    pygame.init()
    # RNGESUS
    #rng = np.random.default_rng()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Forest-Farming")
    sizeBlock=min(SCREEN_HEIGHT//BLOCKY,SCREEN_WIDTH//BLOCKX)
    #game=Game(nbblock_y,nbblock_x,0.8,2,[[2,2],[17,4]])
    #game.initGame()
    grid = Grille(BLOCKX, BLOCKY) #A remplacer par avec la creation du jeux
    running = True
    delay = 16
    tick = 0
    surface=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                if event.type == pygame.KEYDOWN:
                    pass
        start = pygame.time.get_ticks()
        tick += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        create_level(screen,grid,sizeBlock)
        timeTaken = pygame.time.get_ticks()-start
        actualDelay = delay - timeTaken
        pygame.time.delay(actualDelay)
        pygame.display.update()
    pygame.quit()
