import pygame, sys
from pygame.locals import QUIT

def scene3(screen, background):
    background.fill((240, 240, 240))

    #font and size
    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 28)
    fontsmaller = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 22)

    #search bar
    pygame.draw.rect(background, (211, 211, 211), [495, 20, 350, 40], 0)
    pygame.draw.circle(background, (211,211,211), (490,40), 20)
    pygame.draw.circle(background, (211,211,211), (850,40), 20)
    search_logo = pygame.image.load("Images/search_logo.png")
    Newsearch_logo = pygame.transform.scale(search_logo,(35,32))
    search_mess = fontsmaller.render('Search mail', True, (0,0,40))
    
    #Sidebar
    fontsmaller = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 22)
    inbox = fontsmaller.render('Inbox', True, (0,0,40))
    starred = fontsmaller.render('Starred', True, (0,0,40))
    important = fontsmaller.render('Important', True, (0,0,40))
    sent = fontsmaller.render('Sent', True, (0,0,40))
    spam = fontsmaller.render('Spam', True, (0,0,40))
    compose = fontsmaller.render('Compose', True, (0,0,40))
    pygame.draw.rect(background, (190, 230, 245), [40, 80, 130, 60], 0)
    pygame.draw.circle(background, (190, 230, 245), (45,110), 30)
    pygame.draw.circle(background, (190, 230, 245), (170,110), 30)


    pygame.draw.rect(background, (211, 227, 253), [0, 160, 180, 30], 0)
    pygame.draw.circle(background, (211, 227, 253), (180,175), 15)

    gmaiFull = pygame.image.load("Images/gmailFull.png")
    back = pygame.image.load("Images/remove.png.png")

    inbox_logo = pygame.image.load("Images/inbox_logo.png")
    starred_logo = pygame.image.load("Images/starred_logo.png")
    important_logo = pygame.image.load("Images/important_logo.png")
    sent_logo = pygame.image.load("Images/sent_logo.png")
    spam_logo = pygame.image.load("Images/spam_logo.png")
    compose_logo = pygame.image.load("Images/compose_logo.png")
    Newcompose_logo = pygame.transform.scale(compose_logo,(38,35))

    Newstarred_logo = pygame.transform.scale(starred_logo,(28,25))
    Newimportant_logo = pygame.transform.scale(important_logo,(23,21))
    Newsent_logo = pygame.transform.scale(sent_logo,(30,30))
    newBack = pygame.transform.scale(back,(100,50))
    Newspam_logo = pygame.transform.scale(spam_logo,(43,40))

    screen.blit(background, (0, 0))
    screen.blit(inbox, (65, 162))
    screen.blit(starred, (65, 200))
    screen.blit(important, (65, 240))
    screen.blit(sent, (65, 280))
    screen.blit(spam, (65, 320))
    screen.blit(gmaiFull, (30, 20))
    screen.blit(compose, (74, 96))
    screen.blit(newBack, (1170, 10))
    screen.blit(inbox_logo, (20, 163))
    screen.blit(Newstarred_logo, (16, 200))
    screen.blit(Newimportant_logo, (19, 240))
    screen.blit(Newsent_logo, (17, 277))
    screen.blit(Newspam_logo, (10, 315))
    screen.blit(Newsearch_logo, (480, 28))
    screen.blit(search_mess, (530, 28))
    screen.blit(Newcompose_logo, (25, 92))



