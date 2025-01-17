import os
import sys
import pygame

pygame.init()
pageNumber = 1
log_file = open("warnings.log", "w")
sys.stderr = log_file

from pygame.locals import QUIT
from datetime import datetime

def scene11(screen, background):
    background.fill((240, 240, 240))
    global pageNumber

#UI

    #Images
    next = pygame.image.load("Images/next.png")
    newnext = pygame.transform.scale(next,(100,100))
    back = pygame.image.load("Images/next.png")
    newback = pygame.transform.scale(next,(100,100))
    realback = pygame.transform.flip(newback, True, False)

       #font and size
    fontURL = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 12)
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 25)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontmini = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 15)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 50)
    fontminibolddate = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 15)
    
    
    pygame.draw.rect(background, (255, 255, 255), [143, 100, 1000, 550], 0)
    pause = fontminibold.render("Congratulations!", True, (0,0,40))
    pause_text = font.render("You've learned key tips to stay safe online and protect your personal information.", True, (0,0,40))
    pause_text2 = font.render("By recognizing fake websites, avoiding suspicious downloads, and checking URLs", True, (0,0,40))
    pause_text3 = font.render("carefully, you can keep your information secure. Always double-check and contact", True, (0,0,40))
    pause_text4 = font.render("ca trusted source before sharing sensitive information online!", True, (0,0,40))
    


#scene 11 blit

    screen.blit(background,(0,0))
    screen.blit(pause,(450,180))
    screen.blit(pause_text,(200,300))
    screen.blit(pause_text2,(200,350))
    screen.blit(pause_text3,(200,400))
    screen.blit(pause_text4,(200,450))
    screen.blit(realback,(120,590))




def scene10(screen, background):
    background.fill((240, 240, 240))
    global pageNumber

    next = pygame.image.load("Images/next.png")
    newnext = pygame.transform.scale(next,(60,60))
    back = pygame.image.load("Images/next.png")
    newback = pygame.transform.scale(next,(60,60))
    realback = pygame.transform.flip(newback, True, False)

    RBC_logo = pygame.image.load("Images/RBC_logo.png")
    newRBC_logo = pygame.transform.scale(RBC_logo,(110,110))
    rbc_top = pygame.image.load("Images/rbc_top.png")
    rbc_side = pygame.image.load("Images/rbc_side.png")
    newrbc_side = pygame.transform.scale(rbc_side,(230,350))
    rbc_tab = pygame.image.load("Images/rbc_tab.png")
    zip_file = pygame.image.load("Images/zip.png")
    newzip = pygame.transform.scale(zip_file,(110,110))
    download = pygame.image.load("Images/download.png")
    newdownload = pygame.transform.scale(download,(190,55))




    
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
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 18)
    fontminibolddate = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 15)

        #URL
    pygame.draw.rect(rbc_tab, (18, 18, 18), [273, 49, 500, 20], 0)
    url_text = fontURL.render("http://www.rbccroyal-bank.com/person.al/login-page.html", True, (255,255,255))




        #UI text
    trans_text = font.render("Transaction History", True, (0,0,40))
    request = fontminibold.render("Please download the transaction history of your", True, (0,0,40))
    request2 = fontminibold.render("account to check for any malicious activities.", True, (0,0,40))
    zip_name = fontURL.render("history.zip", True, (0,0,40))
    
#Explanation#######################################################################################################################################
    phis_text = fontminibold.render('If any website asks you to download something,', True, (255,0,0))
    phis_text2 = fontminibold.render('it may be a virus. Here’s how to spot it:', True, (255,0,0))
    phis_text3 = fontminibold.render('1. Check for a suspicious file name', True, (255,0,0))
    phis_text4 = fontminibold.render('2. Be cautious', True, (255,0,0))
    phis_text5 = fontmini.render('Avoid files with extensions like .exe, .bat, .js, .vbs, or .scr,', True, (0,0,40))
    phis_text6 = fontmini.render('unless you’re 100% sure they’re safe and necessary. These are', True, (0,0,40))
    phis_text7 = fontmini.render('usually programs that could run and infect your computer,', True, (0,0,50))
    phis_text8 = fontmini.render('so make sure you check the use of the file. In this case,', True, (0,0,50))
    phis_text9 = fontmini.render('the bank transaction history is supposed to be a document,', True, (0,0,50))
    phis_text10 = fontmini.render('but it shows as a .exe file, used for for running programs and commands.', True, (0,0,50))
    phis_text11 = fontmini.render('Like with emails and links previously, file names that are spelled', True, (0,0,50))
    phis_text12 = fontmini.render('suspiciously or with spelling mistakes are usually unsafe.', True, (0,0,50))
    phis_text13 = fontmini.render('f a file name isn’t what you expect, you should always make sure with', True, (0,0,50))
    phis_text14 = fontmini.render('a scanner like virustotal or antivirus checker.', True, (0,0,50))
    phis_text15 = fontmini.render('', True, (0,0,50))
    phis_text16 = fontmini.render('', True, (0,0,50))
    phis_text17 = fontmini.render('', True, (0,0,50))



