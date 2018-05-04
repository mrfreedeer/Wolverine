import pygame

ALTO=1200
ANCHO=1000
limites=[10, 8, 11, 10, 8, 6, 9, 4, 12, 8, 8, 10, 9, 4, 7, 5, 2, 8, 9, 9, 9]
#Funciones

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
        cuadro=pygame.transform.scale(cuadro, (95, 95))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (95, 95))
        idleR.append(cuadro)
        idleL.append(cuadro2)


    #Walk R-L
    for x in range(6):
        cuadro=fondo.subsurface(walkRight[x])
        cuadro=pygame.transform.scale(cuadro, (95, 95))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (95, 95))
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
        cuadro=pygame.transform.scale(cuadro, (95, 95))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (95, 95))
        attack1R.append(cuadro)
        attack1L.append(cuadro2)

    #Attack 1 R-L
    for x in range(3):
        cuadro=fondo.subsurface(attack2[x])
        cuadro=pygame.transform.scale(cuadro, (95, 95))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (95, 95))
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
        self.rect.y=250
        self.vel_x=0
        self.vel_y=0
        self.accion=0
        self.salto=False

    def gravedad(self, v):
        if self.vel_y==0:
            self.vel_y=1
        else:
            self.vel_y+=v

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


        self.rect.x += self.vel_x
        self.rect.y+=self.vel_y
        #print self.indice

        self.rect.x += self.vel_x
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    fondo=pygame.image.load('fondo.png')
    wolverine=pygame.image.load('wolverine_sprites.png')
    infoWolverine=wolverine.get_rect()

    wolverine2=pygame.image.load('wolverine_sprites2.png')
    infoWolverine2=wolverine2.get_rect()

    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    matrizJugador=[]
    #matrizJugador2=[]
    matrizJugador=recortar('wolverine_sprites.png')
    #matrizJugador2=recortar('wolverine_sprites2.png')


    jugador=Jugador(matrizJugador)
    #jugador2=Jugador(matrizJugador2)

    jugadores.add(jugador)
    todos.add(jugador)

    #jugadores.add(jugador2)
    #todos.add(jugador2)

    reloj=pygame.time.Clock()
    dir='R'


    pantalla.blit(fondo, [0,-400])
    pantalla.blit(jugador.f[0][0], [jugador.rect.x, jugador.rect.y])
    #pantalla.blit(jugador2.f[0][0], [jugador2.rect.x, jugador2.rect.y])
    pygame.draw.polygon(pantalla, [255,255,255], [[0,400], [ANCHO, 400]],2)
    pygame.display.flip()

    fin=False
    while not fin:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:

                if event.key==pygame.K_RIGHT:
                    dir='R'
                    jugador.indice=0
                    jugador.vel_y=0
                    jugador.accion=2
                    jugador.vel_x=10

                if event.key==pygame.K_UP:
                    jugador.vel_y=-10
                    if dir=='R':
                        jugador.indice=0
                        jugador.accion=2
                        jugador.vel_x=0
                    else:
                        jugador.indice=0
                        jugador.accion=3
                        jugador.vel_x=0

                if event.key==pygame.K_LEFT:
                    dir='L'
                    jugador.indice=0
                    jugador.vel_y=0
                    jugador.accion=3
                    jugador.vel_x=-10

                if event.key==pygame.K_DOWN:
                    jugador.vel_y=10
                    if dir=='R':
                        jugador.indice=0
                        jugador.accion=2
                        jugador.vel_x=0
                    else:
                        jugador.indice=1
                        jugador.accion=3
                        jugador.vel_x=0
                '''
                if event.key==pygame.K_SPACE:
                    jugador.salto=True
                    jugador.indice=0
                    jugador.rect.y+=-20
                    if dir=='R':
                        jugador.accion=4
                    if dir=='L':
                        jugador.accion=5
                    jugador.salto=True
                '''
                if event.key==pygame.K_q:
                    jugador.indice=0
                    if dir=='R':
                        jugador.accion=6
                    if dir=='L':
                        jugador.accion=7

                if event.key==pygame.K_w:
                    jugador.indice=0
                    if dir=='R':
                        jugador.accion=8
                    if dir=='L':
                        jugador.accion=9

            if event.type == pygame.KEYUP:
                jugador.indice=0

                if dir=='R':
                    jugador.accion=0
                if dir=='L':
                    jugador.accion=1
                jugador.vel_x=0
                jugador.vel_y=0






        todos.update()
        pantalla.blit(fondo, [0,-400])
        pygame.draw.polygon(pantalla, [255,255,255], [[0,320], [ANCHO, 320]],2)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)
