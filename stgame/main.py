import pygame
from datetime import datetime
import random
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
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("fstgame")

# sounds
# pygame.mixer.music.load("music/got.wav")
# pygame.mixer.music.play(-1,0.0,2000)
#player
player1 = Player(100,100,100,100,100)
anm = Anm(150,150,615,10,1)
Anmshot1 = Anmshot(10,10,anm.getx()+20,anm.gety()+20,0.5)

shots = []
anmshots = []
#load image
bgimage = pygame.image.load("images/galaxy.jpg")
resized_background = pygame.transform.scale(bgimage, (screen_w, screen_h))
image = pygame.image.load("images/fighter.png")
big_image = pygame.image.load("images/bgfighter.png")
# original_width, original_height = big_image.get_size()
resized_bigimage = pygame.transform.scale(big_image, (anm.getw(), anm.geth()))
bullet = pygame.image.load("images/bullet.png")
bullet2 = pygame.image.load("images/bullet2.png")
resized_image = pygame.transform.scale(image, (player1.getw(),player1.geth()))

#random number
numbers = [1,7,3,2,3,5,7,9,3,1,3,5,7,9,1,7,3,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,3,5,7,9,3,1,3,5,7,9,1,7,3,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]

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
shot1 = Shot(0,0,0,0,0)
run = True
while run:
    
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
                shot1 = Shot(20,20,player1.getx()+45,player1.gety(),1)
                shots.append(shot1)
            

    
    screen.fill((0, 0, 0))
    screen.blit(resized_background, (0,0))
    #draw player and anm
    # pygame.draw.rect(screen, "black", [player1.getx(),player1.gety(),player1.getw(),player1.geth()])
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
            shot.setspeed(shot.getspeed() * (-1))
            # shot.setspeed(shot.getspeed() + 0.2)
        if shot.gety() >= 720:
            shot.setspeed(shot.getspeed() * (-1))
            # shot.setspeed(shot.getspeed() + 0.2)
    #draw the anm shots
    current_time = datetime.now().time()
    seconds = int(current_time.strftime("%S"))
    milliseconds = current_time.microsecond // 1000
    if seconds % 2 == 0:
        # milliseconds * 500
        if random.choice(numbers) % 2 == 0:
            Anmshot1 = Anmshot(20,20,anm.getx()+65,anm.gety()+130,1)
            anmshots.append(Anmshot1)
    for anmshot in anmshots:
        anmshot.sety(anmshot.gety()+1)
        if anmshot.gety() > 720:
            anmshots.remove(anmshot)
        # pygame.draw.rect(screen, "green", [ anmshot.getx(), anmshot.gety(), anmshot.getw(), anmshot.geth()])
        resized_bullet2 = pygame.transform.scale(bullet2, (anmshot.getw(),anmshot.geth()))
        screen.blit(resized_bullet2, (anmshot.getx(),anmshot.gety()))

    
    

    pygame.display.update()
pygame.quit()



