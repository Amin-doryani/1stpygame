import pygame
from pygame.locals import *
from pygame import mixer
from player import Player

from shot import Shot
pygame.mixer.pre_init(44100,-16,2,512)

mixer.init()
pygame.init()

screen_w = 1280
screen_h = 720
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("fstgame")

#sounds
pygame.mixer.music.load("music/got.wav")
pygame.mixer.music.play(-1,0.0,2000)
# #player
player1 = Player(50,50,100,100,100)
shots = []

run = True
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
                shot1 = Shot(10,10,player1.getx()+20,player1.gety(),0.5)
                shots.append(shot1)
            

    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, "red", [player1.getx(),player1.gety(),player1.getw(),player1.geth()])
    # if shot1:
    #     pygame.draw.rect(screen, "white", [shot1.getx(),shot1.gety(),shot1.getw(),shot1.geth()])
    #     shot1.sety(shot1.gety() - shot1.getspeed() )
    for shot in shots:
        pygame.draw.rect(screen, "white", [shot.getx(),shot.gety(),shot.getw(),shot.geth()])
        shot.sety(shot.gety() - shot.getspeed())
        if shot.gety() <= 0:
            # shots.remove(shot)
            shot.setspeed(shot.getspeed() * (-1))
            # shot.setspeed(shot.getspeed() + 0.2)
        if shot.gety() >= 720:
            shot.setspeed(shot.getspeed() * (-1))
            # shot.setspeed(shot.getspeed() + 0.2)

    pygame.display.update()
pygame.quit()



