import pygame , sys
from classes import  *
pygame.init()

import random

#GLOBAL
lives=3
SIZE = (840, 750)
Game=True
X = 37
Y = 37
VEL=3
INITX = 10
INITY = 10
CLR1=(0,0,255)
CLR2=(255,255,0)
CLR3=(255,0,0)
FPS=50
totalframes=0
#GLOBAL

screen = pygame.display.set_mode(SIZE,0,32)
clock=pygame.time.Clock()

#SPRITES
pac=User("PACr.png","PACl.png","PACdownleft.png","PACupright.png",
        "pacright.png","pacleft.png","pacdownl.png","pacupr.png",INITX+4*X+3,INITY+18*Y+6,30,30,1)

bots=[Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+7*X,INITY+8*Y,30,30,0)
    ,Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+7*X,INITY+9*Y,30,30,0)
    ,Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+8*X,INITY+9*Y,30,30,0)
    ,Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+9*X,INITY+9*Y,30,30,0)
    ,Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+8*X,INITY+9*Y,30,30,0)
    ,Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+9*X,INITY+8*Y,30,30,0)
    ]

#SPIRTES

#EXTRA SPRITES
SuperRec=[RecSprite(CLR1,(INITX,INITY,17*X,19*Y))]
CenterRec= RecSprite(CLR1, (INITX+6*X,INITY+8*Y,5*X,3*Y))
AllRec=[
        RecSprite( CLR1, (INITX+1*X,INITY+1*Y,2*X,2*Y)),
        RecSprite( CLR1, (INITX+4*X,INITY+1*Y,3*X,2*Y)),RecSprite(CLR1, (INITX+12*X,INITY+9*Y,1*X,3*Y)),
        RecSprite(CLR1, (INITX+14*X,INITY+1*Y,2*X,2*Y)),RecSprite(CLR1, (INITX+10*X,INITY+1*Y,3*X,2*Y)),
        RecSprite(CLR1, (INITX+1*X,INITY+4*Y,2*X,1*Y)),RecSprite(CLR1, (INITX+12*X,INITY+4*Y,1*X,4*Y)),
        RecSprite(CLR1, (INITX+8*X,INITY+5*Y,1*X,2*Y)),RecSprite(CLR1, (INITX+4*X,INITY+4*Y,1*X,4*Y)),
        RecSprite(CLR1, (INITX+14*X,INITY+4*Y,2*X,1*Y)),RecSprite(CLR1, (INITX+6*X,INITY+4*Y,5*X,1*Y)),
        RecSprite(CLR1, (INITX+8*X,INITY+0*Y,1*X,3*Y)),RecSprite(CLR1, (INITX+5*X,INITY+6*Y,2*X,1*Y)),
        RecSprite(CLR1, (INITX+10*X,INITY+6*Y,2*X,1*Y)),RecSprite(CLR1, (INITX+4*X,INITY+9*Y,1*X,3*Y)),

        RecSprite(CLR1, (INITX+6*X,INITY+12*Y,5*X,1*Y)),RecSprite(CLR1,(INITX+8*X,INITY+13*Y,1*X,1*Y)),
        RecSprite(CLR1,(INITX+1*X,INITY+13*Y,2*X,1*Y)),RecSprite(CLR1,(INITX+0*X,INITY+15*Y,1*X,1*Y)),
        RecSprite(CLR1,(INITX+2*X,INITY+14*Y,1*X,2*Y)),RecSprite(CLR1,(INITX+1*X,INITY+17*Y,6*X,1*Y)),
        RecSprite(CLR1,(INITX+10*X,INITY+17*Y,6*X,1*Y)),RecSprite(CLR1,(INITX+4*X,INITY+16*Y,1*X,1*Y)),
        RecSprite(CLR1,(INITX+4*X,INITY+13*Y,1*X,1*Y)),RecSprite(CLR1,(INITX+8*X,INITY+15*Y,1*X,3*Y)),
        RecSprite(CLR1,(INITX+12*X,INITY+16*Y,1*X,1*Y)),RecSprite(CLR1,(INITX+4*X,INITY+14*Y,3*X,1*Y)),
        RecSprite(CLR1,(INITX+6*X,INITY+16*Y,1*X,1*Y)),RecSprite(CLR1,(INITX+10*X,INITY+16*Y,1*X,1*Y)),
        RecSprite(CLR1,(INITX+16*X,INITY+15*Y,1*X,1*Y)),RecSprite(CLR1,(INITX+14*X,INITY+13*Y,1*X,3*Y)),
        RecSprite(CLR1,(INITX+15*X,INITY+13*Y,1*X,1*Y)),RecSprite(CLR1,(INITX+12*X,INITY+13*Y,1*X,2*Y)),
        RecSprite(CLR1,(INITX+10*X,INITY+14*Y,2*X,1*Y)),

        RecSprite(CLR3,(INITX+0*X,INITY+6*Y+3,3*X-3,6*Y-3),1),RecSprite(CLR3,(INITX+14*X+3,INITY+6*Y+3,3*X-3,6*Y-3),1),

        RecSprite(CLR3,(INITX-X/3,INITY-Y/3,17*X+X/3,Y/3)),RecSprite(CLR3,(INITX-X/3,INITY+19*Y,17*X+2*X/3,Y/3)),
        RecSprite(CLR3,(INITX+17*X,INITY-Y/3,X/3,19*Y+Y/3,)),RecSprite(CLR3,(INITX-X/3,INITY,X/3,19*Y)),

        RecSprite(CLR3, (INITX+7*X,INITY+10*Y,4*X,1*Y)),RecSprite(CLR3, (INITX+6*X,INITY+8*Y,1*X,3*Y)),
        RecSprite(CLR3, (INITX+8*X,INITY+8*Y,1*X,1*Y)),RecSprite(CLR3, (INITX+10*X,INITY+8*Y,1*X,2*Y))
        ]