#######################################################################################################################################
# Scene 10 Blits
    screen.blit(background, (0, 0))
    screen.blit(newRBC_logo, (35, 90))
    screen.blit(rbc_top, (160, 81))
    screen.blit(newrbc_side, (-23, 290))
    screen.blit(trans_text, (22, 250))
    screen.blit(rbc_tab, (0, 0))
    screen.blit(url_text, (277, 52))
    screen.blit(request, (400, 220))
    screen.blit(request2, (400, 260))
    screen.blit(newzip, (480, 380))
    screen.blit(zip_name, (508, 500))
    screen.blit(newdownload, (680, 400))

    pygame.draw.rect(screen,(211, 227, 253), [0, 550, 2000, 250], 0)
    screen.blit(phis_text, (280, 164))
    screen.blit(phis_text2, (700, 164))
    screen.blit(phis_text3, (150,570))
    screen.blit(phis_text4, (751,570))
    screen.blit(phis_text5, (105,600))
    screen.blit(phis_text6, (105, 618))
    screen.blit(phis_text7, (105,636))
    screen.blit(phis_text8, (105, 654))
    screen.blit(phis_text9, (105, 672))
    screen.blit(phis_text10, (105, 690))
    screen.blit(phis_text11, (700, 600))
    screen.blit(phis_text12, (700, 618))
    screen.blit(phis_text13, (700, 636))
    screen.blit(phis_text14, (700, 654))

 


    
    screen.blit(newnext, (1140, 505))
    screen.blit(realback, (75, 505))


    




def scene9(screen, background):
    background.fill((240, 240, 240))
    global pageNumber

    next = pygame.image.load("Images/next.png")
    newnext = pygame.transform.scale(next,(60,60))
    back = pygame.image.load("Images/next.png")
    newback = pygame.transform.scale(next,(60,60))
    realback = pygame.transform.flip(newback, True, False)

    #font and size
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 25)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontmini = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 17)
    fontminireal = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 15)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 25)
    fontminiboldreal = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 18)
    fontminibolddate = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 15)

#Scene 9 images
    RBC_logo = pygame.image.load("Images/RBC_logo.png")
    newRBC_logo = pygame.transform.scale(RBC_logo,(110,110))
    rbc_top = pygame.image.load("Images/rbc_top.png")
    rbc_wall = pygame.image.load("Images/rbc_wall.png")
    newrbc_wall = pygame.transform.scale(rbc_wall,(476,463))
    rbc_side = pygame.image.load("Images/rbc_side.png")
    newrbc_side = pygame.transform.scale(rbc_side,(230,350))
    rbc_tab = pygame.image.load("Images/rbc_tab.png")


    
#RBC UI
    pygame.draw.rect(background, (255, 255, 255), [190, 90, 1000, 550], 0)
    pygame.draw.rect(background, (0, 106, 195), [0, 77, 2000, 70], 0)
    pygame.draw.rect(background, (0, 106, 195), [10, 239, 10, 40], 0)
    


#Text and boxes

        #font and size
    fontURL = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 12)
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 25)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontmini = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 15)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 27)
    fontminibolddate = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 15)

        #URL
    pygame.draw.rect(rbc_tab, (18, 18, 18), [273, 49, 500, 20], 0)
    url_text = fontURL.render("http://www.rbccroyal-bank.com/person.al/login-page.html", True, (255,255,255))


    
        #email
    email_box = pygame.draw.rect(background, (211, 211, 211), [870, 200, 300, 40], 0)
    email_text = fontsmaller.render("Email address:", True, (0,0,40))

        #Password
    pass_box = pygame.draw.rect(background, (211, 211, 211), [870, 310, 300, 40], 0)
    pass_text = fontsmaller.render("Password:", True, (0,0,40))

        #PIN
    pin_box = pygame.draw.rect(background, (211, 211, 211), [870, 420, 300, 40], 0)
    pin_text = fontsmaller.render("PIN:", True, (0,0,40))

        #SSN
    ssn_box = pygame.draw.rect(background, (211, 211, 211), [870, 530, 300, 40], 0)
    ssn_text = fontsmaller.render("SSN:", True, (0,0,40))

        #UI text
    signin_text = font.render("Sign In", True, (0,0,40))
