import pygame
import random
import math


class fondo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("stage11.png")
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=-50
        self.varx=0
        self.vary=0
        self.mov=True

    def update(self):
        self.rect.x=self.rect.x-self.varx
        self.rect.y=self.rect.y+self.vary

    def movefondo(self):
        self.rect.x=self.rect.x-self.varx



class jugador(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.varx=0
        self.vary=0
        self.j=0
        self.rect.x=300
        self.rect.y=250
        self.salud=100
        self.accion=0
        self.puntaje=0
        self.dir=True
        self.mov=False
        self.c=0
        self.cambiodir=0
        self.flag=True
        self.Tmuerte=5
        self.Tesperar=10
        self.sonido=pygame.mixer.Sound('golpes2.mp3')
        self.Tiempo=120


    def update(self):
        if self.dir:
            self.accion=self.accion
        else:
            if self.flag:
                self.accion=self.accion+self.cambiodir
                self.flag=False
        self.rect.x=self.rect.x+self.varx
        self.rect.y=self.rect.y+self.vary
        self.image=self.m[self.accion][self.j]
        self.j+=1
        if self.j>=len(self.m[self.accion]):
            self.j=0
            if self.dir:
                if not (self.accion==0) and self.mov:
                    self.accion=0
                    self.varx=0
            else:
                if not (self.accion==8) and self.mov:
                    self.accion=8
                    self.varx=0
        if self.salud<=0:
            self.Tmuerte-=1
        if self.Tesperar>0:
            self.Tesperar-=1

        if self.Tesperar==0:
            self.Tiempo-=1
            self.Tesperar=10


class barravida_enemigo(pygame.sprite.Sprite):
    def __init__ (self, vector, pos):
        pygame.sprite.Sprite.__init__(self)
        self.v=vector
        self.image=self.v[0][0]
        self.rect=self.image.get_rect()
        self.i=0
        self.varx=0
        self.rect.midbottom=pos
    def update(self, pos):
        self.rect.midbottom=pos

    def comoloquierollamar(self):
        self.i+=1
        if self.i>=4:
            self.i=4
        self.image=self.v[0][self.i]

class reptiles(pygame.sprite.Sprite):
    def __init__(self, matriz,groupbarras, vector, pos):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.varx=0
        self.vary=0
        self.distancia=0
        self.i=0
        self.golpe=False
        self.accion=0
        self.mov=True
        self.barra=barravida_enemigo(vector, self.rect.midtop)
        groupbarras.add(self.barra)
        self.derecha=True
        self.izquierda=False
        self.Tespera=random.randrange(100,200)
        self.donacion=random.randrange(-5,10)
        self.salud=100
        self.Tmuerte=5

    def update(self):
        self.rect.x=self.rect.x+self.varx
        self.rect.y=self.rect.y+self.vary
        self.barra.update(self.rect.midtop)
        self.image=self.m[self.accion][self.i]
        self.i+=1
        if(self.Tespera>0):
            self.Tespera-=1
        if self.i>=len(self.m[self.accion]):
            self.i=0
            if self.derecha:
                self.i=0
                self.accion=0
                self.varx=0
            if self.izquierda:
                self.i=0
                self.accion=5
                self.varx=0
        if self.salud<=0:
            self.Tmuerte-=1


    def left(self):
        self.izquierda=True
        self.derecha=False
        self.accion=6
        self.varx=-10


    def right(self):
        self.derecha=True
        self.izquierda=False
        self.accion=1
        self.varx=10

    def golpear(self):
        if self.derecha:
                if(self.Tespera<=0):
                    self.accion=2
                    self.golpe=True
                    self.Tespera=random.randrange(100,200)
                    self.varx=0
                    self.i=0

        if self.izquierda:
                if(self.Tespera<=0):
                    self.accion=7
                    self.golpe=True
                    self.Tespera=random.randrange(100,200)
                    self.varx=0
                    self.i=0


class ninjas(pygame.sprite.Sprite):
    def __init__(self, matriz, groupbarras, vector, pos):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.varx=0
        self.vary=0
        self.distancia=0
        self.i=0
        self.golpe=False
        self.accion=0
        self.mov=True
        self.barra=barravida_enemigo(vector, self.rect.midtop)
        groupbarras.add(self.barra)
        self.derecha=True
        self.izquierda=False
        self.Tespera=random.randrange(300,400)
        self.donacion=random.randrange(-10,10)
        self.salud=100
        self.Tmuerte= 5

    def update(self):
        self.rect.x=self.rect.x+self.varx
        self.rect.y=self.rect.y+self.vary
        print self.accion, self.i, 'ninjas'
        self.image=self.m[self.accion][self.i]
        self.barra.update(self.rect.midtop)
        self.i+=1
        if(self.Tespera>0):
            self.Tespera-=1
        if self.i>=len(self.m[self.accion]):
            self.i=0
            if self.derecha:
                self.i=0
                self.accion=0
                self.varx=0
            if self.izquierda:
                self.i=0
                self.accion=5
                self.varx=0
        if self.salud<=0:
            self.Tmuerte-=1

    def left(self):
        self.izquierda=True
        self.derecha=False
        self.accion=6
        self.varx=-10


    def right(self):
        self.izquierda=False
        self.accion=1
        self.derecha=True
        self.varx=10

    def golpear(self):
        if self.derecha:
                if(self.Tespera<=0):
                    self.i=0
                    self.accion=4
                    self.golpe=True
                    self.Tespera=random.randrange(300,400)
                    self.varx=0
        if self.izquierda:
                if(self.Tespera<=0):
                    self.i=0
                    self.accion=9
                    self.golpe=True
                    self.Tespera=random.randrange(300,400)
                    self.varx=0


class enemigas(pygame.sprite.Sprite):
    def __init__(self, matriz, groupbarras, vector, pos):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.varx=0
        self.vary=0
        self.distancia=0
        self.i=0
        self.golpe=False
        self.accion=0
        self.mov=True
        self.barra=barravida_enemigo(vector, self.rect.midtop)
        groupbarras.add(self.barra)
        self.derecha=True
        self.izquierda=False
        self.Tespera=random.randrange(300,400)
        self.donacion=random.randrange(-10,10)
        self.salud=100
        self.Tmuerte=5

    def update(self):
        self.rect.x=self.rect.x+self.varx
        self.rect.y=self.rect.y+self.vary
        self.barra.update(self.rect.midtop)
        print self.accion, self.i
        self.image=self.m[self.accion][self.i]
        self.i+=1
        if(self.Tespera>0):
            self.Tespera-=1
        if self.i>=len(self.m[self.accion]):
            self.i=0
            if self.derecha:
                self.i=0
                self.accion=0
                self.varx=0
            if self.izquierda:
                self.i=0
                self.accion=4
                self.varx=0
        if self.salud<=0:
            self.Tmuerte-=1

    def left(self):
        self.izquierda=True
        self.derecha=False
        self.accion=5
        self.varx=-10


    def right(self):
        self.izquierda=False
        self.accion=1
        self.derecha=True
        self.varx=10

    def golpear(self):
        if self.derecha:
                if(self.Tespera<=0):
                    self.i=0
                    self.accion=2
                    self.golpe=True
                    self.Tespera=random.randrange(300,400)
                    self.varx=0
        if self.izquierda:
                if(self.Tespera<=0):
                    self.i=0
                    self.accion=6
                    self.golpe=True
                    self.Tespera=random.randrange(300,400)
                    self.varx=0


"""class colega(pygame.sprite.Sprite):
    def __init__(self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=50
        self.rect.y=350
        self.varx=0
        self.vary=0
        self.distancia=0
        self.i=0
        self.golpe=False
        self.accion=0
        self.mov=True
        self.derecha=True
        self.izquierda=False
        self.Tespera=random.randrange(0,40)
        self.salud=100
        self.Tmuerte=5

    def update(self):
        self.rect.x=self.rect.x+self.varx
        self.rect.y=self.rect.y+self.vary
        self.image=self.m[self.accion][self.i]
        self.i+=1
        if(self.Tespera>0):
            self.Tespera-=1
        if self.i>=len(self.m[self.accion]):
            self.i=0
            if self.derecha:
                self.i=0
                self.accion=0
                self.varx=0
            if self.izquierda:
                self.i=0
                self.accion=5
                self.varx=0
        if self.salud<=0:
            self.Tmuerte-=1

    def left(self):
        self.izquierda=True
        self.derecha=False
        self.accion=10
        self.varx=-10


    def right(self):
        self.derecha=True
        self.izquierda=False
        self.accion=2
        self.varx=10

    def golpear(self):
        if self.derecha:
                if(self.Tespera<=0):
                    self.golpe=True
                    self.accion=4
                    self.Tespera=random.randrange(0,40)
                    self.varx=0
                    self.i=0

        if self.izquierda:
                if(self.Tespera<=0):
                    self.golpe=True
                    self.accion=12
                    self.Tespera=random.randrange(0,40)
                    self.varx=0
                    self.i=0

    def patada(self):
        if self.golpe:
            if self.derecha:
                if(self.Tespera<=0):
                    self.golpe=True
                    self.accion=5
                    self.Tespera=random.randrange(0,40)
                    self.varx=0
                    self.i=0

            if self.izquierda:
                if(self.Tespera<=0):
                    self.golpe=True
                    self.accion=13
                    self.Tespera=random.randrange(0,40)
                    self.varx=0
                    self.i=0
        self.golpe=False
"""

class helado(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("helado2.png")
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.Ttime=100
        self.id=1
        self.sonido=pygame.mixer.Sound('obtencion.ogg')
        self.varx=0
    def update(self):
        if self.Ttime>0:
            self.Ttime-=1
        self.rect.x=self.rect.x+self.varx

    def desplazar(self):
        self.varx=-10

class pastel(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("pastel.png")
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.Ttime=100
        self.id=0
        self.sonido=pygame.mixer.Sound('obtencion.ogg')
        self.varx=0
    def update(self):
        if self.Ttime>0:
            self.Ttime-=1
        self.rect.x=self.rect.x+self.varx

    def desplazar(self):
        self.varx=-10


class golosina(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("golosina.png")
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.Ttime=100
        self.id=0
        self.varx=0
        self.sonido=pygame.mixer.Sound('obtencion.ogg')
    def update(self):
        if self.Ttime>0:
            self.Ttime-=1
        self.rect.x=self.rect.x+self.varx

    def desplazar(self):
        self.varx=-10



class fuego(pygame.sprite.Sprite):
    def __init__ (self, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.image=self.m[0][0]
        self.rect=self.image.rect_rect()
        self.i=0
        self.rect.x=self.rect.x+300
        self.rect.y=self.rect.y-30
        self.retardo=100
    def update(self):
        if self.retardo<=0:
            i+=1
            self.image=self.m[0][i]
        else:
            self.retardo-=1

class barravida_jugador(pygame.sprite.Sprite):
    def __init__ (self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.v=vector
        self.image=self.v[0][0]
        self.rect=self.image.get_rect()
        self.i=0
        self.rect.x=100
        self.rect.y=30
    def update(self):
        pass