AllPoints=[]
for i in range(1,18):
    for j in range(1,20):
        p=Points(INITX+(i-.5)*X,INITY+(j-.5)*Y,CLR2)
        AllPoints.append(p)
ImpPoints=[]
for point in AllPoints:
    if(point.is_point_in_rec(AllRec)):
        ImpPoints.append(point)

#EXTRA SPRITES

#HELPER FUNC
def board():
    for rec in AllRec:
        rec.draw()
    for point in ImpPoints:
        point.draw()

def collect(points,sprite):
        for point in points:
            if( sprite.rect.x < point.x < sprite.rect.x + sprite.rect.width and sprite.rect.y < point.y < sprite.rect.y + sprite.rect.height ):
                point.visible=False

def UltimateCollision(pac,bots):
    for bot in bots:
        if( bot.rect.x < pac.rect.x+pac.rect.width/2 < bot.rect.x + bot.rect.width and bot.rect.y < pac.rect.y+pac.rect.height/2  < bot.rect.y + bot.rect.height ):
            return True
    return False

def Win(points):
    font = pygame.font.SysFont(None, 36)
    score=0
    for point in points:
        if(point.visible):
            score+=1
    tf=0
    while(score==0 and tf!=FPS*3):
        tf+=1
        text1 = font.render("YOU WIN", 1, (255, 100, 100))
        text1pos = text1.get_rect()
        text1pos.center=(INITX+20*X,INITY+10*Y)
        screen.blit(text1, text1pos)
        pygame.display.flip()
        clock.tick(FPS)
    if(score==0):
        return True
    else :
        return False

def Livescore_disp(lives,points,clr=(255, 255, 0)):
    font = pygame.font.SysFont(None, 36)

    text2 = font.render("LIVES :", 1, clr)
    text2pos = text2.get_rect()
    text2pos.center=(INITX+2*X-20,INITY+9*Y-15)
    screen.blit(text2, text2pos)

    text4 = font.render(str(lives), 1, clr)
    text4pos = text2.get_rect()
    text4pos.center=(INITX+2*X+10,INITY+9*Y+15)
    screen.blit(text4, text4pos)

    score=0
    for point in points:
        if( not point.visible):
            score+=1
    text1 = font.render("SCORE:", 1, (255, 255, 0))
    text1pos = text1.get_rect()
    text1pos.center=(INITX+16*X-15,INITY+9*Y-15)
    screen.blit(text1, text1pos)

    text3 = font.render(str(score), 1, (255, 255, 0))
    text3pos = text3.get_rect()
    text3pos.center=(INITX+16*X-15,INITY+9*Y+15)
    screen.blit(text3, text3pos)

