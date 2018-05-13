import pygame
import time
import random
from wolvbasics import *
from jugador import *
from enemigo import *
from operator import attrgetter

red = (255,0,0)         #rgb(255,0,0)
green = (0,255,0)       #rgb(0,255,0)
blue = (0,0,255)        #rgb(0,0,255)
darkBlue = (0,0,128)    #rgb(0,0,128)
yellow =(255,255,51)    #rgb(255,255,51)
white = (255,255,255)   #rgb(255,255,255)
black = (0,0,0)         #rgb(0,0,0)
pink = (255,200,200) #rgb(255,200,200)
posbg = [0, -840]

beep=pygame.mixer.Sound('beep.ogg')
pygame.mixer.music.load('titlescreen.ogg')
pygame.mixer.music.set_volume(0.5)
level1=pygame.mixer.Sound('level1.ogg')
pygame.mixer.music.play()
channel1 = pygame.mixer.Channel(0)
channel1.set_volume(0)
channel1.play(level1, -1)
def printkey(key):
    if key == pygame.K_LEFT:
        print "Left"
    elif key == pygame.K_RIGHT:
        print "Right"

def main():

    pygame.init()
    pygame.font.init()
    bob = Builder(pygame.font.Font('WolverineFont.ttf', 40), pygame.font.Font('WolverineFont.ttf', 60), pygame.font.Font('WolverineFont.ttf', 15))
    screen = bob.buildscreen()
    menubckg = pygame.image.load('menu.png').convert_alpha()
    gamebckg = pygame.image.load('bg.png').convert_alpha()
    bginfo = [gamebckg.get_rect()[2],gamebckg.get_rect()[3]]
    fondo = pygame.image.load('fondo.png').convert_alpha()
    player1 = pygame.image.load('jugador1.png').convert_alpha()
    player1=pygame.transform.scale(player1, (750, 350))
    player2 = pygame.image.load('jugador2.png').convert_alpha()
    player2=pygame.transform.scale(player2, (750, 350))
    wolvieface = pygame.image.load('WolverineFace.png').convert_alpha()
    wolvieface = pygame.transform.scale(wolvieface, (40,40))
    wolvieface2 = pygame.image.load('WolverineFace2.png').convert_alpha()
    wolvieface2= pygame.transform.scale(wolvieface2, (40,40))
    menuoptions = ["1 Jugador", "2 Jugadores", "Instrucciones", "Salir"]
    pauseoptions = ["Back to Menu"]
    pauserender = bob.buildtxtrender("PAUSE", 1, white)
    pauseoptionrenders = bob.buildtxtrenders(pauseoptions, 0, white)
    menurenders = bob.buildtxtrenders(menuoptions)
    WolverineTitle = bob.buildtxtrender("Wolverine", 1)
    end = False
    fac = Facade(screen, menurenders, WolverineTitle, [250,200], menubckg, [-550,0], wolvieface, wolvieface2)
    fac._screensize = bob.buildresolution()
    posbg[1] += fac._screensize[1]-200
    fac.posbg = posbg[:]
    fac.prevposbg = posbg[:]
    fac.defaultposbg = posbg[:]
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

    wolverine=pygame.image.load('wolverine_sprites.png').convert_alpha()
    infoWolverine=wolverine.get_rect()

    wolverine2=pygame.image.load('wolverine_sprites2.png').convert_alpha()
    infoWolverine2=wolverine2.get_rect()

    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    enemigos2=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    matrizJugador=[]
    #matrizJugador2=[]
    matrizJugador=recortar('wolverine_sprites.png')
    matrizJugador2=recortar('wolverine_sprites2.png')
    matrizEnemigos1=recortarEne1('enemy.png')
    matrizEnemigos2=recortarEne2('enemigoMovil.png')
    matrizBala=recortarBala('lasers.png')
    '''
    enemigo=Enemigo1(matrizEnemigos1)
    enemigos.add(enemigo)
    todos.add(enemigo)

    enemigo2=Enemigo2(matrizEnemigos2)
    enemigos.add(enemigo2)
    todos.add(enemigo2)

    bala=Bala(matrizBala)
    bala.rect.y=enemigo.rect.y+enemigo.rect.height/2
    bala.rect.x=enemigo.rect.width+50
    balas.add(bala)
    todos.add(bala)
    '''


    reloj=pygame.time.Clock()
    generator1=True
    generator2=True
    numberOfMovingEnemies=5
    numberOfStillEnemies=2

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
    playermodlist = {}
    random.seed(pygame.time.get_ticks())
    time2 = pygame.time.get_ticks()
    score = bob.buildscorerender("score")
    endscore = 10000
    genscore = 0
    winrender = bob.buildtxtrender("Congratulations", 1, white)
    loserender = bob.buildtxtrender("GAME OVER", 1, red)
    gameover = False
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
                pygame.mixer.music.set_volume(0.3)
                channel1.set_volume(0)
                '''
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
                '''
            elif state == menuoptions[1] or state == menuoptions[0]:
                pygame.mixer.music.set_volume(0)
                channel1.set_volume(0.3)
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
                #print "Menu Option Clicked: ", menuoptions[mouseonoption]
                mouseclick = False
                state = menuoptions[mouseonoption]
                if mouseonoption == 0:
                    modwait = 15000
                else:
                    modwait = 10000
            if mouseonoption != -1 and mouseonoption not in fac.getTurned():
                #Turns blue the option the mouse is on
                txt = menuoptions[mouseonoption]
                fac.appendTurned(mouseonoption)
                newrender = bob.buildtxtrender(txt, 0, white)
                fac.popmenurenders(mouseonoption)
                fac.insertmenurenders(mouseonoption, newrender)
                beep.play()
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
            #1 Player
            if state == menuoptions[0]:
                genscore=0
                jugador=Jugador(matrizJugador)
                jugadores.add(jugador)
                todos.add(jugador)
            #2 players
            elif state == menuoptions[1]:
                genscore=0
                jugador=Jugador(matrizJugador)
                jugadores.add(jugador)
                todos.add(jugador)
                jugador2=Jugador2(matrizJugador2)
                jugadores.add(jugador2)
                todos.add(jugador2)



        if state == menuoptions[0] or state ==  menuoptions[1]:

            if genscore >= endscore:
                for j in jugadores:
                    j.kill()
                winrenderrect = winrender.get_rect()
                winrenderpos = [RESOLUTION[0]/2 - winrenderrect.width/2,RESOLUTION[1]/2 - winrenderrect.height]
                newbckpos = [RESOLUTION[0]/2 - fac._pauserenders[0].get_rect().width/2]
                newbckpos.append(RESOLUTION[1]/2 + winrenderrect.height + 50)


                screen.blit(winrender, winrenderpos )
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
            elif gameover:
                loserenderrect = loserender.get_rect()
                loserenderpos = [RESOLUTION[0]/2 - loserenderrect.width/2,RESOLUTION[1]/2 - loserenderrect.height]
                newbckpos = [RESOLUTION[0]/2 - fac._pauserenders[0].get_rect().width/2]
                newbckpos.append(RESOLUTION[1]/2 + loserenderrect.height + 50)


                screen.blit(loserender, loserenderpos )
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
                    gameover = False
            elif not fac.pause:
                if fac.posbg[0]==0 or fac.posbg[0]==-220 or fac.posbg[0]==-320 or fac.posbg[0]==-520 or fac.posbg[0]==-660 or fac.posbg[0]==-990:

                    if numberOfMovingEnemies==0:
                        #generator1=True
                        generator2=True
                    for i in range(numberOfMovingEnemies):
                        if generator2:
                            enemy2=Enemigo2(matrizEnemigos2)
                            enemy2.rect.x=random.randrange(0, 900, 30)
                            enemigos2.add(enemy2)
                            todos.add(enemy2)
                    generator2=False

                    for i in range(numberOfStillEnemies):
                        if generator1:
                            enemy=Enemigo1(matrizEnemigos1)
                            enemy.rect.y=random.randrange(500, 700)
                            enemigos.add(enemy)
                            todos.add(enemy)
                    generator1=False
                '''
                if fac.posbg[0]==-220:
                    numberOfMovingEnemies=5
                    numberOfStillEnemies=2
                elif fac.posbg[0]==-320:
                    numberOfMovingEnemies=5
                    numberOfStillEnemies=2
                elif fac.posbg[0]==-660:
                    numberOfMovingEnemies=5
                    numberOfStillEnemies=2
                elif fac.posbg[0]==-990:
                    numberOfMovingEnemies=5
                    numberOfStillEnemies=2

                '''

                for x in jugadores:
                    lsmod = pygame.sprite.spritecollideany(x, modifiers)
                    if lsmod != None:
                        if not lsmod.blink:
                            if lsmod.type in playermodlist:
                                playermodlist.pop(lsmod.type)
                                playermodlist[lsmod.type] = [ pygame.time.get_ticks(), x]
                            else:
                                playermodlist[lsmod.type] = [ pygame.time.get_ticks(), x]
                            x.dealtwithModifiers(lsmod.type)
                            if lsmod.type in [1,3]:
                                x.score += 100
                                genscore += 100
                            else:
                                x.score -= 100
                                genscore -= 100
                            if x.score < 0:
                                x.score = 0
                            if genscore < 0:
                                genscore = 0
                            lsmod.kill()

                gottapop = []
                for x in playermodlist:
                    if pygame.time.get_ticks() - playermodlist[x][0] >= 10000:
                        playermodlist[x][1].resetValue(x)
                        gottapop.append(x)
                for x in gottapop:
                    playermodlist.pop(x)

                if pygame.time.get_ticks() - time >= random.randrange(modwait,modwait*2) and (len(modlist)<=3):
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
                        m.blink = False
                        modifiers.add(m)
                        todos.add(m)
                for x in enemigos2:
                    if state == menuoptions[0]:
                        x.AImove(jugador)
                    else:
                        x.AImove(jugador, jugador2,2)
                    jugadorlscol = pygame.sprite.spritecollide(x, jugadores, False)
                    for y in jugadorlscol:
                        damageinf = y.inflictDamage(x)
                        x._health -= damageinf
                        if damageinf > 0:
                            if x._health <= 0:
                                y.score += 200
                                genscore += 200
                                numberOfMovingEnemies-=1
                                x.die()
                                x.kill()
                            else:
                                y.score += 50
                                genscore += 50

                for x in jugadores:
                    enemylscol = pygame.sprite.spritecollide(x, enemigos2, False)
                    for y in enemylscol:
                        if y.isAttacking():
                            x.dealDamage(0.5)
                todos.update()


                if jugador.rect.y + jugador.rect.height < fac.posbgfixedy + fac.posbg[1]:
                    jugador.rect.y = fac.posbgfixedy + fac.posbg[1] - jugador.rect.height
                if state == menuoptions[1]:
                    if jugador.getHealth() + jugador2.getHealth() <= 0:
                        gameover = True
                    if jugador2.rect.y + jugador2.rect.height < fac.posbgfixedy + fac.posbg[1]:
                        jugador2.rect.y = fac.posbgfixedy + fac.posbg[1] - jugador2.rect.height
                else:
                    if jugador.getHealth() <= 0:
                        gameover = True
                if moves != []:
                    fac.checklimits(moves[0],jugador, bginfo)
                if moves2 != []:
                    fac.checklimits(moves2[0],jugador2, bginfo)
                if fac.prevposbg != fac.posbg:
                    fac.prevposbg[0] = fac.prevposbg[0] - fac.posbg[0]
                    fac.prevposbg[1] = fac.prevposbg[1] - fac.posbg[1]
                    for x in enemigos:
                        x.rect.x -= fac.prevposbg[0]
                        x.rect.y -= fac.prevposbg[1]
                    for x in enemigos2:
                        x.rect.x -= fac.prevposbg[0]
                        x.rect.y -= fac.prevposbg[1]
                    if state == menuoptions[1]:
                        if fac.isLimitrigger(moves[0], jugador, bginfo):
                            jugador2.rect.x -= fac.prevposbg[0]
                            jugador2.rect.y -= fac.prevposbg[1]
                        elif  fac.isLimitrigger(moves[0], jugador, bginfo):
                            jugador.rect.x -= fac.prevposbg[0]
                            jugador.rect.y -= fac.prevposbg[1]
                    fac.prevposbg = fac.posbg[:]
                screen.fill([0,0,0])
                screen.blit(fondo,[0,-50])
                screen.blit(gamebckg, fac.posbg)

                drawlist = []
                for x in todos:
                    drawlist.append(x)
                drawlist.sort(key = attrgetter('rect.y'))
                drawgroup = pygame.sprite.Group()
                for x in drawlist:
                    drawgroup.add(x)
                    drawgroup.draw(screen)
                    drawgroup.remove(x)
                #todos.draw(screen)

                scorerender1 = bob.buildscorerender(str(jugador.score))
                if state == menuoptions[0]:
                    fac.drawLife(jugador.getHealth())
                    fac.drawScore(scorerender1, scorerender = score)
                else:
                    scorerender2 = bob.buildscorerender(str(jugador2.score))
                    fac.drawScore(scorerender1, score, 2,scorerender2)
                    fac.drawLife(jugador.getHealth(), 2, jugador2.getHealth())

                pygame.display.flip()
                reloj.tick(10)

            else:
                screen.blit(pauserender, [pausexpos- pausewidth,pauseypos])
                i = 0
                for x in fac._pauserenders:
                    screen.blit(x,fac.pausepositions[i])
                    i += 1
                select = fac.checkmousepause(mousepos)

                if select != -1 and len(fac.getTurned())<1:
                    beep.play()

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
                    fac.resetposbg()
                    for x in jugadores:
                        x.kill()
                    mouseclick = False
                    fac.pause = False

        #Opcion no jugable
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