#Expllanation##############################################################################################################################
    pygame.draw.rect(background,(211, 227, 253), [200, 153, 480, 480], 0)
    pygame.draw.rect(screen,(211, 227, 253), [470, 20, 410, 55], 0)

    phis_text = fontminibold.render('Wait, is this link safe?', True, (255,0,0))
    phis_text2 = fontmini.render('If you click a link and it asks for personal details like your PIN, SSN,', True, (0,0,50))
    phis_text3 = fontmini.render('password, or email, it’s likely a scam. Heres how to spot it:', True, (0,0,50))
    phis_text4 = fontminibold.render('1. Check the URL', True, (255,0,0))
    phis_text5 = fontminibold.render('2. Look for "https://"', True, (255,0,0))
    phis_text6 = fontminibold.render('3. Be cautious', True, (255,0,0))
    phis_text7 = fontmini.render('Look for typos or extra words. In this example, the link', True, (0,0,50))
    phis_text8 = fontmini.render('http://www.rbccroyal-bank.com/person.al/login-page.html has two c’s', True, (0,0,50))
    phis_text9 = fontmini.render('in rbc, a hyphen between “royal bank”, and a period in between', True, (0,0,50))
    phis_text10 = fontmini.render('“personal”. Subtle typos like these can lead to fake websites.', True, (0,0,50))
    phis_text11 = fontmini.render('Real sites have "https://" and a padlock icon to show they’re secure.', True, (0,0,50))
    phis_text12 = fontmini.render('Here, it is an http:// link which could be unsafe.', True, (0,0,50))
    phis_text13 = fontmini.render('If the site asks for your PIN, SSN, password, or email, don’t enter', True, (0,0,50))
    phis_text14 = fontmini.render('anything until you are absolutely certain that its a trustable site.', True, (0,0,50))
    phis_text15 = fontmini.render('You should always confirm the website address by checking it with the', True, (0,0,50))
    phis_text16 = fontmini.render('official site. Antivirus checkers like virustotal are great ways to paste', True, (0,0,50))
    phis_text17 = fontmini.render('a url and check for malicious flags.', True, (0,0,50))






##########################################################################################################################################################
# Scene 9 Blits
    screen.blit(background, (0, 0))
    screen.blit(newRBC_logo, (35, 90))
    screen.blit(rbc_top, (160, 81))
    screen.blit(email_text, (700, 210))
    screen.blit(pass_text, (700, 310))
    screen.blit(pin_text, (700, 420))
    screen.blit(ssn_text, (700, 530))
    
    screen.blit(newrbc_side, (-23, 290))
    screen.blit(signin_text, (30, 240))
    screen.blit(rbc_tab, (0, 0))
    screen.blit(url_text, (277, 52))

    pygame.draw.rect(screen,(211, 227, 253), [310, 87, 410, 55], 0)
    screen.blit(phis_text, (360, 100))
    screen.blit(phis_text2, (225, 161))
    screen.blit(phis_text3, (225, 179))
    screen.blit(phis_text4, (216,203))
    screen.blit(phis_text5, (216, 330))
    screen.blit(phis_text6, (216, 418))
    screen.blit(phis_text7, (209,237))
    screen.blit(phis_text8, (209, 255))
    screen.blit(phis_text9, (209, 273))
    screen.blit(phis_text10, (209, 291))
    screen.blit(phis_text11, (209, 366))
    screen.blit(phis_text12, (209, 384))
    screen.blit(phis_text13, (209, 462))
    screen.blit(phis_text14, (209, 480))
    screen.blit(phis_text15, (209, 498))
    screen.blit(phis_text16, (209, 516))
    screen.blit(phis_text17, (209, 534))
    screen.blit(newnext, (1140, 645))
    screen.blit(realback, (75, 645))
   
    pygame.draw.line(screen, (255, 0, 0), (274,68), (304,68), 3)
    pygame.draw.line(screen, (255, 0, 0), (350,68), (372,68), 3)
    pygame.draw.line(screen, (255, 0, 0), (457,68), (510,68), 3)

    


