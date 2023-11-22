import pygame
from game import *
from agent import *
from state import State

# Constants
SCREEN_WIDTH =800
SCREEN_HEIGHT = 600
BLOCKX = 20
BLOCKY = 15
SPACING = 1

# Colors
EMPTY_CLR = (240, 234, 210)
LOWTREE_CLR = (167, 201, 87)
MIDTREE_CLR = (106, 153, 78)
HIGHTREE_CLR = (56, 102, 65)
FRUITTREE_CLR = (249, 65, 68)
LUMBER_CLR = (157, 2, 8)

def create_level(screen, grid, sizeBlock):
    for x in range(BLOCKX):
        for y in range(BLOCKY):
            cell=grid.getCell((y,x))
            rectangle=pygame.rect.Rect(sizeBlock*x + SPACING, sizeBlock*y + SPACING, sizeBlock - 2*SPACING, sizeBlock - 2*SPACING) # Spacing de 1 provisoire pour les tests
            if (cell == State.vide):
                pygame.draw.rect(screen, EMPTY_CLR, rectangle)
            elif (cell == State.lowTree):
                pygame.draw.rect(screen, LOWTREE_CLR, rectangle)
            elif (cell == State.midTree):
                pygame.draw.rect(screen, MIDTREE_CLR, rectangle)
            elif (cell == State.highTree):
                pygame.draw.rect(screen, HIGHTREE_CLR, rectangle)
            elif (cell == State.fruitTree):
                pygame.draw.rect(screen, FRUITTREE_CLR, rectangle)
            elif (cell == State.lumber):
                pygame.draw.rect(screen, LUMBER_CLR, rectangle)



if __name__ == "__main__":
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Forest-Farming")
    sizeBlock=min(SCREEN_HEIGHT//BLOCKY,SCREEN_WIDTH//BLOCKX)
    game=Game(BLOCKX, BLOCKY, 3, 3)
    #game.initGame()
    grid = game.grille #A remplacer par avec la creation du jeux

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

    pygame.quit()
