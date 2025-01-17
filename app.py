import os
import sys
import pygame

pygame.init()

pageNumber = 1

log_file = open("warnings.log", "w")
sys.stderr = log_file

from pygame.locals import QUIT
from datetime import datetime



def scene5(screen, background):
    background.fill((240, 240, 240))
    global pageNumber


#Scene 5 images
    rbc_logo = pygame.image.load("Images/rbc_logo.png")
    newrbc_logo = pygame.transform.scale(rbc_logo,(110,110))
    rbc_top = pygame.image.load("Images/rbc_top.png")
    rbc_side = pygame.image.load("Images/rbc_side.png")
    newrbc_side = pygame.transform.scale(rbc_side,(230,350))
    rbc_tab = pygame.image.load("Images/rbc_tab.png")
    zipfile = pygame.image.load("Images/zip.png")
    newzipfile = pygame.transform.scale(zipfile,(110,110))



    
#RBC UI
    pygame.draw.rect(background, (255, 255, 255), [190, 90, 1000, 550], 0)
    pygame.draw.rect(background, (0, 106, 195), [0, 77, 2000, 70], 0)
    pygame.draw.rect(background, (0, 106, 195), [10, 239, 10, 40], 0)
    


#Text and boxes

    #font and size
    fontURL = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 12)
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 19)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontmini = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 15)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 26)
    fontminibolddate = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 15)

    #URL
    pygame.draw.rect(rbc_tab, (18, 18, 18), [273, 49, 500, 20], 0)
    url_text = fontURL.render("http://www.rbccroyal-bank.com/person.al/login-page.html", True, (255,255,255))




    #UI text
    trans_text = font.render("Transaction History", True, (0,0,40))
    request = fontminibold.render("Please download the transaction history of your", True, (0,0,40))
    request2 = fontminibold.render("account to check for any malicious activities.", True, (0,0,40))
    zip_name = fontURL.render("history.zip", True, (0,0,40))
    




    # Scene 5 Blits
    screen.blit(background, (0, 0))
    screen.blit(newrbc_logo, (35, 90))
    screen.blit(rbc_top, (160, 81))
    screen.blit(newrbc_side, (-23, 290))
    screen.blit(trans_text, (22, 250))
    screen.blit(rbc_tab, (0, 0))
    screen.blit(url_text, (277, 52))
    screen.blit(request, (400, 220))
    screen.blit(request2, (400, 260))
    screen.blit(newzipfile, (480, 380))
    screen.blit(zip_name, (508, 500))




def scene4(screen, background):
    background.fill((240, 240, 240))

    
    # Load images and fonts (same as before)
    rbc_logo = pygame.image.load("Images/rbc_logo.png")
    newrbc_logo = pygame.transform.scale(rbc_logo, (110, 110))
    rbc_top = pygame.image.load("Images/rbc_top.png")
    rbc_wall = pygame.image.load("Images/rbc_wall.png")
    newrbc_wall = pygame.transform.scale(rbc_wall, (476, 463))
    rbc_side = pygame.image.load("Images/rbc_side.png")
    newrbc_side = pygame.transform.scale(rbc_side, (230, 350))
    rbc_tab = pygame.image.load("Images/rbc_tab.png")

    # Font definitions
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 25)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontmini = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 15)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 18)
    fontminibolddate = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 15)

    #RBC UI
    pygame.draw.rect(background, (255, 255, 255), [190, 90, 1000, 550], 0)
    pygame.draw.rect(background, (0, 106, 195), [0, 77, 2000, 70], 0)
    pygame.draw.rect(background, (0, 106, 195), [10, 239, 10, 40], 0)

    # URL for the login page
    pygame.draw.rect(rbc_tab, (18, 18, 18), [273, 49, 500, 20], 0)
    url_text = fontmini.render("http://www.rbccroyal-bank.com/person.al/login-page.html", True, (255, 255, 255))

    # Create input boxes for email, password, PIN, SSN
    email_box = pygame.draw.rect(background, (211, 211, 211), [870, 200, 300, 40], 0)
    pass_box = pygame.draw.rect(background, (211, 211, 211), [870, 310, 300, 40], 0)
    pin_box = pygame.draw.rect(background, (211, 211, 211), [870, 420, 300, 40], 0)
    ssn_box = pygame.draw.rect(background, (211, 211, 211), [870, 530, 300, 40], 0)

    # Text prompts
    email_text = fontsmaller.render("Email address:", True, (0, 0, 40))
    pass_text = fontsmaller.render("Password:", True, (0, 0, 40))
    pin_text = fontsmaller.render("PIN:", True, (0, 0, 40))
    ssn_text = fontsmaller.render("SSN:", True, (0, 0, 40))

    # Scene 4 Blits (UI setup)
    screen.blit(background, (0, 0))
    screen.blit(newrbc_logo, (35, 90))
    screen.blit(rbc_top, (160, 81))
    screen.blit(newrbc_wall, (210, 164))
    screen.blit(newrbc_side, (-23, 290))
    screen.blit(rbc_tab, (0, 0))
    screen.blit(url_text, (277, 52))

    # Display labels
    screen.blit(email_text, (700, 210))
    screen.blit(pass_text, (700, 310))
    screen.blit(pin_text, (700, 420))
    screen.blit(ssn_text, (700, 530))

    # User input handling
    user_input = {"email": "", "password": "", "pin": "", "ssn": ""}
    current_field = "email"  # Start with the email field
    global pageNumber
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input[current_field] = user_input[current_field][:-1]
                elif event.key == pygame.K_RETURN:
                    # Move to the next field (or submit form if all are filled)
                    if current_field == "email":
                        current_field = "password"
                    elif current_field == "password":
                        current_field = "pin"
                    elif current_field == "pin":
                        current_field = "ssn"
                    elif current_field == "ssn":
                        # For example, proceed to next page after SSN is entered
                        pageNumber = 5
                        running = False
                else:
                    user_input[current_field] += event.unicode

        # Render the text for each input box
        email_input_surface = font.render(user_input["email"], True, (0, 0, 0))
        pass_input_surface = font.render(user_input["password"], True, (0, 0, 0))
        pin_input_surface = font.render(user_input["pin"], True, (0, 0, 0))
        ssn_input_surface = font.render(user_input["ssn"], True, (0, 0, 0))

        # Display the input in each corresponding box
        screen.blit(email_input_surface, (875, 208))
        screen.blit(pass_input_surface, (875, 318))
        screen.blit(pin_input_surface, (875, 428))
        screen.blit(ssn_input_surface, (875, 538))

                # Draw a black outline around the selected input field
        if current_field == "email":
            pygame.draw.rect(screen, (0, 0, 0), [870, 200, 300, 40], 2)  # Outline for email
        elif current_field == "password":
            pygame.draw.rect(screen, (0, 0, 0), [870, 310, 300, 40], 2)  # Outline for password
        elif current_field == "pin":
            pygame.draw.rect(screen, (0, 0, 0), [870, 420, 300, 40], 2)  # Outline for PIN
        elif current_field == "ssn":
            pygame.draw.rect(screen, (0, 0, 0), [870, 530, 300, 40], 2)  # Outline for SSN

        pygame.display.flip()

    if pageNumber == 5:
        screen.fill((0, 0, 0))
        scene5(screen, background)
        pygame.display.flip()
    
