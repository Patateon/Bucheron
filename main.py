import pygame
import numpy as np
from game import *
from agent import *
from state import *
from astar import *
from cueilleur import *
import sys

# Constants
SCREEN_WIDTH =800
SCREEN_HEIGHT = 600
# Dimensions de la grille
BLOCKX = 20
BLOCKY = 15
SPACING = 1

# Colors
EMPTY_CLR = (240, 234, 210)
LOWTREE_CLR = (167, 201, 87)
MIDTREE_CLR = (106, 153, 78)
HIGHTREE_CLR = (56, 102, 65)
FRUITTREE_CLR = (249, 65, 68)
LUMBER_CLR = (160, 2, 160)#VIOLET
HARVEST_CLR = (0, 0, 0)#NOIR
DEBUG_CLR = (0, 0, 255) # Utile pour debug les chemins

# Dessine la grille
def create_level(screen, grid, sizeBlock):
    for x in range(BLOCKX):
        for y in range(BLOCKY):
            cell=grid.getCell((y,x))
            rectangle=pygame.rect.Rect(sizeBlock*x + SPACING, sizeBlock*y + SPACING, sizeBlock - 2*SPACING, sizeBlock - 2*SPACING) # Spacing de 1 provisoire pour les tests
            match cell:
                case State.vide:
                    pygame.draw.rect(screen, EMPTY_CLR, rectangle)
                case State.lowTree:
                    pygame.draw.rect(screen, LOWTREE_CLR, rectangle)
                case State.midTree:
                    pygame.draw.rect(screen, MIDTREE_CLR, rectangle)
                case State.highTree:
                    pygame.draw.rect(screen, HIGHTREE_CLR, rectangle)
                case State.fruitTree:
                    pygame.draw.rect(screen, FRUITTREE_CLR, rectangle)
                case State.lumber:
                    pygame.draw.rect(screen, LUMBER_CLR, rectangle)
                case State.harvest:
                    pygame.draw.rect(screen, HARVEST_CLR, rectangle)
                case 7:
                    pygame.draw.rect(screen, DEBUG_CLR, rectangle)



if __name__ == "__main__":
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Forest-Farming")
    sizeBlock=min(SCREEN_HEIGHT//BLOCKY,SCREEN_WIDTH//BLOCKX)
    game=Game(BLOCKX, BLOCKY, 2, 2, 4)
    print("POS AGENTS:")
    for agent in game.agents:
        print(agent.pos)
    print("-----------------------")
    grid = game.grille #A remplacer par avec la creation du jeux

    '''
    astar = Astar(grid)
    astar.startSearch(np.array([0, 0]), np.array([14, 14]))
    astar.showPath()
    '''

    running = True
    delay = 400
    tick = 0
    #surface=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
    surface=pygame.Surface((BLOCKX * sizeBlock, BLOCKY * sizeBlock))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                pass

        # Gestion du delai
        start = pygame.time.get_ticks()
        tick += 1

        # Update de la grille
        create_level(screen,grid,sizeBlock)

        # Calcul du delai
        timeTaken = pygame.time.get_ticks()-start
        actualDelay = delay - timeTaken
        pygame.time.delay(actualDelay)

        pygame.display.update()
        print("tick")
        game.update()

    pygame.quit()