def scene8(screen, background):
    background.fill((240, 240, 240))
    global pageNumber

    next = pygame.image.load("Images/next.png")
    newnext = pygame.transform.scale(next,(60,60))
    back = pygame.image.load("Images/next.png")
    newback = pygame.transform.scale(next,(60,60))
    realback = pygame.transform.flip(newback, True, False)

    #font and size
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 25)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontmini = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 17)
    fontminireal = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 15)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 25)
    fontminiboldreal = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 18)
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
    email_title = fontminiboldreal.render('RBC Bank', True, (0,0,40))
    email_address = fontminireal.render('<rbccroy.al-bank@gmail.com>', True, (0,0,40))
    email_dear = fontminireal.render('Dear Customer,', True, (0, 0, 40))
    current_date = datetime.now().strftime('%B %d, %Y')
    bold_date = fontminibolddate.render(current_date, True, (0, 0, 40))
    email_letter1 = fontminireal.render("We're letting you know that we've detected some unusual activity on your card on", True, (0,0,40))
    transaction1  = fontminibolddate.render("Approved transaction at SCM*CASH APP for $756.34 on", True, (0,0,40))
    transaction2  = fontminibolddate.render("Approved transaction at AMAZON for $491.56 on", True, (0,0,40))
    email_letter2 = fontminireal.render("If you did not authorize these changes, please verify your transaction history with your social security number", True, (0,0,40))
    email_letter3 = fontminireal.render("and pin through the link below! Sign On to verify your account details.", True, (0,0,40))
    actnow = fontminibolddate.render("ACT NOW! CLICK THE LINK BELOW.", True, (0,0,40))
    link = fontmini.render("http://www.rbccroyal-bank.com/person.al/login-page.html", True, (0,0,255))
#Explanation##################################################################################################################################

    pygame.draw.rect(background,(211, 227, 253), [0, 550, 2000, 250], 0)
    pygame.draw.line(background, (255, 0, 0), (392,191), (571,191), 3)


    


    phis_text2 = fontmini.render('Scam emails can pretend to be from your bank, using fake logos and urgent', True, (0,0,50))
    phis_text3 = fontmini.render('messages to trick you into believing its from the actual bank.', True, (0,0,50))
    phis_text4 = fontmini.render('They often come from fake email addresses and use "Dear Customer"', True, (0,0,50))
    phis_text5 = fontmini.render('instead of your name. Real banks never ask for passwords or account', True, (0,0,50))
    phis_text6 = fontmini.render('details in an email.Always check by calling your bank or using their official', True, (0,0,50))
    phis_textsd = fontmini.render('website.', True, (0,0,50))
    phis_text7 = fontmini.render('1. Always check who it is from', True, (0,0,50))
    phis_text8 = fontmini.render('2. Does the email make sense', True, (0,0,50))
    phis_text10 = fontmini.render('Notice the email address it is sent from,', True, (0,0,50))
    phis_text11 = fontmini.render('has spelling mistakes and does not', True, (0,0,50))
    phis_text12 = fontmini.render('match a real email address from RBC.', True, (0,0,50))
    phis_text13 = fontmini.render('Oftentimes there will be spelling errors', True, (0,0,50))
    phis_text14 = fontmini.render('and extra letters or special characters.', True, (0,0,50))
    phis_text15 = fontmini.render('In this example, it says there were 2 large', True, (0,0,50))
    phis_text16 = fontmini.render('payments made on your card today from', True, (0,0,50))
    phis_text17 = fontmini.render('cash app and amazon. Ask yourself if', True, (0,0,50))
    phis_text18 = fontmini.render('this was true, and who has access to your .', True, (0,0,50))
    phis_text19 = fontmini.render('account.', True, (0,0,50))



################################################################################################################################################


    #Scene 8 Blits
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

    
    screen.blit(phis_text2, (20, 568))
    screen.blit(phis_text3, (20, 590))
    screen.blit(phis_text4, (20, 613))
    screen.blit(phis_text5, (20, 636))
    screen.blit(phis_text6, (20, 659))
    screen.blit(phis_textsd, (20, 682))
    screen.blit(phis_text7, (635, 574))
    screen.blit(phis_text8, (950, 573))
    screen.blit(phis_text10, (635,603))
    screen.blit(phis_text11, (635,623))
    screen.blit(phis_text12, (635,643))
    screen.blit(phis_text13, (635,663))
    screen.blit(phis_text14, (635, 683))
    screen.blit(phis_text15, (950, 601))
    screen.blit(phis_text16, (950, 621))
    screen.blit(phis_text17, (950, 641))
    screen.blit(phis_text18, (950, 661))
    screen.blit(phis_text19, (950, 681))
    screen.blit(newnext,(1200,500))
    screen.blit(realback,(10,500))

    pygame.draw.line(screen, (0, 0, 255), (346, 466), (717, 466), 2)



    

