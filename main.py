import pygame

red = (255,0,0)         #rgb(255,0,0)
green = (0,255,0)       #rgb(0,255,0)
blue = (0,0,255)        #rgb(0,0,255)
darkBlue = (0,0,128)    #rgb(0,0,128)
yellow =(255,255,51)    #rgb(255,255,51)
white = (255,255,255)   #rgb(255,255,255)
black = (0,0,0)         #rgb(0,0,0)
pink = (255,200,200) #rgb(255,200,200)

RESOLUTION = [1920, 1080]
class Facade(object):
    def __init__(self, screen, menurenders, Wolverine, initialposition):
        self.normalrenders = menurenders[:]
        self.menurenders = menurenders
        self.Wolverine = Wolverine
        self.screen = screen
        self.initialposition = initialposition
        self.display_info = []
        self.turnedoptions = []
    def display_menu(self):
        self.display_Wolverine()
        i = 0
        info = self.menurenders[0].get_rect()
        space = info.height + 10
        for x in self.menurenders:
            self.screen.blit(x,[self.initialposition[0], self.initialposition[1] + i * space])
            info = x.get_rect()
            xinfo = [self.initialposition[0], self.initialposition[1] + i * space, x.get_width(), x.get_height()]
            i += 1
            if xinfo not in self.display_info:
                self.display_info.append(xinfo)

    def display_Wolverine(self):
        self.screen.blit(self.Wolverine, [self.initialposition[0], self.initialposition[1] - 100])
    def checkmouse(self, mousepos):
        for x in self.display_info:
            if mousepos[0] >= x[0] and mousepos[0]<= x[0]+x[2] and mousepos[1] >= x[1] and mousepos[1] <= x[1]+x[3]:
                return self.display_info.index(x)
        return -1

def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode()
    font = pygame.font.Font('WolverineFont.ttf', 60)
    WolverineTitle = font.render("Wolverine", True, black)
    font = pygame.font.Font('WolverineFont.ttf', 40)
    menubckg = pygame.image.load('menu.png')
    menuoptions = ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"]
    menurenders = []
    for x in menuoptions:
        menurenders.append(font.render(x,True, black))

    end = False
    initialposition = [250,200]
    screen.blit(menubckg,[-651,0])

    fac = Facade(screen, menurenders, WolverineTitle, initialposition)
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
            newrender = font.render(txt, True, darkBlue)
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