#HELPER FUNC
while Game:
    #PROCESS
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        elif event.type== pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                if( not pac.is_collision(AllRec)) :
                    pac.velx=-VEL
                else :
                    pac.velx=0
                pac.state=1

            elif event.key== pygame.K_RIGHT:
                if( not pac.is_collision(AllRec)) :
                    pac.velx=VEL
                else :
                    pac.velx=0
                pac.state=0
            elif event.key== pygame.K_DOWN:
                if( not pac.is_collision(AllRec)) :
                    pac.vely=VEL
                else :
                    pac.vely=0
                pac.state=2
            elif event.key== pygame.K_UP:
                if( not pac.is_collision(AllRec)) :
                    pac.vely=-VEL
                else :
                    pac.vely=0
                pac.state=3
        elif event.type== pygame.KEYUP:
            pac.velx=0
            pac.vely=0
    #PROCESS

    #AI
    bots[0].arbit(AllRec)
    bots[0].tick(bots[0].rect.x,bots[0].rect.y,bots[0].rect.width,bots[0].rect.height)

    bots[1].arbit(AllRec)
    bots[1].tick(bots[1].rect.x,bots[1].rect.y,bots[1].rect.width,bots[1].rect.height)

    bots[2].arbit(AllRec)
    bots[2].tick(bots[2].rect.x,bots[2].rect.y,bots[2].rect.width,bots[2].rect.height)

    bots[3].arbit(AllRec)
    bots[3].tick(bots[3].rect.x,bots[3].rect.y,bots[3].rect.width,bots[3].rect.height)

    bots[4].arbit(AllRec)
    bots[4].tick(bots[4].rect.x,bots[4].rect.y,bots[4].rect.width,bots[4].rect.height)

    bots[5].arbit(AllRec)
    bots[5].tick(bots[5].rect.x,bots[5].rect.y,bots[5].rect.width,bots[5].rect.height)

    bots[0].update()
    bots[1].update()
    bots[2].update()
    bots[3].update()
    bots[4].update()
    bots[5].update()

    #AI
    JGame=False
    JGame=UltimateCollision(pac,bots)
    GGame=Win(ImpPoints)

    if(JGame):
        lives-=1
        tf=0
        if(lives!=0):
            pac.rect.x=INITX+4*X+3
            pac.rect.y=INITY+18*Y+6
        while(tf != 3*FPS):
            tf+=1
            if(lives==0):
                font = pygame.font.SysFont(None, 36)
                text1 = font.render("GAME OVER", 1, (255, 100, 100))
                text1pos = text1.get_rect()
                text1pos.center=(INITX+20*X,INITY+10*Y)
                screen.blit(text1, text1pos)
            pygame.draw.rect(screen ,(0,0,0),(INITX+1*X-10,INITY+9*Y-15,1*X,1*Y+10))
            Livescore_disp(lives,ImpPoints,(0,255,0))
            pygame.display.flip()
            clock.tick(FPS)
    if(GGame or lives==0):
        Game=False

    #USER
    totalframes+=1
    pac.update()
    pac.is_collision(AllRec)
    collect(ImpPoints,pac)

    #USER

    #DRAW
    if(totalframes == FPS/5):
        totalframes=0
        pac.tick(pac.rect.x,pac.rect.y,pac.rect.width,pac.rect.height)

    screen.fill((0,0,0))
    board()
    User.pacs.draw(screen)
    Com.bots.draw(screen)
    Livescore_disp(lives,ImpPoints)
    pygame.display.flip()
    #DRAW

    clock.tick(FPS)


import pygame , sys
from classes import  *
pygame.init()

