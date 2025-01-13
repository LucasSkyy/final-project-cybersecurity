import pygame, sys
from pygame.locals import QUIT



def scene2(screen, background):
    
    background.fill((0, 0, 0))
    chess = pygame.image.load("Images/chess.jpg")
    newChess = pygame.transform.scale(chess, (200,200))
    newChess = newChess.convert()
    
    # Rect(left, top, width, height) and pygame.draw.rect(surface, color, rect, width)
    pygame.draw.rect(background, (255, 0, 0), [400, 0, 100, 100], 0)
    pygame.draw.rect(background, (255, 255, 0), [600, 400, 60, 80], 4)
    screen.blit(background, (0, 0))
    screen.blit(newChess, (0,0))
   
   

def scene1(screen, background):
    
    background.fill((255, 255, 255))
    disImage = pygame.image.load("Images/windows_background.jpg")
    chrome = pygame.image.load("Images/chrome.png")
    gmail = pygame.image.load("Images/gmail.png")
    newChrome = pygame.transform.scale(chrome,(40,40))
    newGmail = pygame.transform.scale(gmail,(32,26.5))
    winsearch = pygame.image.load("Images/winsearch.png")
    disImage = disImage.convert()
    
    pygame.draw.rect(background, (0, 0, 0), [0, 670, 1280, 75], 0)
    screen.blit(background, (0, 0))
    screen.blit(disImage,(0,0))
    screen.blit(winsearch,(0,670))
    screen.blit(newChrome,(495,675))
    screen.blit(newGmail,(550,682))
    



pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Click a box')
background = pygame.Surface(size).convert()



pageNumber = 1

clock = pygame.time.Clock()
while True:
    if pageNumber == 1:
        scene1(screen, background)
        
    elif pageNumber == 2:
        scene2(screen, background)
        
        
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