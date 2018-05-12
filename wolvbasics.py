import pygame

red = (255,0,0)         #rgb(255,0,0)
green = (0,255,0)       #rgb(0,255,0)
blue = (0,0,255)        #rgb(0,0,255)
darkBlue = (0,0,128)    #rgb(0,0,128)
yellow =(255,255,51)    #rgb(255,255,51)
white = (255,255,255)   #rgb(255,255,255)
black = (0,0,0)         #rgb(0,0,0)
pink = (255,200,200) #rgb(255,200,200)c

class Modifier(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

class Facade(object):
    def __init__(self, screen, menurenders, Wolverine, initialposition, bckg, bckgpos):
        self._normalrenders = menurenders[:]
        self._menurenders = menurenders
        self._Wolverine = Wolverine
        self._screen = screen
        self._initialposition = initialposition
        self._display_info = []
        self._turnedoptions = []
        self._bckg = bckg
        self._bckgpos = bckgpos
        self._modifiers = []
        self.pause = False
        self._screensize = pygame.display.Info()
        self._lifepos = [70, 20]
        self._healthheight = 40
        self._pauserenders = []
        self._normalpauserenders = []
        self.pausepositions = []

    def drawLife(self, health):
        rect = [self._lifepos[0], self._lifepos[1], 302 , self._healthheight]
        rect2 = [self._lifepos[0] + 1, self._lifepos[1] + 1, health*3, self._healthheight-2]
        pygame.draw.rect(self._screen, blue,rect, 1)
        pygame.draw.rect(self._screen, red,rect2)
    def loadmodifiers(self, path, quantity = 4):
        image = pygame.image.load(path).convert_alpha()
        imageinfo = image.get_rect()
        xwidth = imageinfo[2]/quantity
        self._modifiers = []
        for x in range(quantity):
            subsquare = image.subsurface(x * xwidth, 0, xwidth, imageinfo[3])
            subsquare = pygame.transform.scale(subsquare,[75,75])
            self._modifiers.append(subsquare)
    def setPauserenders(self, pauserenders):
        self._pauserenders = pauserenders
        self._normalpauserenders = pauserenders[:]
    def getModifier(self, i):
        if i < len(self._modifiers):
            m = Modifier(self._modifiers[i])
            return m
        else:
            return -1
    def getModifiers(self):
        return self._modifiers
    def getTurned(self):
        return self._turnedoptions
    def appendTurned(self,objt):
        self._turnedoptions.append(objt)
    def popmenurenders(self, popindex):
        self._menurenders.pop(popindex)
    def insertmenurenders(self,insertindex, element):
        self._menurenders.insert(insertindex, element)
    def emptyTurned(self):
        self._turnedoptions = []
    def resetmenurenders(self):
        self._menurenders = self._normalrenders[:]
    def display_menu(self):
        self.display_Wolverine()
        i = 0
        info = self._menurenders[0].get_rect()
        space = info.height + 10
        for x in self._menurenders:
            self._screen.blit(x,[self._initialposition[0], self._initialposition[1] + i * space])
            info = x.get_rect()
            xinfo = [self._initialposition[0], self._initialposition[1] + i * space, x.get_width(), x.get_height()]
            i += 1
            if xinfo not in self._display_info:
                self._display_info.append(xinfo)

    def display_Wolverine(self):
        self._screen.blit(self._Wolverine, [self._initialposition[0], self._initialposition[1] - 100])
    def checkmouse(self, mousepos):
        for x in self._display_info:
            if mousepos[0] >= x[0] and mousepos[0]<= x[0]+x[2] and mousepos[1] >= x[1] and mousepos[1] <= x[1]+x[3]:
                return self._display_info.index(x)
        return -1
    def checkmousepause(self,mousepos, overwrite = None):
        i = 0
        for x in self._pauserenders:
            rect = x.get_rect()
            if overwrite == None:
                rect.x, rect.y = self.pausepositions[i][0], self.pausepositions[i][1]
            else:
                rect.x, rect.y = overwrite[0], overwrite[1]
            i += 1
            if rect.collidepoint(mousepos):
                return self._pauserenders.index(x)
        return -1

    def display_bkg(self):
        self._screen.blit(self._bckg, self._bckgpos)
    def checklimits(self, key, player, bginfo):
        bglimit = 150
        limit = 15

        if player.rect.x > self._screensize[0] - bglimit and key == pygame.K_RIGHT:
                if bginfo[0] + self.posbg[0] - self._screensize[0]  - limit >0:
                    self.posbg[0] -= limit
        if player.rect.x < limit and key == pygame.K_LEFT:
            if self.posbg[0]  + limit <0:
                    self.posbg[0] += limit
        if player.rect.y > self._screensize[1] - bglimit and key == pygame.K_DOWN:
                if bginfo[1] + self.posbg[1] - self._screensize[1]  - limit >0:
                    self.posbg[1] -= limit
        if player.rect.y + player.rect.height < self.posbgfixedy + self.posbg[1] + limit and key == pygame.K_UP:
            if self.posbg[1] + self.posbgfixedy + limit < self._screensize[1] - 200:
                    self.posbg[1] += limit
class Builder(object):
    def __init__(self, normalfont, titlefont):
        self._normalfont = normalfont
        self._titlefont = titlefont
    def buildscreen(self):
        self._screensize = pygame.display.Info()
        screen = pygame.display.set_mode([self._screensize.current_w,self._screensize.current_h])
        return screen
    def buildresolution(self):
        return (self._screensize.current_w, self._screensize.current_h)
    def buildtxtrenders(self, txtlist, fonttype = 0, colour = black):
        renders = []
        if fonttype == 0:
            for x in txtlist:
                renders.append(self._normalfont.render(x, True, colour))
        else:
            for x in txtlist:
                renders.append(self._titlefont.render(x, True, colour))
        return renders
    def buildtxtrender(self,txt, fonttype = 0, colour = black):
        if fonttype == 0:
            return self._normalfont.render(txt, True, colour)
        else:
            return self._titlefont.render(txt, True, colour)
