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

def main():
    pygame.init()
    pygame.font.init()
    screensize = pygame.display.Info()
    RESOLUTION = [screensize.current_w,screensize.current_h]
    bob = Builder(pygame.font.Font('WolverineFont.ttf', 40), pygame.font.Font('WolverineFont.ttf', 60))
    screen = bob.buildscreen()
    menubckg = pygame.image.load('menu.png')
    menuoptions = ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"]
    pauserender =bob.buildtxtrender("PAUSE", 1, white)
    menurenders = bob.buildtxtrenders(menuoptions)
    WolverineTitle = bob.buildtxtrender("Wolverine", 1)
    end = False
    fac = Facade(screen, menurenders, WolverineTitle, [250,200], menubckg, [-550,0])
    fac.display_bkg()
    mouseclick = False
    fac.display_menu()
    fac.loadmodifiers('gamemodifiers.png')
    modi = 0

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
    #matrizJugador2=recortar('wolverine_sprites2.png')


    jugador=Jugador(matrizJugador)
    #jugador2=Jugador(matrizJugador2)

    jugadores.add(jugador)
    todos.add(jugador)

    #jugadores.add(jugador2)
    #todos.add(jugador2)

    reloj=pygame.time.Clock()


    screen.blit(jugador.f[0][0], [jugador.rect.x, jugador.rect.y])
    #screen.blit(jugador2.f[0][0], [jugador2.rect.x, jugador2.rect.y])
    pygame.draw.polygon(screen, [255,255,255], [[0,400], [ANCHO, 400]],2)
    pygame.display.flip()

    fin=False
    allowedmoves = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_w, pygame.K_q, pygame.K_SPACE]
    moves = []


    while not end:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        mouseclick = True
                if event.type == pygame.MOUSEBUTTONUP:
                        mouseclick = False
            elif state == 'opcion1':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        fac.pause = not fac.pause
                    if event.key in allowedmoves:
                        moves.insert(0,event.key)
                    if moves != []:
                        if moves[0] ==pygame.K_RIGHT:
                            jugador.derecha()
                        if moves[0] == pygame.K_LEFT:
                            jugador.izquierda()
                        if moves[0] == pygame.K_SPACE:
                            jugador.saltar()
                        if moves[0] == pygame.K_q:
                            jugador.teclaq()
                        if moves[0] == pygame.K_w:
                            jugador.teclaw()
                if event.type == pygame.KEYUP:
                    if event.key in allowedmoves:
                        moves.remove(event.key)
                    jugador.soltartecla()
        mousepos = pygame.mouse.get_pos()
        mouseonoption = fac.checkmouse(mousepos)
        if state == 'menu':
            if mouseonoption != -1 and mouseclick: #Detecting Option Clicked
                print "Menu Option Clicked: ", menuoptions[mouseonoption]
                mouseclick = False
                state = 'opcion1'
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
        if state == 'opcion1':
            if not fac.pause:
                todos.update()
                screen.fill([0,0,0])
                pygame.draw.polygon(screen, [255,255,255], [[0,320], [ANCHO, 320]],2)
                todos.draw(screen)
                pygame.display.flip()
                reloj.tick(10)
            else:
                xwidth = pauserender.get_width()/2
                ywidth = pauserender.get_height()/2
                screen.blit(pauserender, [RESOLUTION[0]/2 - xwidth,RESOLUTION[1]/2 - ywidth])
                pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