def scene7(screen, background):
    background.fill((240, 240, 240))
    global pageNumber

    next = pygame.image.load("Images/next.png")
    newnext = pygame.transform.scale(next,(60,60))
    back = pygame.image.load("Images/next.png")
    newback = pygame.transform.scale(next,(60,60))
    realback = pygame.transform.flip(newback, True, False) 

    #font and size
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 25)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontmini = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 17)
    fontminireal = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 15)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 25)
    fontminiboldreal = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 18)
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
    email_title = fontminiboldreal.render('RBC Bank', True, (0,0,40))
    email_address = fontminireal.render('<rbccroy.al-bank@gmail.com>', True, (0,0,40))
    email_dear = fontminireal.render('Dear Customer,', True, (0, 0, 40))
    current_date = datetime.now().strftime('%B %d, %Y')
    bold_date = fontminibolddate.render(current_date, True, (0, 0, 40))
    email_letter1 = fontminireal.render("We're letting you know that we've detected some unusual activity on your card on", True, (0,0,40))
    transaction1  = fontminibolddate.render("Approved transaction at SCM*CASH APP for $756.34 on", True, (0,0,40))
    transaction2  = fontminibolddate.render("Approved transaction at AMAZON for $491.56 on", True, (0,0,40))
    email_letter2 = fontminireal.render("If you did not authorize these changes, please verify your transaction history with your social security number", True, (0,0,40))
    email_letter3 = fontminireal.render("and pin through the link below! Sign On to verify your account details.", True, (0,0,40))
    actnow = fontminibolddate.render("ACT NOW! CLICK THE LINK BELOW.", True, (0,0,40))
    link = fontmini.render("http://www.rbccroyal-bank.com/person.al/login-page.html", True, (0,0,255))



    #Expanation#######################################################################################
    pygame.draw.rect(background,(211, 227, 253), [470, 20, 410, 55], 0)
    pygame.draw.rect(background,(211, 227, 253), [0, 550, 2000, 250], 0)
    pygame.draw.rect(background,(255, 0, 0), [470, 20, 410, 55], 1)
    pygame.draw.rect(background,(255, 0, 0), [790, 382, 283, 35], 5)
    


    phis_text = fontminibold.render('But first, what is ‘Phishing’?', True, (255,0,0))
    phis_text2 = fontmini.render('Phishing is a type of cybersecurity attack where someone tries to fool you into giving them your important information, like passwords, bank details, or personal', True, (0,0,50))
    phis_text3 = fontmini.render('secrets. It’s like a trick thats disguised as something or someone you trust, and makes you give sensitive information to dangerous people or download malicious files.', True, (0,0,50))
    phis_text4 = fontmini.render('Imagine you get an email or a message that looks like it’s from your favorite video game or a store you trust. It might say something like: “Your account has a problem!', True, (0,0,50))
    phis_text5 = fontmini.render('Click here to fix it.” It looks real, but it’s actually from a scammer pretending to be that company. When you click the link, they might ask you to type in your ', True, (0,0,50))
    phis_text6 = fontmini.render('password or other private info. If you do, they take that information and can use it to steal things from you.', True, (0,0,50))


    ###################################################################################################

    #Scene 7 Blits
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

    screen.blit(phis_text, (495, 38))
    screen.blit(phis_text2, (20, 568))
    screen.blit(phis_text3, (20, 590))
    screen.blit(phis_text4, (20, 613))
    screen.blit(phis_text5, (20, 636))
    screen.blit(phis_text6, (20, 659))
    screen.blit(newnext,(1200,500))
    screen.blit(realback,(10,500))
  
    


    pygame.draw.line(screen, (0, 0, 255), (346, 466), (717, 466), 2)
    


def scene6(screen, background):
    background.fill((240, 240, 240))
    global pageNumber

#UI

        #Images
    next = pygame.image.load("Images/next.png")
    newnext = pygame.transform.scale(next,(110,110))

       #font and size
    fontURL = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 12)
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 25)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontmini = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 15)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 30)
    fontminibolddate = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 15)
    
    
    pygame.draw.rect(background, (255, 255, 255), [143, 100, 1000, 550], 0)
    pause = fontminibold.render("Pause for a moment, what just happened?", True, (0,0,40))
    pause_text = font.render("This is a real life example of how individuals get their personal information stolen.", True, (0,0,40))
    pause_text2 = font.render("You just experienced is a form of phishing, which leads to having sensitive bank", True, (0,0,40))
    pause_text3 = font.render("information taken from scammers.", True, (0,0,40))


#scene 6 blit

    screen.blit(background,(0,0))
    screen.blit(pause,(370,40))
    screen.blit(pause_text,(200,300))
    screen.blit(pause_text2,(200,350))
    screen.blit(pause_text3,(200,400))
    screen.blit(newnext,(1075,565))