import random

#GLOBAL
lives=3
SIZE = (840, 750)
Game=True
X = 37
Y = 37
VEL=3
INITX = 10
INITY = 10
CLR1=(0,0,255)
CLR2=(255,255,0)
CLR3=(255,0,0)
FPS=50
totalframes=0
#GLOBAL

screen = pygame.display.set_mode(SIZE,0,32)
clock=pygame.time.Clock()

#SPRITES
pac=User("PACr.png","PACl.png","PACdownleft.png","PACupright.png",
        "pacright.png","pacleft.png","pacdownl.png","pacupr.png",INITX+4*X+3,INITY+18*Y+6,30,30,1)

bots=[Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+7*X,INITY+8*Y,30,30,0)
    ,Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+7*X,INITY+9*Y,30,30,0)
    ,Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+8*X,INITY+9*Y,30,30,0)
    ,Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+9*X,INITY+9*Y,30,30,0)
    ,Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+8*X,INITY+9*Y,30,30,0)
    ,Com("angry bot30.png","angry bot30left.png","eatable bot30.png",INITX+9*X,INITY+8*Y,30,30,0)
    ]

#SPIRTES

#EXTRA SPRITES
SuperRec=[RecSprite(CLR1,(INITX,INITY,17*X,19*Y))]
CenterRec= RecSprite(CLR1, (INITX+6*X,INITY+8*Y,5*X,3*Y))
AllRec=[
        RecSprite( CLR1, (INITX+1*X,INITY+1*Y,2*X,2*Y)),
        RecSprite( CLR1, (INITX+4*X,INITY+1*Y,3*X,2*Y)),RecSprite(CLR1, (INITX+12*X,INITY+9*Y,1*X,3*Y)),
        RecSprite(CLR1, (INITX+14*X,INITY+1*Y,2*X,2*Y)),RecSprite(CLR1, (INITX+10*X,INITY+1*Y,3*X,2*Y)),
        RecSprite(CLR1, (INITX+1*X,INITY+4*Y,2*X,1*Y)),RecSprite(CLR1, (INITX+12*X,INITY+4*Y,1*X,4*Y)),
        RecSprite(CLR1, (INITX+8*X,INITY+5*Y,1*X,2*Y)),RecSprite(CLR1, (INITX+4*X,INITY+4*Y,1*X,4*Y)),
        RecSprite(CLR1, (INITX+14*X,INITY+4*Y,2*X,1*Y)),RecSprite(CLR1, (INITX+6*X,INITY+4*Y,5*X,1*Y)),
        RecSprite(CLR1, (INITX+8*X,INITY+0*Y,1*X,3*Y)),RecSprite(CLR1, (INITX+5*X,INITY+6*Y,2*X,1*Y)),
        RecSprite(CLR1, (INITX+10*X,INITY+6*Y,2*X,1*Y)),RecSprite(CLR1, (INITX+4*X,INITY+9*Y,1*X,3*Y)),

        RecSprite(CLR1, (INITX+6*X,INITY+12*Y,5*X,1*Y)),RecSprite(CLR1,(INITX+8*X,INITY+13*Y,1*X,1*Y)),
        RecSprite(CLR1,(INITX+1*X,INITY+13*Y,2*X,1*Y)),RecSprite(CLR1,(INITX+0*X,INITY+15*Y,1*X,1*Y)),
        RecSprite(CLR1,(INITX+2*X,INITY+14*Y,1*X,2*Y)),RecSprite(CLR1,(INITX+1*X,INITY+17*Y,6*X,1*Y)),
        RecSprite(CLR1,(INITX+10*X,INITY+17*Y,6*X,1*Y)),RecSprite(CLR1,(INITX+4*X,INITY+16*Y,1*X,1*Y)),
        RecSprite(CLR1,(INITX+4*X,INITY+13*Y,1*X,1*Y)),RecSprite(CLR1,(INITX+8*X,INITY+15*Y,1*X,3*Y)),
        RecSprite(CLR1,(INITX+12*X,INITY+16*Y,1*X,1*Y)),RecSprite(CLR1,(INITX+4*X,INITY+14*Y,3*X,1*Y)),
        RecSprite(CLR1,(INITX+6*X,INITY+16*Y,1*X,1*Y)),RecSprite(CLR1,(INITX+10*X,INITY+16*Y,1*X,1*Y)),
        RecSprite(CLR1,(INITX+16*X,INITY+15*Y,1*X,1*Y)),RecSprite(CLR1,(INITX+14*X,INITY+13*Y,1*X,3*Y)),
        RecSprite(CLR1,(INITX+15*X,INITY+13*Y,1*X,1*Y)),RecSprite(CLR1,(INITX+12*X,INITY+13*Y,1*X,2*Y)),
        RecSprite(CLR1,(INITX+10*X,INITY+14*Y,2*X,1*Y)),

        RecSprite(CLR3,(INITX+0*X,INITY+6*Y+3,3*X-3,6*Y-3),1),RecSprite(CLR3,(INITX+14*X+3,INITY+6*Y+3,3*X-3,6*Y-3),1),

        RecSprite(CLR3,(INITX-X/3,INITY-Y/3,17*X+X/3,Y/3)),RecSprite(CLR3,(INITX-X/3,INITY+19*Y,17*X+2*X/3,Y/3)),
        RecSprite(CLR3,(INITX+17*X,INITY-Y/3,X/3,19*Y+Y/3,)),RecSprite(CLR3,(INITX-X/3,INITY,X/3,19*Y)),

        RecSprite(CLR3, (INITX+7*X,INITY+10*Y,4*X,1*Y)),RecSprite(CLR3, (INITX+6*X,INITY+8*Y,1*X,3*Y)),
        RecSprite(CLR3, (INITX+8*X,INITY+8*Y,1*X,1*Y)),RecSprite(CLR3, (INITX+10*X,INITY+8*Y,1*X,2*Y))
        ]

