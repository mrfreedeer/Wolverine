import pygame

ALTO=1000
ANCHO=1000
limites=[10, 8, 11, 10, 8, 6, 9, 4, 12, 8, 8, 10, 9, 4, 7, 5, 2, 8, 9, 9, 9]
#Funciones
'''
def recortarCara(archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()
    lista=[]
    cuadro=fondo.subsurface(5, 1628, 105, 105)
    #cuadro=pygame.transform.scale(cuadro, (95, 95))
    lista.append(cuadro)
    return lista
'''
def recortar(archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()
    matriz=[]
    idleR=[]
    idleL=[]
    walkR=[]
    walkL=[]
    jumpR=[]
    jumpL=[]
    attack1R=[]
    attack1L=[]
    attack2R=[]
    attack2L=[]



    idle=[[18,25,54,59], [93,25,54,59], [172,25,54,59]]

    #walkRight=[[11, 193, 59, 59], [174, 193, 49, 59], [89, 192, 59, 59], [249, 193, 59, 59], [323, 200, 56, 53], [402, 197, 56, 55]]
    #walkRight=[[11, 193, 59, 59], [89, 192, 59, 59], [249, 193, 59, 59], [323, 200, 56, 53], [402, 197, 56, 55]]
    walkRight=[[11, 193, 59, 59] , [172, 196, 51, 55], [249, 193, 59, 59], [323, 200, 56, 53], [402, 197, 56, 55],[16, 281, 51, 55], [91, 281, 51, 55]]

    '''          Se ancha                               Se ancha                             '''
    jump=[[178, 252, 40, 85], [244, 253, 56, 85], [331, 253, 40, 85], [391, 262, 66, 76]]


    attack1=[[245, 11, 60, 72], [323, 12, 60, 72], [385, 12, 77, 72]]

    attack2=[[242, 108, 63, 59], [313, 95, 73, 73], [397, 98, 54, 74]]

    #Idle R-L
    for x in range(3):
        cuadro=fondo.subsurface(idle[x])
        cuadro=pygame.transform.scale(cuadro, (125, 125))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (125, 125))
        idleR.append(cuadro)
        idleL.append(cuadro2)


    #Walk R-L
    for x in range(6):
        cuadro=fondo.subsurface(walkRight[x])
        cuadro=pygame.transform.scale(cuadro, (125, 125))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (125, 125))
        walkR.append(cuadro)
        walkL.append(cuadro2)

    #Jump R-L
    for x in range(4):
        cuadro=fondo.subsurface(jump[x])
        cuadro=pygame.transform.scale(cuadro, (100, 95))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (100, 95))
        jumpR.append(cuadro)
        jumpL.append(cuadro2)

    #Attack 1 R-L
    for x in range(3):
        cuadro=fondo.subsurface(attack1[x])
        cuadro=pygame.transform.scale(cuadro, (125, 125))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (125, 125))
        attack1R.append(cuadro)
        attack1L.append(cuadro2)

    #Attack 2 R-L
    for x in range(3):
        cuadro=fondo.subsurface(attack2[x])
        cuadro=pygame.transform.scale(cuadro, (125, 125))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (125, 125))
        attack2R.append(cuadro)
        attack2L.append(cuadro2)

    return idleR, idleL, walkR, walkL, jumpR, jumpL, attack1R, attack1L, attack2R, attack2L

