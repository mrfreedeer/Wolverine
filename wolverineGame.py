import pygame

ALTO=1000
ANCHO=1000
limites=[10, 8, 11, 10, 8, 6, 9, 4, 12, 8, 8, 10, 9, 4, 7, 5, 2, 8, 9, 9, 9]
#Funciones
def recortarCara(archivo):
    fondo=pygame.image.load(archivo)
    infoFondo=fondo.get_rect()
    lista=[]
    cuadro=fondo.subsurface(5, 1628, 105, 105)
    #cuadro=pygame.transform.scale(cuadro, (95, 95))
    lista.append(cuadro)
    return lista

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



    idle=[[0,0,58,54], [69,0,58,54], [133,0,58,54], [199,0,58,54], [269,0,58,54], [339,0,58,54], [401,0,58,54],
            [473,0,58,54], [538,0,58,54], [598,0,58,54]]

    walkRight=[[0, 608, 51, 47], [56, 608, 51, 47], [105, 608, 51, 47], [154, 608, 51, 47], [210, 608, 51, 47],
            [267, 608, 51, 47], [326, 608, 51, 47], [387, 608, 51, 47], [440, 608, 51, 47], [491, 608, 49, 47],
            [544, 608, 49, 47], [598, 608, 51, 47]]

    jump=[[6, 764, 72, 42], [87, 743, 44, 62], [139, 741, 51, 64], [201, 736, 62, 64], [273, 745, 70, 48], [350, 747, 64, 53],
        [420, 745, 55, 59], [481, 745, 55, 68]]

    attack1=[[7, 526, 77, 58], [95, 526, 77, 58]]

    #Idle R-L
    for x in range(limites[0]):
        cuadro=fondo.subsurface(idle[x])
        cuadro=pygame.transform.scale(cuadro, (95, 95))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (100, 95))
        idleR.append(cuadro)
        idleL.append(cuadro2)


    #Walk R-L
    for x in range(limites[8]):
        cuadro=fondo.subsurface(walkRight[x])
        cuadro=pygame.transform.scale(cuadro, (90, 90))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (90, 90))
        walkR.append(cuadro)
        walkL.append(cuadro2)

    #Jump R-L
    for x in range(3):
        cuadro=fondo.subsurface(jump[x])
        cuadro=pygame.transform.scale(cuadro, (100, 100))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (100, 100))
        jumpR.append(cuadro)
        jumpL.append(cuadro2)

    #Attack 1 R-L
    for x in range(2):
        cuadro=fondo.subsurface(attack1[x])
        cuadro=pygame.transform.scale(cuadro, (100, 100))
        cuadro2=pygame.transform.flip(cuadro, True, False)
        cuadro2=pygame.transform.scale(cuadro2, (90, 90))
        attack1R.append(cuadro)
        attack1L.append(cuadro2)

    return idleR, idleL, walkR, walkL, jumpR, jumpL, attack1R, attack1L

#Clases
class Jugador(pygame.sprite.Sprite):
    def __init__(self, matriz, imagenCara):
        pygame.sprite.Sprite.__init__(self)
        self.f=matriz
        self.image=self.f[0][0]
        self.lifeImage=imagenCara
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

            if self.indice > 9:
                self.indice=0
        #Idle R
        if self.accion==1:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice > 9:
                self.indice=0
        #Walk R
        if self.accion==2:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1


            if self.indice == 9:
                self.rect.x+=-10

            if self.indice > 11:
                self.indice=0

        #Walk L
        if self.accion==3:
            self.image = self.f[self.accion][self.indice]
            self.indice += 1

            if self.indice == 9:
                self.rect.x+=-10

            if self.indice > 11:
                self.indice=0

        #Jump R
        if self.accion==4:
            if self.indice <3:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice == 3:
                self.indice=3

        #Jump L
        if self.accion==5:
            if self.indice <3:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice == 3:
                self.indice=3

        #Attack R
        if self.accion==6:
            if self.indice <2:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice == 1:
                self.indice=0

        #Attack L
        if self.accion==7:
            if self.indice <1:
                self.image = self.f[self.accion][self.indice]
                self.indice += 1
            #Es 7 normalmente
            if self.indice == 1:
                self.indice=0

        self.gravedad(1)
        self.rect.y+=self.vel_y
        if self.rect.y > (255):
            self.rect.y=250
            self.vel_y=0
        self.rect.x += self.vel_x
        #print self.indice

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    #fondo=pygame.image.load('mapa01.png')
    wolverine=pygame.image.load('WolverineCort.png')
    infoWolverine=wolverine.get_rect()

    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    matrizJugador=[]
    matrizJugador=recortar('WolverineCort.png')

    wolvFace=recortarCara('WolverineCort.png')

    jugador=Jugador(matrizJugador, wolvFace)
    jugadores.add(jugador)
    todos.add(jugador)

    reloj=pygame.time.Clock()
    dir='R'


    pantalla.blit(jugador.f[0][0], [jugador.rect.x, jugador.rect.y])
    pygame.draw.polygon(pantalla, [255,255,255], [[0,400], [ANCHO, 400]],2)
    pygame.display.flip()

    fin=False
    while not fin:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:



                if event.key==pygame.K_RIGHT:
                    if jugador.accion==4:
                        pass
                    else:
                        jugador.indice=0
                        jugador.vel_y=0
                        jugador.rect.y+=10
                        jugador.salto=False
                        dir='R'
                        jugador.accion=2
                        jugador.vel_x=10


                if event.key==pygame.K_LEFT:
                    if jugador.accion==5:
                        pass
                    else:
                        jugador.indice=0
                        jugador.vel_y=0
                        jugador.rect.y+=10
                        jugador.salto=False
                        dir='L'
                        jugador.accion=3
                        jugador.vel_x=-10

                if event.key==pygame.K_SPACE:
                    jugador.salto=True
                    jugador.indice=0
                    jugador.rect.y+=-20
                    if dir=='R':
                        jugador.accion=4
                    if dir=='L':
                        jugador.accion=5
                    jugador.salto=True

                if event.key==pygame.K_q:
                    jugador.indice=0
                    if dir=='R':
                        jugador.accion=6
                    if dir=='L':
                        jugador.accion=7


            if event.type == pygame.KEYUP:
                jugador.indice=0
                if jugador.accion==2 or jugador.accion==3:
                    if dir=='R':
                        jugador.accion=0
                    if dir=='L':
                        jugador.accion=1
                    jugador.vel_x=0
                    jugador.rect.y+=10
                if jugador.accion==4 or jugador.accion==5 or jugador.accion==6 or jugador.accion==7:
                    if dir=='R':
                        jugador.accion=0
                    if dir=='L':
                        jugador.accion=1
                    jugador.vel_x=0
                    jugador.rect.y+=20


            if jugador.salto:
                jugador.vel_y=-15
                jugador.salto=False




        todos.update()
        pantalla.fill([0,0,0])
        pygame.draw.polygon(pantalla, [255,255,255], [[0,320], [ANCHO, 320]],2)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(15)
