from marvelLine import*

class marvelCharacter():
    def __init__(self,name='Unnamed',color='#FFFFFF',icon='None'):
        self.name = name
        self.color = color
        self.icon = icon
        self.paths = []

    def addPath(self,eventA,eventB):
        c = [eventA,eventB]
        if eventA.x > eventB.x:
            c.reverse()
        d = c[0].name + c[1].name
        if d not in marvelLine.lines.keys():
            self.paths.append(marvelLine(c[0], c[1]))
        else:
            self.paths.append(marvelLine.lines[d])
        marvelLine.lines[d].characters.append(self)

    def assignColor(self,color):
        self.color = color
    def __str__(self):
        return("%s" % (self.name))
