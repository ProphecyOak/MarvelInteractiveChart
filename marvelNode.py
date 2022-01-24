class marvelNode():
    num = 0
    lines = []
    def __init__(self,bin=0,name='Unnamed',type='Event',main='Avengers',time='none',prevalence=0):
        marvelNode.num += 1
        self.x = marvelNode.num
        self.time = time
        self.bin = bin
        self.name = name
        self.type = type
        self.line = main
        if not self.line in marvelNode.lines:
            marvelNode.lines.append(self.line)
        self.height = marvelNode.lines.index(self.line)
        self.prevalence = prevalence

    def getCoords(self):
        return(self.x,self.y)
    def __str__(self):
        return("%s. %s: %s" % (self.x,self.type,self.name))