AllPoints=[]
for i in range(1,18):
    for j in range(1,20):
        p=Points(INITX+(i-.5)*X,INITY+(j-.5)*Y,CLR2)
        AllPoints.append(p)
ImpPoints=[]
for point in AllPoints:
    if(point.is_point_in_rec(AllRec)):
        ImpPoints.append(point)

#EXTRA SPRITES

#HELPER FUNC
def board():
    for rec in AllRec:
        rec.draw()
    for point in ImpPoints:
        point.draw()

def collect(points,sprite):
        for point in points:
            if( sprite.rect.x < point.x < sprite.rect.x + sprite.rect.width and sprite.rect.y < point.y < sprite.rect.y + sprite.rect.height ):
                point.visible=False

def UltimateCollision(pac,bots):
    for bot in bots:
        if( bot.rect.x < pac.rect.x+pac.rect.width/2 < bot.rect.x + bot.rect.width and bot.rect.y < pac.rect.y+pac.rect.height/2  < bot.rect.y + bot.rect.height ):
            return True
    return False

def Win(points):
    font = pygame.font.SysFont(None, 36)
    score=0
    for point in points:
        if(point.visible):
            score+=1
    tf=0
    while(score==0 and tf!=FPS*3):
        tf+=1
        text1 = font.render("YOU WIN", 1, (255, 100, 100))
        text1pos = text1.get_rect()
        text1pos.center=(INITX+20*X,INITY+10*Y)
        screen.blit(text1, text1pos)
        pygame.display.flip()
        clock.tick(FPS)
    if(score==0):
        return True
    else :
        return False

def Livescore_disp(lives,points,clr=(255, 255, 0)):
    font = pygame.font.SysFont(None, 36)

    text2 = font.render("LIVES :", 1, clr)
    text2pos = text2.get_rect()
    text2pos.center=(INITX+2*X-20,INITY+9*Y-15)
    screen.blit(text2, text2pos)

    text4 = font.render(str(lives), 1, clr)
    text4pos = text2.get_rect()
    text4pos.center=(INITX+2*X+10,INITY+9*Y+15)
    screen.blit(text4, text4pos)

    score=0
    for point in points:
        if( not point.visible):
            score+=1
    text1 = font.render("SCORE:", 1, (255, 255, 0))
    text1pos = text1.get_rect()
    text1pos.center=(INITX+16*X-15,INITY+9*Y-15)
    screen.blit(text1, text1pos)

    text3 = font.render(str(score), 1, (255, 255, 0))
    text3pos = text3.get_rect()
    text3pos.center=(INITX+16*X-15,INITY+9*Y+15)
    screen.blit(text3, text3pos)