def scene5(screen, background):
    background.fill((240, 240, 240))
    global pageNumber

    # Load assets (icons, images, fonts)
    disImage = pygame.image.load("Images/windows_background.jpg")
    chrome = pygame.image.load("Images/chrome.png")
    gmail = pygame.image.load("Images/gmail.png")
    recy = pygame.image.load("Images/recyclying.png")
    adobe = pygame.image.load("Images/adobe.png")
    winsearch = pygame.image.load("Images/winsearch.png")
    thispc = pygame.image.load("Images/thispc.png")
    fileex = pygame.image.load("Images/fileex.png")
    setting = pygame.image.load("Images/setting.png")
    gmail1 = pygame.image.load("Images/gmail.png")

    newRecy = pygame.transform.scale(recy, (50, 50))
    newChrome = pygame.transform.scale(chrome, (40, 40))
    newGmail = pygame.transform.scale(gmail, (32, 25))
    newAdobe = pygame.transform.scale(adobe, (43, 43))
    Newthispc = pygame.transform.scale(thispc, (43, 43))
    Newfileex = pygame.transform.scale(fileex, (43, 43))
    newGmail1 = pygame.transform.scale(gmail1, (41, 31))
    newSetting = pygame.transform.scale(setting, (35, 31))

    RBC_logo = pygame.image.load("Images/RBC_logo.png")
    newRBC_logo = pygame.transform.scale(RBC_logo, (110, 110))
    rbc_top = pygame.image.load("Images/rbc_top.png")
    rbc_side = pygame.image.load("Images/rbc_side.png")
    newrbc_side = pygame.transform.scale(rbc_side, (230, 350))
    rbc_tab = pygame.image.load("Images/rbc_tab.png")
    zip_file = pygame.image.load("Images/zip.png")
    newzip = pygame.transform.scale(zip_file, (110, 110))
    download = pygame.image.load("Images/download.png")
    newdownload = pygame.transform.scale(download, (230, 70))

    # Load notification image (adjusted size)
    virus_notification = pygame.image.load("Images/virus_notification.png")
    newvirus_notification = pygame.transform.scale(virus_notification, (500, 200))

    # Fonts
    fontURL = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 12)
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 19)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 26)

    # Notification settings
    screen_width, screen_height = screen.get_size()
    notification_width = 500
    notification_height = 200
    notification_x = screen_width  # Start off-screen to the right
    notification_target_x = screen_width - notification_width - 20  # 20px margin from the right
    notification_y = screen_height - notification_height - 20  # 20px margin from the bottom
    notification_speed = 15  # Speed of sliding (pixels per frame)
    sliding_started = False
    sliding_done = False
    notification_start_time = None  # To track when the notification starts
    switch_scene_time = None  # To track when the scene should change

    # Download button coordinates
    download_button_rect = pygame.Rect(680, 400, 230, 70)

    # Scene loop
    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if download_button_rect.collidepoint(event.pos):  # Check if clicked inside the button
                        sliding_started = True
                        notification_start_time = current_time  # Track when the notification starts
                        switch_scene_time = None  # Reset switch scene timer

        # Hover effect for the button (scale down on hover)
        if download_button_rect.collidepoint(pygame.mouse.get_pos()):
            button_width = 230 * 0.9
            button_height = 70 * 0.9
        else:
            button_width = 230
            button_height = 70

        # Slide notification logic
        if sliding_started and not sliding_done:
            if notification_x > notification_target_x:
                notification_x -= notification_speed  # Move notification left
            if notification_x <= notification_target_x:
                sliding_done = True  # Stop sliding when the target position is reached
                # Once the notification finishes sliding, start the delay for scene switch
                switch_scene_time = current_time

        # Check if 3 seconds have passed since notification finished sliding
        if switch_scene_time and current_time - switch_scene_time > 5000:  # 3 seconds
            pageNumber = 6  # Switch to scene 6 after 3 seconds
            return scene6(screen, background)  # Call scene 6

        # Draw the background
        screen.blit(background, (0, 0))
        pygame.draw.rect(background, (255, 255, 255), [190, 90, 1000, 550], 0)
        pygame.draw.rect(background, (0, 106, 195), [0, 77, 2000, 70], 0)
        pygame.draw.rect(background, (0, 106, 195), [10, 239, 10, 40], 0)

        # Draw UI elements
        screen.blit(newRBC_logo, (35, 90))
        screen.blit(rbc_top, (160, 81))
        screen.blit(newrbc_side, (-23, 290))
        screen.blit(rbc_tab, (0, 0))
        pygame.draw.rect(rbc_tab, (18, 18, 18), [273, 49, 500, 20], 0)
        url_text = fontURL.render("http://www.rbccroyal-bank.com/person.al/login-page.html", True, (255, 255, 255))
        screen.blit(url_text, (277, 52))
        trans_text = font.render("Transaction History", True, (0, 0, 40))
        request = fontminibold.render("Please download the transaction history of your", True, (0, 0, 40))
        request2 = fontminibold.render("account to check for any malicious activities.", True, (0, 0, 40))
        screen.blit(trans_text, (22, 250))
        screen.blit(request, (400, 220))
        screen.blit(request2, (400, 260))
        screen.blit(newzip, (480, 380))
        zip_name = fontURL.render("history.zip", True, (0, 0, 40))
        screen.blit(zip_name, (508, 500))
        screen.blit(newdownload, (680, 400))

        # Taskbar icons
        pygame.draw.rect(screen, (0, 0, 0), [0, 670, 1280, 75], 0)
        pygame.draw.rect(screen, (60, 60, 60), [493, 671, 45, 45], 0)
        pygame.draw.rect(screen, (34, 166, 242), [493, 717, 45, 10], 0)
        screen.blit(newSetting, (600, 678))
        screen.blit(newChrome, (495, 675))
        screen.blit(winsearch, (0, 670))
        screen.blit(newGmail, (550, 682))

        # Draw the download button with the new size
        download_button_rect.width = button_width
        download_button_rect.height = button_height
        screen.blit(newdownload, (680, 400))

        # Draw sliding notification (now it's the larger image)
        if sliding_started:
            screen.blit(newvirus_notification, (notification_x, notification_y))  # Draw the notification image at the new position

        # Update display
        pygame.display.flip()
        pygame.time.Clock().tick(60)


    
