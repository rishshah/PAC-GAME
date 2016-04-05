import pygame
import random
SIZE = (840, 750)
BOTVEL=4
screen = pygame.display.set_mode(SIZE,0,32)

class User(pygame.sprite.Sprite):
    pacs=pygame.sprite.Group()

    def __init__(self,imgr,imgl,imgd,imgu,imgrs,imgls,imgds,imgus,x,y,width,height,state):
        pygame.sprite.Sprite.__init__(self)

        self.images=(imgr,imgl,imgd,imgu,imgrs,imgls,imgds,imgus)
        self.state=state

        self.image=pygame.image.load(self.images[self.state])
        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y=y
        self.rect.width=width
        self.rect.height=height

        self.velx=0
        self.vely=0

        User.pacs.add(self)

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

    def tick(self,x,y,width,height):
        User.pacs.remove(self)

        if(self.state<4):
            self.state+=4
        else:
            self.state-=4

        self.image= pygame.image.load(self.images[self.state])
        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y=y
        self.rect.width=width
        self.rect.height=height

        User.pacs.add(self)

    def is_collision(self,recs):
        l=False
        for rec in recs:
            l=rec.collision(self)
        return l

class Com(pygame.sprite.Sprite):
    bots=pygame.sprite.Group()

    def __init__(self,imgr,imgl,imgdumb,x,y,width,height,state):
        pygame.sprite.Sprite.__init__(self)

        self.images=(imgl,imgr,imgdumb)
        self.state=state

        self.image=pygame.image.load(self.images[self.state])
        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y=y
        self.rect.width=width
        self.rect.height=height

        self.velx=BOTVEL
        self.vely=0

        Com.bots.add(self)

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

    def is_collision(self,recs):
        l=False
        b=l
        for rec in recs:
            l=rec.collision(self)
            if(l):
                b=True
        return b

    def arbit(self,recs):
        xp=self.velx
        yp=self.vely
        if(self.is_collision(recs)):
            self.velx=(random.randint(0,2)-1)*BOTVEL
            if(self.velx==0):
                self.vely=(random.randint(0,2)-1)*BOTVEL
            else :
                self.vely=0
            while((self.vely==0 and self.velx==0) or (self.velx==xp and self.vely==yp) ):
                self.velx=(random.randint(0,2)-1)*BOTVEL
                if(self.velx==0):
                    self.vely=(random.randint(0,2)-1)*BOTVEL
                else:
                    self.vely=0
    def tick(self,x,y,width,height):
        Com.bots.remove(self)

        if(self.velx>0):
            self.state=1
        else:
            self.state=0

        self.image= pygame.image.load(self.images[self.state])
        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y=y
        self.rect.width=width
        self.rect.height=height

        Com.bots.add(self)

class RecSprite:

    def __init__(self,clr,(x,y,width,height),depth=0):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.clr=clr
        self.depth=depth

    def draw(self):
        pygame.draw.rect(screen ,self.clr,(self.x,self.y,self.width,self.height),self.depth)
    def is_out(self,p):
        if( self.x < p[0] < self.x + self.width and self.y < p[1] < self.y + self.height ):
            return False
        return True

    def collision(self,sprite):

        tl=[sprite.rect.x , sprite.rect.y]
        tr=[sprite.rect.x +sprite.rect.width , sprite.rect.y]
        bl=[sprite.rect.x , sprite.rect.y+sprite.rect.height]
        br=[sprite.rect.x +sprite.rect.width , sprite.rect.y+sprite.rect.height]

        TL= not self.is_out(tl)
        TR= not self.is_out(tr)
        BL= not self.is_out(bl)
        BR= not self.is_out(br)
        if(not(TL or BR or BL or TR)):
            return False

        if(TL and not( BR or BL or TR)):
            if(sprite.velx<0):
                sprite.rect.x=self.width+self.x
            elif(sprite.vely<0):
                sprite.rect.y=self.height+self.y
            sprite.velx=0
            sprite.vely=0
        elif(TR and not( BR or BL or TL)):
            if(sprite.velx>0):
                sprite.rect.x=self.x-sprite.rect.width
            elif(sprite.vely<0):
                sprite.rect.y=self.height+self.y
            sprite.velx=0
            sprite.vely=0
        elif(BL and not( BR or TL or TR)):
            if(sprite.velx<0):
                sprite.rect.x=self.width+self.x
            elif(sprite.vely>0):
                sprite.rect.y=self.y-sprite.rect.height
            sprite.velx=0
            sprite.vely=0
        elif(BR and not( TL or BL or TR)):
            if(sprite.velx>0):
                sprite.rect.x=self.x-sprite.rect.width
            elif(sprite.vely>0):
                sprite.rect.y=self.y-sprite.rect.height
            sprite.velx=0
            sprite.vely=0
        elif(TL and TR and not BL and not BR):
            sprite.vely=0
            sprite.rect.y=self.height+self.y
        elif(BL and BR and not TL and not TR):
            sprite.vely=0
            sprite.rect.y=self.y-sprite.rect.height
        elif(BR and TR and not TL and not BL):
            sprite.velx=0
            sprite.rect.x=self.x - sprite.rect.width
        elif(BL and TL and not TR and not BR):
            sprite.velx=0
            sprite.rect.x=self.x+self.width
        #sprite.update()
        return True

class Points:
    radius=4

    def __init__(self,x,y,clr):
        self.x=int(x)
        self.y=int(y)
        self.clr=clr
        self.visible=True

    def is_point_in_rec(self,recs):
        for rec in recs:
            if rec.x < self.x < rec.x+rec.width and rec.y < self.y < rec.y+rec.height :
                return False
        return True

    def draw(self):
        if(self.visible):
            pygame.draw.circle(screen ,self.clr,(self.x,self.y),Points.radius)

