import pygame
from wolvbasics import *
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
    bob = Builder(pygame.font.Font('WolverineFont.ttf', 40), pygame.font.Font('WolverineFont.ttf', 60))
    screen = bob.buildscreen()
    menubckg = pygame.image.load('menu.png')
    menuoptions = ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"]
    menurenders = bob.buildtxtrenders(menuoptions)
    WolverineTitle = bob.buildtxtrender("Wolverine", 1)
    end = False
    fac = Facade(screen, menurenders, WolverineTitle, [250,200], menubckg, [-651,0])
    fac.display_bkg()
    mouseclick = False
    fac.display_menu()

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
        mousepos = pygame.mouse.get_pos()
        mouseonoption = fac.checkmouse(mousepos)

        if mouseonoption != -1 and mouseclick: #Detecting Option Clicked
            print "Menu Option Clicked: ", menuoptions[mouseonoption]
            mouseclick = False
        if mouseonoption != -1 and mouseonoption not in fac.turnedoptions:
            #Turns blue the option the mouse is on
            txt = menuoptions[mouseonoption]
            fac.turnedoptions.append(mouseonoption)
            newrender = bob.buildtxtrender(txt, 0, darkBlue)
            fac.menurenders.pop(mouseonoption)
            fac.menurenders.insert(mouseonoption, newrender)
            screen.fill(black)
            screen.blit(menubckg,[-651,0])
            fac.display_menu()
        elif fac.turnedoptions != [] and mouseonoption == -1:
            #Returns all text to normal colors
            fac.turnedoptions = []
            fac.menurenders = fac.normalrenders[:]
            screen.fill(black)
            screen.blit(menubckg,[-651,0])
            fac.display_menu()
    pygame.quit()

if __name__ == '__main__':
    main()