def scene4(screen, background):
    background.fill((240, 240, 240))

    # Font definitions
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 25)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontmini = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 15)
    fontminibold = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 18)
    fontminibolddate = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 15)
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 28)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontsmallest = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 16)
    fontboldsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 16)
    
    # Load images and fonts (same as before)
    rbc_logo = pygame.image.load("Images/rbc_logo.png")
    newrbc_logo = pygame.transform.scale(rbc_logo, (110, 110))
    rbc_top = pygame.image.load("Images/rbc_top.png")
    rbc_wall = pygame.image.load("Images/rbc_wall.png")
    newrbc_wall = pygame.transform.scale(rbc_wall, (476, 463))
    rbc_side = pygame.image.load("Images/rbc_side.png")
    newrbc_side = pygame.transform.scale(rbc_side, (230, 350))
    rbc_tab = pygame.image.load("Images/rbc_tab.png")
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
    objective3 = fontboldsmaller.render('Type to sign in to your bank account!', True, (0,0,40))

    #Icons Resized
    newRecy = pygame.transform.scale(recy,(50,50))
    newChrome = pygame.transform.scale(chrome,(40,40))
    newGmail = pygame.transform.scale(gmail,(32,25))
    newAdobe = pygame.transform.scale(adobe,(43,43))
    Newthispc = pygame.transform.scale(thispc,(43,43))
    Newfileex = pygame.transform.scale(fileex,(43,43))
    newGmail1 = pygame.transform.scale(gmail1,(41,31))
    newSetting = pygame.transform.scale(setting,(35,31))




    pygame.draw.rect(background, (0, 0, 0), [0, 670, 1280, 75], 0)

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

    pygame.draw.rect(screen, (60, 60, 60), [493, 671, 45, 45], 0)
    pygame.draw.rect(screen, (34, 166, 242), [493, 717, 45, 10], 0)

    screen.blit(newSetting,(600,678))
    screen.blit(newChrome,(495,675))
    screen.blit(winsearch,(0,670))
    screen.blit(newGmail,(550,682))

    pygame.draw.rect(screen, (173, 216, 230), [286, 466, 300, 50], 0)
    screen.blit(objective3, (286,482))
    

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
                    if user_input[current_field]:
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

        pygame.draw.rect(screen, (240, 240, 240), [870, 200, 300, 40], 0)  # Email box
        pygame.draw.rect(screen, (240, 240, 240), [870, 310, 300, 40], 0)  # Password box
        pygame.draw.rect(screen, (240, 240, 240), [870, 420, 300, 40], 0)  # PIN box
        pygame.draw.rect(screen, (240, 240, 240), [870, 530, 300, 40], 0)  # SSN box

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
    global pageNumber

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

        #taskbar
    pygame.draw.rect(background, (0, 0, 0), [0, 670, 1280, 75], 0)
    
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
    pygame.draw.rect(background, (255, 255, 255), [234, 76, 950, 570], 0)
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

    screen.blit(newSetting,(600,678))
    screen.blit(newChrome,(495,675))
    screen.blit(winsearch,(0,670))
    pygame.draw.rect(screen, (60, 60, 60), [543, 670, 45, 45], 0)
    pygame.draw.rect(screen, (34, 166, 242), [543, 717, 45, 10], 0)
    screen.blit(newGmail,(550,682))

    pygame.draw.line(screen, (0, 0, 255), (346, 466), (717, 466), 2)

