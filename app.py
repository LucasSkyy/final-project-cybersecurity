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
    #Icons
    disImage = pygame.image.load("Images/windows_background.jpg")
    chrome = pygame.image.load("Images/chrome.png")
    gmail = pygame.image.load("Images/gmail.png")
    gmail1 = pygame.image.load("Images/gmail.png")
    recy = pygame.image.load("Images/recyclying.png")
    adobe = pygame.image.load("Images/adobe.png")
    winsearch = pygame.image.load("Images/winsearch.png")
    thispc = pygame.image.load("Images/thispc.png")
    fileex = pygame.image.load("Images/fileex.png")
    setting = pygame.image.load("Images/setting.png")
    #Icons Resized
    newRecy = pygame.transform.scale(recy,(50,50))
    newChrome = pygame.transform.scale(chrome,(40,40))
    newGmail = pygame.transform.scale(gmail,(32,25))
    newAdobe = pygame.transform.scale(adobe,(43,43))
    Newthispc = pygame.transform.scale(thispc,(43,43))
    Newfileex = pygame.transform.scale(fileex,(43,43))
    newGmail1 = pygame.transform.scale(gmail1,(41,31))
    newSetting = pygame.transform.scale(setting,(35,31))

    disImage = disImage.convert() 
    
    pygame.draw.rect(disImage, (0, 0, 0), [0, 670, 1280, 75], 0)
    screen.blit(background, (0, 0))
    screen.blit(disImage,(0,0))
    screen.blit(winsearch,(0,670))
    screen.blit(newChrome,(495,675))
    screen.blit(newGmail,(550,682))
    screen.blit(newRecy,(20,30))
    screen.blit(newAdobe,(22,110))
    screen.blit(Newthispc,(20,180))
    screen.blit(Newfileex,(23,245))
    screen.blit(newGmail1,(25,320))
    screen.blit(newSetting,(600,678))
    



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
            print(x)
            print(y)
            if x >=400 and x <= 500 and y >=0 and y <=100 and pageNumber == 1:
                pageNumber = 2
            elif x >=400 and x <= 500 and y >=0 and y <=100 and pageNumber == 2:
                pageNumber = 1
            elif x >=600 and x <=640 and y >=400 and y <=480:
                print("This is the bottom box")
                
    pygame.display.update()