#Clases
class Jugador(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.f=matriz
        self.image=self.f[0][0]
        self.rect=self.image.get_rect()
        self.indice=0
        self.rect.x=50
        self.rect.y=450
        self.vel_x=0
        self.vel_y=0
        self.accion=0
        self.salto=False
        self.dir = 'R'
        self._health = 100
        self.uplimit_y=450
        self.downlimit_y=610
    def getHealth(self):
        return self._health
    def gravedad(self, v):
        if self.vel_y==0:
            self.vel_y=1
        else:
            self.vel_y+=v
    def move(self, key):
        if key == pygame.K_RIGHT:
            self.derecha()
        elif key == pygame.K_LEFT:
            self.izquierda()
        elif key == pygame.K_UP:
            self.arriba()
        elif key == pygame.K_DOWN:
            self.abajo()
        elif key == pygame.K_j:
            self.teclaq()
        elif key == pygame.K_k:
            self.teclaw()
    def update(self):
        '''
        if self.salto:
            self.vel_y=-15
            self.salto=False
        '''
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
        #Walk R
        if self.accion==2:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1
            if self.indice > 5:
                self.indice=0

        #Walk L
        if self.accion==3:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice > 5:
                self.indice=0

        #Jump R
        if self.accion==4:
            if self.indice <4:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice == 3:
                self.indice=3

        #Jump L
        if self.accion==5:
            if self.indice <4:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice == 3:
                self.indice=3

        #1
        #Attack R
        if self.accion==6:
            if self.indice <3:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 2:
                self.indice=0

        #Attack L
        if self.accion==7:
            if self.indice <3:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 2:
                self.indice=0
        #2
        #Attack R
        if self.accion==8:
            if self.indice <3:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 2:
                self.indice=0

        #Attack L
        if self.accion==9:
            if self.indice <3:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 2:
                self.indice=0

        #self.gravedad(1)
        self.rect.y+=self.vel_y

        if self.rect.y <=self.uplimit_y:
            self.rect.y=self.uplimit_y
            self.vel_y=0

        if self.rect.y>=610:
            self.rect.y=610
            self.vel_y=0

        if self.rect.x>1100:
            self.rect.x=1100
            self.vel_x=0

        if self.rect.x<0:
            self.rect.x=0
            self.vel_x=0

        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

    def derecha(self):
        if self.accion==4:
            pass
        else:
            self.indice=0
            self.vel_y=0
            self.salto=False
            self.dir='R'
            self.accion=2
            self.vel_x=18
        '''
        if self.rect.x>=1050:
            self.rect.x=1050
            self.vel_x=0
        '''
    def izquierda(self):
        if self.accion==5:
            pass
        else:
            self.indice=0
            self.vel_y=0
            self.salto=False
            self.dir='L'
            self.accion=3
            self.vel_x=-18

    def arriba(self):
        self.vel_y=-10
        if self.dir=='R':
            self.indice=0
            self.accion=2
            self.vel_x=0
        else:
            self.indice=0
            self.accion=3
            self.vel_x=0

    def abajo(self):
        self.vel_y=10
        if self.dir=='R':
            self.indice=0
            self.accion=2
            self.vel_x=0
        else:
            self.indice=0
            self.accion=3
            self.vel_x=0

    def saltar(self):
        self.salto=True
        self.indice=0
        self.rect.y+=-20
        if self.dir=='R':
            self.accion=4
        if self.dir=='L':
            self.accion=5
        self.salto=True

    def teclaq(self):
        self.indice=0
        if self.dir=='R':
            self.accion=6
        if self.dir=='L':
            self.accion=7

    def teclaw(self):
        self.indice=0
        if self.dir=='R':
            self.accion=8
        if self.dir=='L':
            self.accion=9

    def soltartecla(self):
        self.indice=0
        if self.accion==2 or self.accion==3:
            if self.dir=='R':
                self.accion=0
            if self.dir=='L':
                self.accion=1
            self.vel_x=0
            self.vel_y=0

        if self.accion==4 or self.accion==5 or self.accion==6 or self.accion==7 or self.accion==8 or self.accion==9:
            if self.dir=='R':
                self.accion=0
            if self.dir=='L':
                self.accion=1
            self.vel_x=0

class Jugador2(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.f=matriz
        self.image=self.f[0][0]
        self.rect=self.image.get_rect()
        self.indice=0
        self.rect.x=50
        self.rect.y=550
        self.vel_x=0
        self.vel_y=0
        self.accion=0
        self.salto=False
        self.dir = 'R'
        self._health = 100
        self.uplimit_y=450
        self.downlimit_y=610
    def getHealth(self):
        return self._health
    def gravedad(self, v):
        if self.vel_y==0:
            self.vel_y=1
        else:
            self.vel_y+=v
    def move(self, key):
        if key == pygame.K_d:
            self.derecha()
        elif key == pygame.K_a:
            self.izquierda()
        elif key == pygame.K_w:
            self.arriba()
        elif key == pygame.K_s:
            self.abajo()
        #elif key == pygame.K_SPACE:
        #    self.saltar()
        elif key == pygame.K_r:
            self.teclaq()
        elif key == pygame.K_t:
            self.teclaw()
    def update(self):
        '''
        if self.salto:
            self.vel_y=-15
            self.salto=False
        '''
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
        #Walk R
        if self.accion==2:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1
            if self.indice > 5:
                self.indice=0

        #Walk L
        if self.accion==3:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice > 5:
                self.indice=0

        #Jump R
        if self.accion==4:
            if self.indice <4:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice == 3:
                self.indice=3

        #Jump L
        if self.accion==5:
            if self.indice <4:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice == 3:
                self.indice=3

        #1
        #Attack R
        if self.accion==6:
            if self.indice <3:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 2:
                self.indice=0

        #Attack L
        if self.accion==7:
            if self.indice <3:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 2:
                self.indice=0
        #2
        #Attack R
        if self.accion==8:
            if self.indice <3:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 2:
                self.indice=0

        #Attack L
        if self.accion==9:
            if self.indice <3:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice > 2:
                self.indice=0

        #self.gravedad(1)
        self.rect.y+=self.vel_y

        if self.rect.y <=self.uplimit_y:
            self.rect.y=self.uplimit_y
            self.vel_y=0

        if self.rect.y>=610:
            self.rect.y=610
            self.vel_y=0

        if self.rect.x>1100:
            self.rect.x=1100
            self.vel_x=0

        if self.rect.x<0:
            self.rect.x=0
            self.vel_x=0

        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

    def derecha(self):
        if self.accion==4:
            pass
        else:
            self.indice=0
            self.vel_y=0
            self.salto=False
            self.dir='R'
            self.accion=2
            self.vel_x=18
        '''
        if self.rect.x>=1050:
            self.rect.x=1050
            self.vel_x=0
        '''
    def izquierda(self):
        if self.accion==5:
            pass
        else:
            self.indice=0
            self.vel_y=0
            self.salto=False
            self.dir='L'
            self.accion=3
            self.vel_x=-18

    def arriba(self):
        self.vel_y=-10
        if self.dir=='R':
            self.indice=0
            self.accion=2
            self.vel_x=0
        else:
            self.indice=0
            self.accion=3
            self.vel_x=0

    def abajo(self):
        self.vel_y=10
        if self.dir=='R':
            self.indice=0
            self.accion=2
            self.vel_x=0
        else:
            self.indice=0
            self.accion=3
            self.vel_x=0

    def saltar(self):
        self.salto=True
        self.indice=0
        self.rect.y+=-20
        if self.dir=='R':
            self.accion=4
        if self.dir=='L':
            self.accion=5
        self.salto=True

    def teclaq(self):
        self.indice=0
        if self.dir=='R':
            self.accion=6
        if self.dir=='L':
            self.accion=7

    def teclaw(self):
        self.indice=0
        if self.dir=='R':
            self.accion=8
        if self.dir=='L':
            self.accion=9

    def soltartecla(self):
        self.indice=0
        if self.accion==2 or self.accion==3:
            if self.dir=='R':
                self.accion=0
            if self.dir=='L':
                self.accion=1
            self.vel_x=0
            self.vel_y=0

        if self.accion==4 or self.accion==5 or self.accion==6 or self.accion==7 or self.accion==8 or self.accion==9:
            if self.dir=='R':
                self.accion=0
            if self.dir=='L':
                self.accion=1
            self.vel_x=0