def scene2(screen, background):
    #background
    background.fill((240, 240, 240))
    

    #font and size
    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 28)
    fontsmaller = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 22)
    fontboldsmaller = pygame.font.Font('C:\Windows\Fonts\Arialbd.ttf', 22)

    #main index
    pygame.draw.rect(background, (255, 255, 255), [220, 75, 1000, 620], 0)

    
    
    pygame.draw.rect(background, (235, 235, 235), [220, 178, 1000, 32], 0)
    pygame.draw.rect(background, (235, 235, 235), [220, 213, 1000, 32], 0)
    pygame.draw.rect(background, (235, 235, 235), [220, 248, 1000, 32], 0)
    pygame.draw.rect(background, (235, 235, 235), [220, 283, 1000, 32], 0)
    
    
    
    pygame.draw.line(background, (200, 200, 200), (219,139), (1220,139), 2)
    pygame.draw.line(background, (200, 200, 200), (219,176), (1220,176), 2)
    pygame.draw.line(background, (200, 200, 200), (219,211), (1220,211), 2)
    pygame.draw.line(background, (200, 200, 200), (219,246), (1220,246), 2)
    pygame.draw.line(background, (200, 200, 200), (219,281), (1220,281), 2)
    pygame.draw.line(background, (200, 200, 200), (219,316), (1220,316), 2)

    reload_logo = pygame.image.load("Images/reload.png")
    extra_logo = pygame.image.load("Images/extra.png")
    end_logo = pygame.image.load("Images/end_logo.png")

    scamText = fontboldsmaller.render('RBC Bank', True, (0,0,40))
    





    #search bar
    pygame.draw.rect(background, (211, 211, 211), [495, 20, 350, 40], 0)
    pygame.draw.circle(background, (211,211,211), (490,40), 20)
    pygame.draw.circle(background, (211,211,211), (850,40), 20)
    search_logo = pygame.image.load("Images/search_logo.png")
    Newsearch_logo = pygame.transform.scale(search_logo,(35,32))
    search_mess = fontsmaller.render('Search mail', True, (0,0,40))


    #Sidebar
    fontsmaller = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 22)
    inbox = fontsmaller.render('Inbox', True, (0,0,40))
    starred = fontsmaller.render('Starred', True, (0,0,40))
    important = fontsmaller.render('Important', True, (0,0,40))
    sent = fontsmaller.render('Sent', True, (0,0,40))
    spam = fontsmaller.render('Spam', True, (0,0,40))
    compose = fontsmaller.render('Compose', True, (0,0,40))
    pygame.draw.rect(background, (190, 230, 245), [40, 80, 130, 60], 0)
    pygame.draw.circle(background, (190, 230, 245), (45,110), 30)
    pygame.draw.circle(background, (190, 230, 245), (170,110), 30)

    pygame.draw.rect(background, (211, 227, 253), [0, 160, 180, 30], 0)
    pygame.draw.circle(background, (211, 227, 253), (180,175), 15)

    gmaiFull = pygame.image.load("Images/gmailFull.png")
    back = pygame.image.load("Images/remove.png.png")

    inbox_logo = pygame.image.load("Images/inbox_logo.png")
    starred_logo = pygame.image.load("Images/starred_logo.png")
    important_logo = pygame.image.load("Images/important_logo.png")
    sent_logo = pygame.image.load("Images/sent_logo.png")
    spam_logo = pygame.image.load("Images/spam_logo.png")
    compose_logo = pygame.image.load("Images/compose_logo.png")
    Newcompose_logo = pygame.transform.scale(compose_logo,(38,35))

    Newstarred_logo = pygame.transform.scale(starred_logo,(28,25))
    Newimportant_logo = pygame.transform.scale(important_logo,(23,21))
    Newsent_logo = pygame.transform.scale(sent_logo,(30,30))
    newBack = pygame.transform.scale(back,(100,50))
    Newspam_logo = pygame.transform.scale(spam_logo,(43,40))

    

    
    
    
    
    
    screen.blit(background, (0, 0))
    screen.blit(inbox, (65, 162))
    screen.blit(starred, (65, 200))
    screen.blit(important, (65, 240))
    screen.blit(sent, (65, 280))
    screen.blit(spam, (65, 320))
    screen.blit(gmaiFull, (30, 20))
    screen.blit(compose, (74, 96))
    screen.blit(newBack, (1170, 10))
    screen.blit(inbox_logo, (20, 163))
    screen.blit(Newstarred_logo, (16, 200))
    screen.blit(Newimportant_logo, (19, 240))
    screen.blit(Newsent_logo, (17, 277))
    screen.blit(Newspam_logo, (10, 315))
    screen.blit(Newsearch_logo, (480, 28))
    screen.blit(search_mess, (530, 28))
    screen.blit(Newcompose_logo, (25, 92))
    screen.blit(reload_logo, (230 , 92))
    screen.blit(extra_logo, (245 , 143))
    screen.blit(extra_logo, (245 , 178))
    screen.blit(extra_logo, (245 , 213))
    screen.blit(extra_logo, (245 , 248))
    screen.blit(extra_logo, (245 , 283))
    screen.blit(end_logo, (320 , 330))
    screen.blit(scamText, (335 , 144))
    
   

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
    

######################################################################################################################################

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

    elif pageNumber == 3:
        scene3(screen, background)
        


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
            if x >=549 and x <= 582 and y >=680 and y <=708 and pageNumber == 1:
                pageNumber = 2
            elif x >=1242 and x <= 1260 and y >=27 and y <=47 and pageNumber == 2:
                pageNumber = 1
            elif x >=220 and x <= 1219 and y >=75 and y <=113 and pageNumber == 2:
                pageNumber = 3

            elif x >=600 and x <=640 and y >=400 and y <=480:
                print("This is the bottom box")


    pygame.display.update()