sound_time = 0

def scene2(screen, background):
    #background
    background.fill((240, 240, 240))
    global pageNumber
    
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
    objective2 = fontboldsmaller.render('You have a new email! Click to open.', True, (0,0,40))
    Newcompose_logo = pygame.transform.scale(compose_logo,(38,35))

    Newstarred_logo = pygame.transform.scale(starred_logo,(28,25))
    Newimportant_logo = pygame.transform.scale(important_logo,(23,21))
    Newsent_logo = pygame.transform.scale(sent_logo,(30,30))
    newBack = pygame.transform.scale(back,(100,50))
    Newspam_logo = pygame.transform.scale(spam_logo,(43,40))

    

    #taskbar
    pygame.draw.rect(background, (0, 0, 0), [0, 670, 1280, 75], 0)



    
    
    
    
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
    screen.blit(newSetting,(600,678))
    screen.blit(newChrome,(495,675))
    screen.blit(winsearch,(0,670))
    pygame.draw.rect(screen, (60, 60, 60), [543, 670, 45, 45], 0)
    pygame.draw.rect(screen, (34, 166, 242), [543, 717, 45, 10], 0)
    pygame.draw.rect(screen, (173, 216, 230), [523, 475, 300, 50], 0)
    screen.blit(objective2, (538,490))
    screen.blit(newGmail,(550,682))
    
   

def scene1(screen, background):
    
    background.fill((255, 255, 255))
    global pageNumber, sound_time

    #font and size
    font = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 28)
    fontsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 22)
    fontsmallest = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 16)
    fontboldsmaller = pygame.font.Font('C:\\Windows\\Fonts\\Arialbd.ttf', 16)

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
    objective1 = fontboldsmaller.render('Welcome, you have a new gmail notification! Click to open the app.', True, (0,0,40))
    
    #Audio
    windows_sound = pygame.mixer.Sound("Images/windows_on.mp3")

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
    pygame.draw.rect(screen, (173, 216, 230), [350, 0, 550, 50], 0)
    screen.blit(objective1, (373,20))
    sound_time += clock.get_time()
    if sound_time < 1:
        pygame.mixer.Sound.play(windows_sound)
    
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
pygame.display.set_caption('Cybersecurity Bank Email Scam: Exploring Phishing!')
background = pygame.Surface(size).convert()

click_sound = pygame.mixer.Sound("Images/click.mp3")

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
    check_on = False

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
    elif pageNumber == 6:
        scene6(screen, background)
    elif pageNumber == 7:
        scene7(screen, background)
    elif pageNumber == 8:
        scene8(screen, background)
    elif pageNumber == 9:
        scene9(screen, background)
    elif pageNumber == 10:
        scene10(screen, background)
    elif pageNumber == 11:
        scene11(screen, background)

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.Sound.play(click_sound)
            x, y = event.pos
            print(x, y)  # Debugging output for mouse click positions
            if x >= 549 and x <= 582 and y >= 680 and y <= 708 and pageNumber == 1:
                pageNumber = 2
            if x >= 19 and x <= 72 and y >= 313 and y <= 352 and pageNumber == 1:
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
            elif x >= 698 and x <= 905 and y >= 410 and y <= 460 and pageNumber == 5:
                pageNumber = 6
            elif x >= 1075 and x <= 1185 and y >= 565 and y <= 676 and pageNumber == 6:
                pageNumber = 7
            elif x >= 1200 and x <= 1259 and y >= 502 and y <= 561 and pageNumber == 7:
                pageNumber = 8
            elif x >= 9 and x <= 69 and y >= 501 and y <= 559 and pageNumber == 7:
                pageNumber = 6
            elif x >= 1200 and x <= 1259 and y >= 502 and y <= 561 and pageNumber == 8:
                pageNumber = 9
            elif x >= 9 and x <= 69 and y >= 501 and y <= 559 and pageNumber == 8:
                pageNumber = 7
            elif x >= 1142 and x <= 1200 and y >= 646 and y <= 703 and pageNumber == 9:
                pageNumber = 10
            elif x >= 74 and x <= 134 and y >= 645 and y <= 705 and pageNumber == 9:
                pageNumber = 8
            elif x >= 1139 and x <= 1202 and y >= 503 and y <= 565 and pageNumber == 10:
                pageNumber = 11
            elif x >= 75 and x <= 136 and y >= 503 and y <= 566 and pageNumber == 10:
                pageNumber = 9
            elif x >= 119 and x <= 221 and y >=589  and y <= 692 and pageNumber == 11:
                pageNumber = 10




            




    pygame.display.update()