#HELPER FUNC
while Game:
    #PROCESS
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        elif event.type== pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                if( not pac.is_collision(AllRec)) :
                    pac.velx=-VEL
                else :
                    pac.velx=0
                pac.state=1

            elif event.key== pygame.K_RIGHT:
                if( not pac.is_collision(AllRec)) :
                    pac.velx=VEL
                else :
                    pac.velx=0
                pac.state=0
            elif event.key== pygame.K_DOWN:
                if( not pac.is_collision(AllRec)) :
                    pac.vely=VEL
                else :
                    pac.vely=0
                pac.state=2
            elif event.key== pygame.K_UP:
                if( not pac.is_collision(AllRec)) :
                    pac.vely=-VEL
                else :
                    pac.vely=0
                pac.state=3
        elif event.type== pygame.KEYUP:
            pac.velx=0
            pac.vely=0
    #PROCESS

    #AI
    bots[0].arbit(AllRec)
    bots[0].tick(bots[0].rect.x,bots[0].rect.y,bots[0].rect.width,bots[0].rect.height)

    bots[1].arbit(AllRec)
    bots[1].tick(bots[1].rect.x,bots[1].rect.y,bots[1].rect.width,bots[1].rect.height)

    bots[2].arbit(AllRec)
    bots[2].tick(bots[2].rect.x,bots[2].rect.y,bots[2].rect.width,bots[2].rect.height)

    bots[3].arbit(AllRec)
    bots[3].tick(bots[3].rect.x,bots[3].rect.y,bots[3].rect.width,bots[3].rect.height)

    bots[4].arbit(AllRec)
    bots[4].tick(bots[4].rect.x,bots[4].rect.y,bots[4].rect.width,bots[4].rect.height)

    bots[5].arbit(AllRec)
    bots[5].tick(bots[5].rect.x,bots[5].rect.y,bots[5].rect.width,bots[5].rect.height)

    bots[0].update()
    bots[1].update()
    bots[2].update()
    bots[3].update()
    bots[4].update()
    bots[5].update()

    #AI
    JGame=False
    JGame=UltimateCollision(pac,bots)
    GGame=Win(ImpPoints)

    if(JGame):
        lives-=1
        tf=0
        if(lives!=0):
            pac.rect.x=INITX+4*X+3
            pac.rect.y=INITY+18*Y+6
        while(tf != 3*FPS):
            tf+=1
            if(lives==0):
                font = pygame.font.SysFont(None, 36)
                text1 = font.render("GAME OVER", 1, (255, 100, 100))
                text1pos = text1.get_rect()
                text1pos.center=(INITX+20*X,INITY+10*Y)
                screen.blit(text1, text1pos)
            pygame.draw.rect(screen ,(0,0,0),(INITX+1*X-10,INITY+9*Y-15,1*X,1*Y+10))
            Livescore_disp(lives,ImpPoints,(0,255,0))
            pygame.display.flip()
            clock.tick(FPS)
    if(GGame or lives==0):
        Game=False

    #USER
    totalframes+=1
    pac.update()
    pac.is_collision(AllRec)
    collect(ImpPoints,pac)

    #USER

    #DRAW
    if(totalframes == FPS/5):
        totalframes=0
        pac.tick(pac.rect.x,pac.rect.y,pac.rect.width,pac.rect.height)

    screen.fill((0,0,0))
    board()
    User.pacs.draw(screen)
    Com.bots.draw(screen)
    Livescore_disp(lives,ImpPoints)
    pygame.display.flip()
    #DRAW

    clock.tick(FPS)


