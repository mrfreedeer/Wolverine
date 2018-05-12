import pygame
import time
import random
from wolvbasics import *
from jugador import *
from enemigo import *

red = (255,0,0)         #rgb(255,0,0)
green = (0,255,0)       #rgb(0,255,0)
blue = (0,0,255)        #rgb(0,0,255)
darkBlue = (0,0,128)    #rgb(0,0,128)
yellow =(255,255,51)    #rgb(255,255,51)
white = (255,255,255)   #rgb(255,255,255)
black = (0,0,0)         #rgb(0,0,0)
pink = (255,200,200) #rgb(255,200,200)
posbg = [0, -840]
def printkey(key):
    if key == pygame.K_LEFT:
        print "Left"
    elif key == pygame.K_RIGHT:
        print "Right"

def main():

    pygame.init()
    pygame.font.init()
    bob = Builder(pygame.font.Font('WolverineFont.ttf', 40), pygame.font.Font('WolverineFont.ttf', 60))
    screen = bob.buildscreen()
    menubckg = pygame.image.load('menu.png')
    menubckg2 = pygame.image.load('menu.png')
    gamebckg = pygame.image.load('bg.png')
    bginfo = [gamebckg.get_rect()[2],gamebckg.get_rect()[3]]
    fondo = pygame.image.load('fondo.png')
    player1 = pygame.image.load('jugador1.png')
    player1=pygame.transform.scale(player1, (750, 350))
    player2 = pygame.image.load('jugador2.png')
    player2=pygame.transform.scale(player2, (750, 350))
    menuoptions = ["1 Jugador", "2 Jugadores", "Instrucciones", "Salir"]
    pauseoptions = ["Back to Menu"]
    pauserender = bob.buildtxtrender("PAUSE", 1, white)
    pauseoptionrenders = bob.buildtxtrenders(pauseoptions, 0, white)
    menurenders = bob.buildtxtrenders(menuoptions)
    WolverineTitle = bob.buildtxtrender("Wolverine", 1)
    end = False
    fac = Facade(screen, menurenders, WolverineTitle, [250,200], menubckg, [-550,0])
    fac._screensize = bob.buildresolution()
    posbg[1] += fac._screensize[1]-200
    fac.posbg = posbg
    fac.posbgfixedy = 840
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
    backtomenured = bob.buildtxtrender("Back to Menu", 0, red)

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
    matrizEnemigos1=recortarEne1('enemy.png')

    enemigo=Enemigo1(matrizEnemigos1)
    enemigos.add(enemigo)
    todos.add(enemigo)


    reloj=pygame.time.Clock()

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

    pausexpos = fac._screensize[0]/2
    pauseypos = fac._screensize[1]/2 - pauseheight
    xpos = pausexpos
    ypos = pauseypos + pauserender.get_height() + 10
    for x in pauseoptionrenders:
        pausepositions.append((pausexpos-x.get_width()/2, ypos))
        ypos += x.get_height() + 10
    fac.pausepositions = pausepositions
    blink = False
    time = pygame.time.get_ticks()
    turn = False
    modlist = []
    random.seed(pygame.time.get_ticks())
    time2 = pygame.time.get_ticks()
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
                        blink = True
                        time = pygame.time.get_ticks()
                        lasttime = pygame.time.get_ticks()
                    if event.key == pygame.K_RIGHT:
                        modi += 1
                        blink = True
                        time = pygame.time.get_ticks()
                        lasttime = pygame.time.get_ticks()
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

            elif state == menuoptions[1] or state == menuoptions[0]:

                #print 'Jugador:', jugador.rect.x, jugador.rect.y
                #print 'Fondo:',posbg
                #Gestion de limites------------------------------------------------------
                if event.type == pygame.KEYDOWN:

                    #ACOMODAR ESTE
                    '''
                    if posbg[1]<=-432:
                        if jugador.rect.y<=342:
                            jugador.downlimit_y+=6

                            posbg[1]+=12
                    '''

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
                    if state == menuoptions[1]:
                        if event.key in allowedmoves2:
                            moves2.insert(0,event.key)
                        if moves2 != []:
                            jugador2.move(moves2[0])

                if event.type == pygame.KEYUP:
                    if event.key in allowedmoves:
                        moves.remove(event.key)
                    jugador.soltartecla()
                    if moves != []:
                        jugador.move(moves[0])
                    if state == menuoptions[1]:
                        if event.key in allowedmoves2:
                            moves2.remove(event.key)
                        jugador2.soltartecla()
                        if moves2 != []:
                            jugador2.move(moves2[0])
        mousepos = pygame.mouse.get_pos()
        mouseonoption = fac.checkmouse(mousepos)
        if state == 'menu':
            if blink:
                if pygame.time.get_ticks()-lasttime >= 200:
                    turn = not turn
                    lasttime = pygame.time.get_ticks()
                    if turn:
                        m.kill()
                    else:
                        modifiers.add(m)
                        everyone.add(m)
                elif pygame.time.get_ticks() - time >= 2000:
                    blink = not blink
                    modifiers.add(m)
                    everyone.add(m)
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
            if state == menuoptions[0]:
                jugador=Jugador(matrizJugador)
                jugadores.add(jugador)
                todos.add(jugador)
            elif state == menuoptions[1]:
                jugador=Jugador(matrizJugador)
                jugadores.add(jugador)
                todos.add(jugador)
                jugador2=Jugador2(matrizJugador2)
                jugadores.add(jugador2)
                todos.add(jugador2)



        if state == menuoptions[0] or state ==  menuoptions[1]:

            if not fac.pause:
                if pygame.time.get_ticks() - time >= random.randrange(10000,20000) and (len(modlist)<=3):
                    m = fac.getModifier(random.randrange(0,4))
                    m.rect.x = random.randrange(0,fac._screensize[0]-100)
                    m.rect.y = random.randrange((fac.posbg[1] + fac.posbgfixedy), fac._screensize[1]-100)
                    blink = True
                    lasttime = pygame.time.get_ticks()
                    time = pygame.time.get_ticks()
                    modifiers.add(m)
                    todos.add(m)
                    modlist.append(m)
                elif pygame.time.get_ticks() - time2 >= 20000:
                    time2 = pygame.time.get_ticks()
                    if modlist != []:
                        modlist[0].kill()
                        modlist.pop(0)
                if blink:
                    if pygame.time.get_ticks()-lasttime >= 200:
                        turn = not turn
                        lasttime = pygame.time.get_ticks()
                        if turn:
                            m.kill()
                        else:
                            modifiers.add(m)
                            todos.add(m)
                    elif pygame.time.get_ticks() - time >= 2000:
                        blink = not blink
                        modifiers.add(m)
                        todos.add(m)
                todos.update()

                if jugador.rect.y + jugador.rect.height < fac.posbgfixedy + fac.posbg[1]:
                    jugador.rect.y = fac.posbgfixedy + fac.posbg[1] - jugador.rect.height
                if state == menuoptions[1]:
                    if jugador2.rect.y + jugador2.rect.height < fac.posbgfixedy + fac.posbg[1]:
                        jugador2.rect.y = fac.posbgfixedy + fac.posbg[1] - jugador2.rect.height
                if moves != []:
                    fac.checklimits(moves[0],jugador, bginfo)
                if moves2 != []:
                    fac.checklimits(moves2[0],jugador2, bginfo)
                screen.fill([0,0,0])
                screen.blit(fondo,[0,-50])
                screen.blit(gamebckg, fac.posbg)

                todos.draw(screen)
                fac.drawLife(jugador.getHealth())
                pygame.display.flip()
                reloj.tick(10)

            #if state == menuoptions[2]:

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
                if pauseoptions[select] == "Back to Menu" and mouseclick and select != -1:
                    state = 'menu'
                    for x in jugadores:
                        x.kill()
                    mouseclick = False
                    fac.pause = False
        elif state == menuoptions[2]:
            newbckpos =   [850, 650]
            screen.fill([0,0,0])
            fac.display_bkg()
            #screen.blit(menubckg2, [100, 0])
            screen.blit(player1,[10,0])
            screen.blit(player2,[10,400])
            screen.blit(fac._pauserenders[0], newbckpos)

            select = fac.checkmousepause(mousepos, newbckpos)

            if select != -1:
                txt = pauseoptions[select]
                fac._pauserenders.pop(select)
                fac._pauserenders.insert(select,backtomenured)
                fac._turnedoptions.append(select)
            elif select == -1 and fac.getTurned() != []:
                fac._pauserenders = fac._normalpauserenders[:]
                fac.emptyTurned()
            elif len(fac.getTurned())> 1:
                txt = pauseoptions[select]
                fac._pauserenders = fac._normalpauserenders[:]
                fac._pauserenders.pop(select)
                fac._pauserenders.insert(select,backtomenured)
                fac._turnedoptions.append(select)
            if pauseoptions[select] == "Back to Menu" and mouseclick and select!= -1:
                state = 'menu'
            #screen.blit(x,[750, 350])
            #select = fac.checkmousepause(mousepos)
        elif state == 'Salir':
            end = True
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