def scene3(screen, background):
    background.fill((240, 240, 240))

    #font and size
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 25)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontmini = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 15)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 18)
    fontminibolddate = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 15)

    #search bar
    pygame.draw.rect(background, (211, 211, 211), [495, 20, 350, 40], 0)
    pygame.draw.circle(background, (211,211,211), (490,40), 20)
    pygame.draw.circle(background, (211,211,211), (850,40), 20)
    search_logo = pygame.image.load("Images/search_logo.png")
    Newsearch_logo = pygame.transform.scale(search_logo,(35,32))
    search_mess = fontsmaller.render('Search mail', True, (0,0,40))
    
    #Sidebar
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
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

    gmailFull = pygame.image.load("Images/gmailFull.png")
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

    #Scam Email Letter
    pygame.draw.rect(background, (255, 255, 255), [234, 76, 950, 600], 0)
    pygame.draw.rect(background, (240, 240, 240), [274, 210, 870, 400], 0)
    pygame.draw.rect(background, (255, 255, 255), [304, 240, 810, 340], 0)
    garbage = pygame.image.load("Images/garbage.png")
    profile = pygame.image.load("Images/profile.png")
    newProfile = pygame.transform.scale(profile,(37,37))
    newGarbage = pygame.transform.scale(garbage,(320,45))
    scam_title = font.render('URGENT: Account Activity Alert', True, (0,0,40))
    email_title = fontminibold.render('RBC Bank', True, (0,0,40))
    email_address = fontmini.render('<rbccroy.al-bank@gmail.com>', True, (0,0,40))
    email_dear = fontmini.render('Dear Customer,', True, (0, 0, 40))
    current_date = datetime.now().strftime('%B %d, %Y')
    bold_date = fontminibolddate.render(current_date, True, (0, 0, 40))
    email_letter1 = fontmini.render("We're letting you know that we've detected some unusual activity on your card on", True, (0,0,40))
    transaction1  = fontminibolddate.render("Approved transaction at SCM*CASH APP for $756.34 on", True, (0,0,40))
    transaction2  = fontminibolddate.render("Approved transaction at AMAZON for $491.56 on", True, (0,0,40))
    email_letter2 = fontmini.render("If you did not authorize these changes, please verify your transaction history with your social security number", True, (0,0,40))
    email_letter3 = fontmini.render("and pin through the link below! Sign On to verify your account details.", True, (0,0,40))
    actnow = fontminibolddate.render("ACT NOW! CLICK THE LINK BELOW.", True, (0,0,40))
    link = fontmini.render("http://www.rbccroyal-bank.com/person.al/login-page.html", True, (0,0,255))





    #Scene 3 Blits
    screen.blit(background, (0, 0))
    screen.blit(inbox, (65, 162))
    screen.blit(starred, (65, 200))
    screen.blit(important, (65, 240))
    screen.blit(sent, (65, 280))
    screen.blit(spam, (65, 320))
    screen.blit(gmailFull, (30, 20))
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
    screen.blit(newGarbage, (234,78))
    screen.blit(newProfile, (244,166))
    screen.blit(scam_title, (272,124))
    screen.blit(email_title, (288,171))
    screen.blit(email_address, (380,173))
    screen.blit(email_dear, (322,255))

    screen.blit(email_letter1, (346, 293))
    screen.blit(bold_date, (880, 293))

    screen.blit(transaction1, (346, 323))
    screen.blit(bold_date, (743, 323))
    screen.blit(transaction2, (346, 343))
    screen.blit(bold_date, (690, 343))

    screen.blit(email_letter2, (346, 373))
    screen.blit(email_letter3, (346, 393))
    screen.blit(actnow, (798, 393))
    screen.blit(link, (346, 450))

    pygame.draw.line(screen, (0, 0, 255), (346, 466), (717, 466), 2)



