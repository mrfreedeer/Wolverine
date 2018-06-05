import pygame
import random
import math
random.seed(pygame.time.get_ticks())

ALTO=1000
ANCHO=1000
pygame.mixer.init(44100, -16, 2, 2048)


screensize = pygame.display.Info()
RESOLUTION = [screensize.current_w, screensize.current_h]
bglimit = 10
#Funciones

def recortarTorr(archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()
    matriz=[]
    spawn=[[0, 78, 87, 36], [0, 78, 87, 36], [178, 78, 87, 36], [267, 78, 87, 36], [356, 34, 87, 79],
            [445, 34, 87, 79], [534, 34, 87, 79], [624, 34, 87, 79], [713, 34, 87, 79]]
    shoot=[0, 194, 104, 79]

    spawnS=[]
    shootS=[]


    #Idle R-L
    for x in range(10):
        cuadro=fondo.subsurface(spawn[x])
        #cuadro=pygame.transform.scale(cuadro, (125, 125))
        #cuadro2=pygame.transform.flip(cuadro, True, False)
        #cuadro2=pygame.transform.scale(cuadro2, (125, 125))
        spawnS.append(cuadro)
        #idleL.append(cuadro2)
    cuadro=fondo.subsurface(shoot)
    shootS.append(cuadro)

    return spawnS, shootS


def recortarBala(archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()
    matriz=[]

    cuadro=fondo.subsurface(108, 201, 35, 11)
    matriz.append(cuadro)

    return matriz
    
matrizBala=recortarBala('lasers.png')
#Clases
class Turret(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.f=matriz
        self.image=self.f[0][0]
        self.rect=self.image.get_rect()
        self.indice=1
        self.rect.x=50
        self.rect.y=500
        self.accion=0
        self.dir = 'L'
        self._health = 100
        self.shoottimer = 50
        self.shoot = False

    def getHealth(self):
        return self._health

    def die(self):
        #ouch.play()
        channel4.play(blast)

    def update(self):
        #Idle R
        self.shoottimer -= 1
        if self.shoottimer < 0:
            self.shoot = True
            self.shoottimer = random.randrange(20,50)

        if self.shoot:
            self.accion=2
        else:
            self.accion=0
        if self.accion==0:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice > 2:
                self.indice=0
        #Idle L
        if self.accion==1:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice > 2:
                self.indice=0

        #1
        #Attack R
        if self.accion==2:
            if self.indice <=2:
                self.image = self.f[self.accion][self.indice]
                if self.indice==1:
                    shoot=Bala(matrizBala)
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 2:
                self.indice=0

        #Attack L
        if self.accion==3:
            if self.indice <=2:
                self.image = self.f[self.accion][self.indice]
                if self.indice==0:
                    self.rect.x+=85
                self.indice += 1
                if self.indice==1:
                    self.rect.x-=67
                if self.indice==2:
                    self.rect.x-=18

            #Es 7 normalmente
            if self.indice > 2:
                self.indice=0


class Bala (pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.f=matriz
        self.image=self.f[0]
        self.rect=self.image.get_rect()
        self.rect.x=50
        self.rect.y=450
        self.vel_x=15
        self.dir = 'R'
        self.lucky = random.randrange(0,2)
    def AIbullet(self, player, noplayers = 1, player2 = None):
        movedir = random.randrange(0,2)
        if noplayers == 1:
            selectplayer = player
        else:
            distanceplayer1 = math.fabs(player.rect.x-self.rect.x)+math.fabs(player.rect.y-self.rect.y)
            distanceplayer2 = math.fabs(player2.rect.x-self.rect.x)+math.fabs(player2.rect.y-self.rect.y)
            if distanceplayer1 > distanceplayer2:
                selectplayer = player2
            else:
                selectplayer = player
        if movedir:
            if self.rect.y - selectplayer.rect.y > 10:
                self.rect.y -= 4
            elif self.rect.y - selectplayer.rect.y < - 5:
                self.rect.y += 4

    def update(self):
        self.rect.x+=self.vel_x
            #Mov diagonal
