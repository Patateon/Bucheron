import pygame
import numpy as np
from game import *
from agent import *
from state import *
from astar import *
import sys

# Constants
GAME_WIDTH =800
GAME_HEIGHT = 600
DISPLAY_HEIGHT = 100
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
DEBUG_CLR = (0, 0, 255) # Utile pour debug les chemins

# Les delais
POUSSE = 5
MATURATION = 30

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
                case 6:
                    pygame.draw.rect(screen, DEBUG_CLR, rectangle)



if __name__ == "__main__":
    
    pygame.init()
    
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT+DISPLAY_HEIGHT))
    pygame.display.set_caption("Forest-Farming")
    sizeBlock=min(GAME_HEIGHT//BLOCKY,GAME_WIDTH//BLOCKX)
    game=Game(BLOCKX, BLOCKY, 2, 4)
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
    interface_surface = pygame.Surface((GAME_WIDTH,DISPLAY_HEIGHT))
    game_surface = pygame.Surface((GAME_WIDTH,GAME_HEIGHT))
    font = pygame.font.SysFont('DejaVuSerif-Bold.ttf',40)
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

        # Pousse arbre
        if (tick % POUSSE == 0):
            game.growArbres()
        # Pousse fruits
        if (tick % MATURATION == 0):
            game.growFruits()

        # Update arbre
        game.updateArbre()
        # Update de la grille
        interface_surface.fill((255,255,255))
        interface_surface.blit(font.render(f'Temps : {pygame.time.get_ticks()//1000}s', True, (0,0,0)),(10,10))
        interface_surface.blit(font.render(f'Score : {game.score.getScore()}pts', True, (0,0,0)),(GAME_WIDTH//2,10))
        screen.blit(interface_surface,(0,0))
        create_level(game_surface,grid,sizeBlock)
        screen.blit(game_surface,(0,DISPLAY_HEIGHT))

        # Calcul du delai
        timeTaken = pygame.time.get_ticks()-start
        actualDelay = delay - timeTaken
        pygame.time.delay(actualDelay)

        pygame.display.update()
        print("tick")
        game.update()

    pygame.quit()
