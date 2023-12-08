import pygame
import numpy as np
from game import *
from agent import *
from state import *
from astar import *
from cueilleur import *
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
HARVEST_CLR = (0, 0, 0)#NOIR
DEBUG_CLR = (0, 0, 255) # Utile pour debug les chemins

# Les delais
POUSSE = 5
MATURATION = 30

# Dessine la grille
def create_level(screen, grid, sizeBlock):
    sprite_size = (2*(sizeBlock - 2*SPACING), 2*(sizeBlock - 2*SPACING))
    low_image = pygame.image.load("sprite/low_tree.png")
    low_image = pygame.transform.scale(low_image,sprite_size)
    mid_image = pygame.image.load("sprite/mid_tree.png")
    mid_image = pygame.transform.scale(mid_image,sprite_size)
    big_image = pygame.image.load("sprite/big_tree.png")
    big_image = pygame.transform.scale(big_image,sprite_size)
    fruit_image = pygame.image.load("sprite/fruit_tree.png")
    fruit_image = pygame.transform.scale(fruit_image,sprite_size)
    lumber_image = pygame.image.load("sprite/lumberjack.png")
    lumber_image = pygame.transform.scale(lumber_image,sprite_size)
    harvester_image = pygame.image.load("sprite/harvester.png")
    harvester_image = pygame.transform.scale(harvester_image,sprite_size)
    screen.fill((0,0,0))
    for x in range(BLOCKX):
        for y in range(BLOCKY):
            cell=grid.getCell((y,x))
            rectangle=pygame.rect.Rect(sizeBlock*x + SPACING, sizeBlock*y + SPACING, sizeBlock - 2*SPACING, sizeBlock - 2*SPACING) # Spacing de 1 provisoire pour les tests
            position = (sizeBlock*x + SPACING/2-sizeBlock/2, sizeBlock*y + SPACING/2-sizeBlock)
            pygame.draw.rect(screen, EMPTY_CLR, rectangle)
            match cell:
                case State.lowTree:
                    screen.blit(low_image, position)
                case State.midTree:
                    screen.blit(mid_image, position)
                case State.highTree:
                    screen.blit(big_image, position)
                case State.fruitTree:
                    screen.blit(fruit_image, position)
                case State.lumber:
                    screen.blit(lumber_image, position)
                case State.harvest:
                    screen.blit(harvester_image, position)
                case 7:
                    pygame.draw.rect(screen, DEBUG_CLR, rectangle)
            



if __name__ == "__main__":
    
    pygame.init()
    
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT+DISPLAY_HEIGHT))
    pygame.display.set_caption("Forest-Farming")
    sizeBlock=min(GAME_HEIGHT//BLOCKY,GAME_WIDTH//BLOCKX)
    game=Game(BLOCKX, BLOCKY, 2, 2, 4, 10, 3)
    #print("POS AGENTS:")
    #for agent in game.agents:
        #print(agent.pos)
    #print("-----------------------")
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
