import pygame
import random
import math
random.seed(pygame.time.get_ticks())

ALTO=1000
ANCHO=1000
limites=[10, 8, 11, 10, 8, 6, 9, 4, 12, 8, 8, 10, 9, 4, 7, 5, 2, 8, 9, 9, 9]
pygame.mixer.init(44100, -16, 2, 2048)
punchE2=pygame.mixer.Sound('punchEnemy.ogg')
stepE=pygame.mixer.Sound('pasosJugador.ogg')
stepE.set_volume(0.05)
screensize = pygame.display.Info()
RESOLUTION = [screensize.current_w, screensize.current_h]
bglimit = 10
#Funciones

def recortarEne1(archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()
    matriz=[]
    idleR=[]
    idleL=[]
    attack1R=[]
    attack1L=[]




    idle=[[248, 187, 57,75], [305, 187, 57,75], [362, 187, 57,75]]

    #walkRight=[[11, 193, 59, 59] , [172, 196, 51, 55], [249, 193, 59, 59], [323, 200, 56, 53], [402, 197, 56, 55],[16, 281, 51, 55], [91, 281, 51, 55]]

    attack1=[[4,183,50,75], [67,183,77,75], [154,183,84,75]]

    #attack2=[[242, 108, 63, 59], [313, 95, 73, 73], [397, 98, 54, 74]]

    #Idle R-L
    for x in range(3):
        cuadro=fondo.subsurface(idle[x])
        cuadro=pygame.transform.scale(cuadro, (125, 125))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (125, 125))
        idleR.append(cuadro2)
        idleL.append(cuadro)

    #Attack 1 R-L
    '''
    for x in range(3):
        cuadro=fondo.subsurface(attack1[x])
        cuadro=pygame.transform.scale(cuadro, (125, 125))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (125, 125))
        attack1R.append(cuadro2)
        attack1L.append(cuadro)
    '''
    cuadro0=fondo.subsurface(attack1[0])
    cuadro0=pygame.transform.scale(cuadro0, (125, 125))
    cuadro1=fondo.subsurface(attack1[1])
    cuadro1=pygame.transform.scale(cuadro1, (192, 125))
    cuadro2=fondo.subsurface(attack1[2])
    cuadro2=pygame.transform.scale(cuadro1, (210, 125))

    attack1L.append(cuadro0)
    attack1L.append(cuadro1)
    attack1L.append(cuadro2)

    cuadro00=pygame.transform.flip(cuadro0, True, False)
    cuadro11=pygame.transform.flip(cuadro1, True, False)
    cuadro22=pygame.transform.flip(cuadro2, True, False)

    attack1R.append(cuadro00)
    attack1R.append(cuadro11)
    attack1R.append(cuadro22)

    return idleR, idleL, attack1R, attack1L

def recortarEne2(archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()
    matriz=[]
    idleR=[]
    idleL=[]
    walkR=[]
    walkL=[]
    attack1R=[]
    attack1L=[]




    idle=[[1, 11, 31, 67], [55, 11, 31, 67], [111, 11, 31, 67]]

    walkRight=[[183, 11, 38, 67] , [251, 11, 31, 67], [310, 11, 31, 67], [364, 11, 37, 67], [428, 11, 30, 67],[485, 11, 30, 67]]

    attack1=[[0,101,35,67], [49,101,55,67]]


    #Idle R-L
    for x in range(3):
        cuadro=fondo.subsurface(idle[x])
        cuadro=pygame.transform.scale(cuadro, (100, 125))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (100, 125))
        idleR.append(cuadro)
        idleL.append(cuadro2)

    #Walk R-L
    for x in range(6):
        cuadro=fondo.subsurface(walkRight[x])
        cuadro=pygame.transform.scale(cuadro, (100, 125))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (100, 125))
        walkR.append(cuadro)
        walkL.append(cuadro2)

    #Attack 1 R-L
    for x in range(2):
        cuadro=fondo.subsurface(attack1[x])
        cuadro=pygame.transform.scale(cuadro, (100, 125))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (100, 125))
        attack1R.append(cuadro)
        attack1L.append(cuadro2)


    return idleR, idleL, walkR, walkL, attack1R, attack1L

