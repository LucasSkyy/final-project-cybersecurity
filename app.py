import pygame, sys
from pygame.locals import QUIT



def gotoPage2(screen, background):
    
    background.fill((0, 0, 0))
    chess = pygame.image.load("chess.jpg")
    newChess = pygame.transform.scale(chess, (200,200))
    newChess = newChess.convert()
    
    # Rect(left, top, width, height) and pygame.draw.rect(surface, color, rect, width)
    pygame.draw.rect(background, (255, 0, 0), [400, 0, 100, 100], 0)
    pygame.draw.rect(background, (255, 255, 0), [600, 400, 60, 80], 4)
    screen.blit(background, (0, 0))
    screen.blit(newChess, (0,0))
   
   

def gotoPage1(screen, background):
    
    background.fill((255, 255, 255))
    disImage = pygame.image.load("disney.jpg")
    disImage = disImage.convert()
    
    pygame.draw.rect(background, (0, 0, 255), [400, 0, 100, 100], 0)
    screen.blit(background, (0, 0))
    screen.blit(disImage,(0,0))
    



pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Click a box')
background = pygame.Surface(size).convert()


pageNumber = 1

clock = pygame.time.Clock()
while True:
    if pageNumber == 1:
        gotoPage1(screen, background)
        
    elif pageNumber == 2:
        gotoPage2(screen, background)
        
        
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if x >=400 and x <= 500 and y >=0 and y <=100 and pageNumber == 1:
                pageNumber = 2
            elif x >=400 and x <= 500 and y >=0 and y <=100 and pageNumber == 2:
                pageNumber = 1
            elif x >=600 and x <=640 and y >=400 and y <=480:
                print("This is the bottom box")
                
    pygame.display.update()