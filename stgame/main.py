import pygame
from datetime import datetime
import random
import time
from power import Power
from pygame.locals import *

from pygame import mixer
from player import Player
from anm import Anm
from anmshot import Anmshot

from shot import Shot
pygame.mixer.pre_init(44100,-16,2,512)

mixer.init()
pygame.init()

screen_w = 1280
screen_h = 720
pawerx = random_number = random.randint(100, 900)
pawery = random_number = random.randint(300, 600)
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("fstgame")
pawer1 = Power(20,20,100,700,0)
# sounds
pygame.mixer.music.load("music/got.wav")
pygame.mixer.music.play(-1,0.0,2000)
boom = pygame.mixer.Sound("music/boom.wav")
collect = pygame.mixer.Sound("music/collect.wav")
dot = pygame.mixer.Sound("music/dot.wav")

boom.set_volume(0.4)

# player
player1 = Player(100,100,100,100,100,20)

anm = Anm(150,150,615,24,1,10,0.1)
anmher = anm.getheart()
Anmshot1 = Anmshot(10,10,anm.getx()+20,anm.gety()+20,0.5)

shots = []
anmshots = []
#load image
bgimage = pygame.image.load("images/galaxy.jpg")
resized_background = pygame.transform.scale(bgimage, (screen_w, screen_h))
image = pygame.image.load("images/fighter.png")
big_image = pygame.image.load("images/bgfighter.png")
greenh = pygame.image.load("images/green.png")
resized_greenh = pygame.transform.scale(greenh, (40,40))
# original_width, original_height = big_image.get_size()
resized_bigimage = pygame.transform.scale(big_image, (anm.getw(), anm.geth()))
bullet = pygame.image.load("images/bullet.png")
bullet_bom = pygame.image.load("images/bullet1bom.png")
bullet2 = pygame.image.load("images/bullet2.png")
resized_image = pygame.transform.scale(image, (player1.getw(),player1.geth()))