def scene2(screen, background):
    #background
    background.fill((240, 240, 240))
    

    #font and size
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 28)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontsmallest = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 16)
    fontboldsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 16)

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

    scamText = fontboldsmaller.render('RBC Bank                                   URGENT: Account Activity Alert', True, (0,0,40))
    email2 = fontsmallest.render('Google Classroom                      Returned: Culminating project', True, (0,0,40))
    email3 = fontsmallest.render('Instagram                                      You have 15 new notifications', True, (0,0,40))
    email4 = fontsmallest.render('Glenforest SS                              Course Selection 2025-2026', True, (0,0,40))
    email5 = fontsmallest.render('Jacob A.                                       Google Docs Sharing', True, (0,0,40))






    #search bar
    pygame.draw.rect(background, (211, 211, 211), [495, 20, 350, 40], 0)
    pygame.draw.circle(background, (211,211,211), (490,40), 20)
    pygame.draw.circle(background, (211,211,211), (850,40), 20)
    search_logo = pygame.image.load("Images/search_logo.png")
    Newsearch_logo = pygame.transform.scale(search_logo,(35,32))
    search_mess = fontsmaller.render('Search mail', True, (0,0,40))


    #Sidebar
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
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

    gmailFull = pygame.image.load("Images/gmailFull.png")
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
    screen.blit(gmailFull, (30, 20))
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
    screen.blit(scamText, (335 , 150))
    screen.blit(email2, (335 , 185))
    screen.blit(email3, (335 , 220))
    screen.blit(email4, (335 , 255))
    screen.blit(email5, (335 , 290))
    
   

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
    
sys.stderr = sys.__stderr__
log_file.close()

######################################################################################################################################

# Redirect low-level stderr to a log file
log_file = open("warnings.log", "w")
os.dup2(log_file.fileno(), sys.stderr.fileno())  # Redirect stderr

from pygame.locals import QUIT

# Define your scenes (scene1, scene2, scene3) and other setup code here
# ... (Your existing scene definitions are unchanged)

# Restore stderr to default after Pygame is initialized and images are loaded
# (Optional: Only if you want regular debug messages on the console after setup)
os.dup2(sys.__stderr__.fileno(), sys.stderr.fileno())
log_file.close()

# Initialize Pygame
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Click a box')
background = pygame.Surface(size).convert()

# Main game loop
def main():
    global pageNumber
    current_scene = "scene4"

    while True:
        if current_scene == "scene4":
            current_scene = scene4(screen, background)
        elif current_scene == "scene5":
            scene5(screen, background)
            current_scene = None  # Exit after Scene 5 (or handle further scenes)

clock = pygame.time.Clock()

while True:
    if pageNumber == 1:
        scene1(screen, background)
    elif pageNumber == 2:
        scene2(screen, background)
    elif pageNumber == 3:
        scene3(screen, background)
    elif pageNumber == 4:
        scene4(screen, background)
    elif pageNumber == 5:
        scene5(screen, background)

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y)  # Debugging output for mouse click positions
            if x >= 549 and x <= 582 and y >= 680 and y <= 708 and pageNumber == 1:
                pageNumber = 2
            elif x >= 1242 and x <= 1260 and y >= 27 and y <= 47 and pageNumber == 2:
                pageNumber = 1
            elif x >= 305 and x <= 1218 and y >= 142 and y <= 175 and pageNumber == 2:
                pageNumber = 3
            elif x >= 342 and x <= 722 and y >= 449 and y <= 469 and pageNumber == 3:
                pageNumber = 4
            elif x >= 248 and x <= 265 and y >= 92 and y <= 110 and pageNumber == 3:
                pageNumber = 2
            elif x >= 1238 and x <= 1278 and y >= 0 and y <= 35 and pageNumber == 4:
                pageNumber = 3
            elif x >= 869 and x <= 1170 and y >= 199 and y <= 238 and pageNumber == 4:
                pageNumber = 5
            




    pygame.display.update()