def recortarBala(archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()
    matriz=[]

    cuadro=fondo.subsurface(410, 35, 15, 15)
    matriz.append(cuadro)

    return matriz
matrizBala=recortarBala('lasers.png')
#Clases
class Enemigo1(pygame.sprite.Sprite):
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

    def getHealth(self):
        return self._health

    def shoot(self, key):
        a=random.randrange(0,10)
        if a==5:
            if self.accion==2:
                pass

    def update(self):
        #Idle R
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




class Enemigo2(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.f=matriz
        self.image=self.f[0][0]
        self.rect=self.image.get_rect()
        self.indice=0
        self.rect.x=900
        self.rect.y=500
        self.accion=0
        self.dir = 'R'
        self._health = 100
        self.finished = False
        self.prevkey = None
        self.vel_y = 0
        self.vel_x = 0
        self.vel_x_value = 10
        self.vel_y_value = 6
        self.moverange = 50
        self.movetime = random.randrange(0,100)

    def getHealth(self):
        return self._health

    def getSlope(self, posJugador):
        point1 = [self.rect.x, self.rect.y]
        if self.rect.x == posJugador[0]:
            return False
        m = float(posJugador[1] -  point1[1])/(posJugador[0] - point1[0])
        b = posJugador[1] - m*posJugador[0]

        return [m, b]
    def isAttacking(self):
        if self.prevkey in ['AL', 'AR']:
            return True
        else:
            return False
    def AImove(self, jugador1, jugador2 = None, noplayers = 1):

        self.movetime -= 1
        if self.movetime <= -20:
            print "reset"
            self.movetime = random.randrange(0,100)
            self.move('I')
        if self.movetime <= 0:
            if noplayers == 1:
                selectplayer = jugador1
            else:
                distanceplayer1 = math.fabs(jugador1.rect.x-self.rect.x)+math.fabs(jugador1.rect.y-self.rect.y)
                distanceplayer2 = math.fabs(jugador2.rect.x-self.rect.x)+math.fabs(jugador2.rect.y-self.rect.y)
                if distanceplayer1 > distanceplayer2:
                    selectplayer = jugador2
                else:
                    selectplayer = jugador1
            if math.fabs(selectplayer.rect.x - self.rect.x) <= self.moverange and math.fabs(selectplayer.rect.y- self.rect.y) <= self.moverange/4:
                if selectplayer.rect.x - self.rect.x > 0:
                    self.move('AR')
                else:
                    self.move('AL')
            else:
                movedir = random.randrange(0,2)
                discardedy = False
                if movedir:
                    if selectplayer.rect.y - self.rect.y > self.moverange/4:
                        self.vel_y = self.vel_y_value
                        if selectplayer.rect.x - self.rect.x > 0:
                            self.move('R')
                        else:
                            self.move('L')
                    elif selectplayer.rect.y - self.rect.y < -self.moverange/4:
                        self.vel_y = -self.vel_y_value
                        if selectplayer.rect.x - self.rect.x > 0:
                            self.move('R')
                        else:
                            self.move('L')
                    else:
                        discardedy = True
                else:
                    if selectplayer.rect.x - self.rect.x > self.moverange:
                        self.vel_x = self.vel_x_value
                        if selectplayer.rect.x - self.rect.x > 0:
                            self.move('R')
                        else:
                            self.move('L')
                    elif selectplayer.rect.x - self.rect.x < -self.moverange:
                        self.vel_x = -self.vel_x_value
                        if selectplayer.rect.x - self.rect.x > 0:
                            self.move('R')
                        else:
                            self.move('L')





    def move(self, key):
        if self.finished or self.prevkey not in ['AL', 'AR']:
            self.finished = False
            if key == 'R':
                self.accion = 2
            elif key == 'L':
                self.accion = 3
            elif key == 'AR':
                self.accion = 4
            elif key == 'AL':
                self.accion = 5
            elif key == 'I':
                self.accion = 0
            self.prevkey = key
            self.indice = 0
    def update(self):
        #Idle R
        if self.accion==0:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice > 2:
                self.indice=0
            self.vel_x = 0
            self.vel_y = 0
        #Idle L
        if self.accion==1:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice > 2:
                self.finished = True
                self.indice=0
            self.vel_x = 0
            self.vel_y = 0

        #Walk R
        if self.accion==2:
            if self.indice <=5:
                self.image = self.f[self.accion][self.indice]
                if self.indice==0:
                    stepE.play()
                if self.indice==3:
                    stepE.play()
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 5:
                self.finished = True
                self.indice=0

        #Walk L
        if self.accion==3:
            if self.indice <=5:
                self.image = self.f[self.accion][self.indice]
                if self.indice==0:
                    stepE.play()
                if self.indice==3:
                    stepE.play()
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 5:
                self.finished = True
                self.indice=0

        #1
        #Attack R
        if self.accion==4:
            if self.indice <=1:
                self.image = self.f[self.accion][self.indice]
                if self.indice==1:
                    punchE2.play()
                self.indice += 1

            if self.indice > 1:
                self.finished = True
                self.indice=0
            self.vel_x = 0
            self.vel_y = 0

        #Attack L
        if self.accion==5:
            if self.indice <=1:
                self.image = self.f[self.accion][self.indice]
                if self.indice==1:
                    punchE2.play()
                self.indice += 1

            if self.indice > 1:
                self.finished = True
                self.indice=0
            self.vel_x = 0
            self.vel_y = 0
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

        #if self.rect.x + self.rect.width > RESOLUTION[0] - bglimit:
        #    self.rect.x = RESOLUTION[0] - bglimit - self.rect.width
        #elif self.rect.x < bglimit:
        #    self.rect.x = bglimit


class Bala (pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.f=matriz
        self.image=self.f[0]
        self.rect=self.image.get_rect()
        self.rect.x=50
        self.rect.y=450
        self.vel_x=5
        self.dir = 'R'

        def update(self):
            self.rect.x+=self.vel_x
            #Mov diagonal