#random number
numbers = [1,7,3,2,3,5,7,9,3,1,3,5,7,9,1,7,3,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,3,5,7,9,3,1,3,5,7,9,1,7,3,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
run2 = False
## change the player Y
def changeplayer_y(player,x):
    if player.gety()>0 and x>0 :
        player.sety(player.gety()-(player.getspeed())*x)
    if (player.gety()-(player.getspeed())*x)< screen_h - player.geth() and x < 0:
        player.sety(player.gety()-(player.getspeed())*x)
   ## END
## change the player X
def changeplayer_x(player,x) :
    if player.getx() > 0  and  x>0:
        player.setx(player.getx()-(player.getspeed())*x)
    if x < 0 and (player.getx()-(player.getspeed())*x) < screen_w - player.getw():
        player.setx(player.getx()-(player.getspeed())*x)
## END
# shot1 = Shot(0,0,0,0,0)
run = True 
while run:
    if player1.gett() == 0:
        run =False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # player1.sety(player1.gety()-10)
                changeplayer_y(player1,1)
            if event.key == pygame.K_DOWN:
                changeplayer_y(player1,-1)
            if event.key == pygame.K_LEFT:
                changeplayer_x(player1,1)
            if event.key == pygame.K_RIGHT:
                changeplayer_x(player1,-1)
            if event.key == pygame.K_SPACE:
                shot1 = Shot(20,20,player1.getx()+45,player1.gety(),1,100,0)
                shots.append(shot1)
            

    
    screen.fill((0, 0, 0))
    screen.blit(resized_background, (0,0))
    var2 = 10
    for ff in range(player1.gett()):
        pygame.draw.rect(screen, "green", [((screen_w/2) - 100)+var2,700,10,10])
        var2 +=10
    #draw power
    if pawer1.getlived() > 0:
        # print("yes")
        # pygame.draw.rect(screen, "green", [pawerx,pawery,20,20])
        screen.blit(resized_greenh, (pawerx,pawery))
        pawer1.setlived(pawer1.getlived()-1)
    if pawer1.getlived() > 0 and ((pawerx>player1.getx() and pawerx<(player1.getx()+100)) and (pawery>player1.gety() and pawery < player1.gety() +100)):
        pawer1.setlived(0)
        collect.play()
        player1.sett(player1.gett()+5)
    #draw player and anm
    pygame.draw.rect(screen, "black", [20,10,104,20],2)
    var = 10
    i = 1
    if anm.getheart() > 0:
        pygame.draw.rect(screen, "red", [20+2,10+2,10,16])
    else:
        
        anmher +=5
        anm.setheart(anmher)
        anm.setspd(anm.getspd()+0.1)
          
        anm.setx(615)
        anm.sety(24)
        anm.setspeed(anm.getspeed()*-1)
        numbers.append(2)
        pawer1.setlived(2000)
        pawerx = random_number = random.randint(100, 900)
        pawery = random_number = random.randint(300, 600)
        # pawer1 = Power(20,20,100,700,100)nionnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        
        # screen.fill((0, 0, 0))
        # screen.blit(resized_background, (0,0))
        # time.sleep(1)
        continue
    if anm.getheart() >= 100:
        del(anm)
        run = False
        screen.fill((0, 0, 0))
        run2 = True
        break 
    for i in range(anm.getheart()):
        pygame.draw.rect(screen, "red", [20+2+var,10+2,10,16])
        var +=10
    screen.blit(resized_image, (player1.getx(),player1.gety()))
    anm.chnagepos()
    # pygame.draw.rect(screen, "blue", [anm.getx(),anm.gety(),anm.getw(),anm.geth()])
    screen.blit(resized_bigimage, (anm.getx(),anm.gety()))
    

    for shot in shots:
        # pygame.draw.rect(screen, "black", [shot.getx(),shot.gety(),shot.getw(),shot.geth()])
        resized_bullet = pygame.transform.scale(bullet, (shot.getw(),shot.geth()))
        screen.blit(resized_bullet, (shot.getx(),shot.gety()))
        shot.sety(shot.gety() - shot.getspeed())
        if shot.gety() <= 0:
            shots.remove(shot)
            continue
        if shot.gety() < (anm.gety() + anm.geth()) and  (shot.getx() < (anm.getx() + anm.getw()) and shot.getx() > anm.getx()):
            if shot.getadded() == 0:
                shot.setw(shot.getw()*2)
                shot.seth(shot.geth()*2)
                shot.setadded(1)
                

            resized_bullet = pygame.transform.scale(bullet_bom, (shot.getw(),shot.geth()))
            screen.blit(resized_bullet, (shot.getx(),shot.gety()))

            if shot.getlived() == 100:
                boom.play()
            if shot.getlived() > 0:
                shot.setlived(shot.getlived() - 1)
            else:
                anm.setheart(anm.getheart()-1)
                shots.remove(shot)
        
        
            # shot.setspeed(shot.getspeed() * (-1))
            # shot.setspeed(shot.getspeed() + 0.2)
        # if shot.gety() >= 720:
        #     shot.setspeed(shot.getspeed() * (-1))
        #     # shot.setspeed(shot.getspeed() + 0.2)
    #draw the anm shots
    current_time = datetime.now().time()
    seconds = int(current_time.strftime("%S"))
    
    if seconds % 2 == 0:
        # milliseconds * 500
        if random.choice(numbers) % 2 == 0:
            Anmshot1 = Anmshot(20,20,anm.getx()+65,anm.gety()+130,1)
            anmshots.append(Anmshot1)
    for anmshot in anmshots:
        anmshot.sety(anmshot.gety()+1)
        if anmshot.gety() > 720:
            anmshots.remove(anmshot)
            continue
        # pygame.draw.rect(screen, "green", [ anmshot.getx(), anmshot.gety(), anmshot.getw(), anmshot.geth()])
        if (anmshot.getx()>player1.getx() and anmshot.getx()< player1.getx()+100) and (anmshot.gety()>player1.gety() and anmshot.gety()< player1.gety()+100) and player1.gett()>0:
            player1.sett(player1.gett()-1)
            dot.play()
            anmshots.remove(anmshot)
        resized_bullet2 = pygame.transform.scale(bullet2, (anmshot.getw(),anmshot.geth()))
        screen.blit(resized_bullet2, (anmshot.getx(),anmshot.gety()))

    
    

    pygame.display.update()

pygame.quit()
mixer.init()
pygame.init()
screen_w = 1280
screen_h = 720 
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("fstgame") 
pygame.mixer.music.load("music/won.wav")
pygame.mixer.music.play(-1,0.0,2000)

bgimage2 = pygame.image.load("images/R.jpeg")
resized_background2 = pygame.transform.scale(bgimage2, (1280, 720))
while run2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run2 = False
    screen.fill((0, 0, 0))
    screen.blit(resized_background2, (0,0)) 
    pygame.display.update()
pygame.quit()



