import pygame
from wolvbasics import *
from jugador import *
red = (255,0,0)         #rgb(255,0,0)
green = (0,255,0)       #rgb(0,255,0)
blue = (0,0,255)        #rgb(0,0,255)
darkBlue = (0,0,128)    #rgb(0,0,128)
yellow =(255,255,51)    #rgb(255,255,51)
white = (255,255,255)   #rgb(255,255,255)
black = (0,0,0)         #rgb(0,0,0)
pink = (255,200,200) #rgb(255,200,200)
posbg = [0, -300]
def printkey(key):
    if key == pygame.K_LEFT:
        print "Left"
    elif key == pygame.K_RIGHT:
        print "Right"
def main():
    pygame.init()
    pygame.font.init()
    screensize = pygame.display.Info()
    RESOLUTION = [screensize.current_w,screensize.current_h]
    bob = Builder(pygame.font.Font('WolverineFont.ttf', 40), pygame.font.Font('WolverineFont.ttf', 60))
    screen = bob.buildscreen()
    menubckg = pygame.image.load('menu.png')
    gamebckg = pygame.image.load('bg.png')
    fondo = pygame.image.load('fondo.png')
    menuoptions = ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"]
    pauseoptions = ["Back to Menu"]
    pauserender = bob.buildtxtrender("PAUSE", 1, white)
    pauseoptionrenders = bob.buildtxtrenders(pauseoptions, 0, white)
    menurenders = bob.buildtxtrenders(menuoptions)
    WolverineTitle = bob.buildtxtrender("Wolverine", 1)
    end = False
    fac = Facade(screen, menurenders, WolverineTitle, [250,200], menubckg, [-550,0])
    fac.display_bkg()
    mouseclick = False
    fac.display_menu()
    fac.loadmodifiers('gamemodifiers.png')
    modi = 0

    fac.setPauserenders(pauseoptionrenders)

    modifiers = pygame.sprite.Group()
    everyone = pygame.sprite.Group()
    m = fac.getModifier(modi)
    modifiers.add(m)
    everyone.add(m)
    state = 'menu'


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
    matrizJugador2=recortar('wolverine_sprites2.png')



    jugador=Jugador(matrizJugador)
    jugador2=Jugador2(matrizJugador2)


    jugadores.add(jugador)
    todos.add(jugador)

    jugadores.add(jugador2)
    todos.add(jugador2)

    reloj=pygame.time.Clock()


    screen.blit(jugador.f[0][0], [jugador.rect.x, jugador.rect.y])
    screen.blit(jugador2.f[0][0], [jugador2.rect.x, jugador2.rect.y])
    #screen.blit(gamebckg, [0,0])
    pygame.draw.polygon(screen, [255,255,255], [[0,400], [ANCHO, 400]],2)
    pygame.display.flip()

    fin=False
    allowedmoves = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_k, pygame.K_j, pygame.K_UP, pygame.K_DOWN]
    allowedmoves2 = [pygame.K_w, pygame.K_d, pygame.K_t, pygame.K_r, pygame.K_a, pygame.K_s]
    moves = []
    moves2 = []
    pausewidth = pauserender.get_width()/2
    pauseheight = pauserender.get_height()/2
    for x in pauseoptionrenders:
        pauseheight += x.get_height()/2 + 10
    pausepositions = []

    pausexpos = RESOLUTION[0]/2
    pauseypos = RESOLUTION[1]/2 - pauseheight
    xpos = pausexpos
    ypos = pauseypos + pauserender.get_height() + 10
    for x in pauseoptionrenders:
        pausepositions.append((pausexpos-x.get_width()/2, ypos))
        ypos += x.get_height() + 10
    fac.pausepositions = pausepositions
    while not end:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouseclick = True
            if event.type == pygame.MOUSEBUTTONUP:
                    mouseclick = False
            if state == 'menu':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        modi -= 1
                    if event.key == pygame.K_RIGHT:
                        modi += 1
                    if modi < 0:
                        modi = 3
                    elif modi > 3:
                        modi = 0
                    if modifiers:
                        for x in modifiers:
                            x.kill()
                    m = fac.getModifier(modi)
                    modifiers.add(m)
                    everyone.add(m)
            elif state == "Opcion 1":

                print 'Jugador:', jugador.rect.x, jugador.rect.y
                print 'Fondo:',posbg
                #Gestion de limites------------------------------------------------------
                if jugador.rect.x>=1100:
                    if posbg[0]==0:
                        posbg[0]=posbg[0]
                    if posbg[0]==-1000:
                        posbg[0]=posbg[0]
                    else:
                        posbg[0]-=12
                #Acomodar limite jugador 2, aplica rangos iguales. Aun no se como volver a subir el fondo
                if jugador.rect.y>=610:
                    if jugador.rect.y<=330:
                        jugador.uplimit_y=jugador.uplimit_y
                    else:
                        jugador.uplimit_y+=-6
                    if posbg[1]<=-430:
                        posbg[1]=posbg[1]
                    else:
                        posbg[1]-=12
                #ACOMODAR ESTE
                '''
                if posbg[1]<=-432:
                    if jugador.rect.y<=342:
                        jugador.downlimit_y+=6

                        posbg[1]+=12
                '''
                if jugador2.rect.x>=1100:
                    if posbg[0]==0:
                        posbg[0]=posbg[0]
                    if posbg[0]==-1000:
                        posbg[0]=posbg[0]
                    else:
                        posbg[0]-=12
                #Acomodar limite jugador 2, aplica rangos iguales. Aun no se como volver a subir el fondo
                if jugador2.rect.y>=610:
                    if jugador2.rect.y<=330:
                        jugador2.uplimit_y=jugador2.uplimit_y
                    else:
                        jugador2.uplimit_y+=-6
                    if posbg[1]<=-430:
                        posbg[1]=posbg[1]
                    else:
                        posbg[1]-=12
                #ACOMODAR ESTE
                '''
                if posbg[1]<=-432:
                    if jugador2.rect.y<=342:
                        jugador2.downlimit_y+=6

                        posbg[1]+=12
                '''



                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        fac.pause = not fac.pause

                    if event.key in allowedmoves:
                        moves.insert(0,event.key)
                    if moves != []:
                        jugador.move(moves[0])

                    if event.key in allowedmoves2:
                        moves2.insert(0,event.key)
                    if moves2 != []:
                        jugador2.move(moves2[0])

                if event.type == pygame.KEYUP:
                    if event.key in allowedmoves:
                        moves.remove(event.key)

                    if event.key in allowedmoves2:
                        moves2.remove(event.key)
                    jugador.soltartecla()
                    jugador2.soltartecla()
                    if moves != []:
                        jugador.move(moves[0])
                    if moves2 != []:
                        jugador2.move(moves2[0])
        mousepos = pygame.mouse.get_pos()
        mouseonoption = fac.checkmouse(mousepos)
        if state == 'menu':
            if mouseonoption != -1 and mouseclick: #Detecting Option Clicked
                print "Menu Option Clicked: ", menuoptions[mouseonoption]
                mouseclick = False
                state = menuoptions[mouseonoption]
            if mouseonoption != -1 and mouseonoption not in fac.getTurned():
                #Turns blue the option the mouse is on
                txt = menuoptions[mouseonoption]
                fac.appendTurned(mouseonoption)
                newrender = bob.buildtxtrender(txt, 0, white)
                fac.popmenurenders(mouseonoption)
                fac.insertmenurenders(mouseonoption, newrender)
            elif fac.getTurned() != [] and mouseonoption == -1:
                #Returns all text to normal colors
                fac.emptyTurned()
                fac.resetmenurenders()
            elif len(fac.getTurned()) > 1:
                fac.emptyTurned()
                fac.resetmenurenders()
                txt = menuoptions[mouseonoption]
                fac.appendTurned(mouseonoption)
                newrender = bob.buildtxtrender(txt, 0, white)
                fac.popmenurenders(mouseonoption)
                fac.insertmenurenders(mouseonoption, newrender)
            screen.fill(black)
            fac.display_bkg()
            fac.display_menu()
            mousepos = pygame.mouse.get_pos()

            everyone.draw(screen)
        if state == "Opcion 1":
            if not fac.pause:
                todos.update()
                screen.fill([0,0,0])
                screen.blit(fondo,[0,-50])
                screen.blit(gamebckg, posbg)

                todos.draw(screen)
                fac.drawLife(jugador.getHealth())
                pygame.display.flip()
                reloj.tick(10)
            else:
                screen.blit(pauserender, [pausexpos- pausewidth,pauseypos])
                i = 0
                for x in fac._pauserenders:
                    screen.blit(x,fac.pausepositions[i])
                    i += 1
                select = fac.checkmousepause(mousepos)

                if select != -1:
                    txt = pauseoptions[select]
                    fac._pauserenders.pop(select)
                    selectedrender = bob.buildtxtrender(txt, 0, red)
                    fac._pauserenders.insert(select,selectedrender)
                    fac._turnedoptions.append(select)
                elif select == -1 and fac.getTurned() != []:
                    fac._pauserenders = fac._normalpauserenders[:]
                    fac.emptyTurned()
                elif len(fac.getTurned())> 1:
                    txt = pauseoptions[select]
                    fac._pauserenders = fac._normalpauserenders[:]
                    fac._pauserenders.pop(select)
                    selectedrender = bob.buildtxtrender(txt, 0, red)
                    fac._pauserenders.insert(select,selectedrender)
                    fac._turnedoptions.append(select)
                if pauseoptions[select] == "Back to Menu" and mouseclick:
                    state = 'menu'
                    mouseclick = False
                    fac.pause = False
                pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
