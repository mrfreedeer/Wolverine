import pygame

red = (255,0,0)         #rgb(255,0,0)
green = (0,255,0)       #rgb(0,255,0)
blue = (0,0,255)        #rgb(0,0,255)
darkBlue = (0,0,128)    #rgb(0,0,128)
yellow =(255,255,51)    #rgb(255,255,51)
white = (255,255,255)   #rgb(255,255,255)
black = (0,0,0)         #rgb(0,0,0)
pink = (255,200,200) #rgb(255,200,200)c

class Facade(object):
    def __init__(self, screen, menurenders, Wolverine, initialposition, bckg, bckgpos):
        self.normalrenders = menurenders[:]
        self.menurenders = menurenders
        self.Wolverine = Wolverine
        self.screen = screen
        self.initialposition = initialposition
        self.display_info = []
        self.turnedoptions = []
        self.bckg = bckg
        self.bckgpos = bckgpos

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
    def display_bkg(self):
        self.screen.blit(self.bckg, self.bckgpos)

class Builder(object):
    def __init__(self, normalfont, titlefont):
        self.normalfont = normalfont
        self.titlefont = titlefont
    def buildscreen(self):
        return pygame.display.set_mode()
    def buildtxtrenders(self, txtlist, fonttype = 0, colour = black):
        renders = []
        if fonttype == 0:
            for x in txtlist:
                renders.append(self.normalfont.render(x, True, colour))
        else:
            for x in txtlist:
                renders.append(self.titlefont.render(x, True, colour))
        return renders
    def buildtxtrender(self,txt, fonttype = 0, colour = black):
        if fonttype == 0:
            return self.normalfont.render(txt, True, colour)
        else:
            return self.titlefont.render(txt, True, colour)
