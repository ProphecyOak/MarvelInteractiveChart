class marvelLine():
    num = 0
    lines = {}
    def __init__(self, eventA, eventB):
        self.startPoint = eventA
        self.endPoint = eventB
        self.x1=eventA.x
        self.x2=eventB.x
        self.y1=eventA.height
        self.y2=eventB.height
        marvelLine.num += 1
        self.num = marvelLine.num
        marvelLine.lines[eventA.name+eventB.name] = self
        self.characters = []

    def updatePoints(self):
        self.x1=self.startPoint.x
        self.x2=self.endPoint.x
        self.y1=self.startPoint.line
        self.y2=self.endPoint.line

    def crosses(self,other):
        if self.startPoint in [other.startPoint,other.endPoint] or self.endPoint in [other.startPoint,other.endPoint]:
            return 0
        mA = (self.y2-self.y1)/(self.x2-self.x1)
        mB = (other.y2-other.y1)/(other.x2-other.x1)
        bA = self.y1-mA*self.x1
        bB = other.y1-mB*other.x1
        if mA == mB or bA == bB:
            return 0
        xI = (bB-bA)/(mA-mB)
        if xI > max(self.x1,other.x1) and xI < min(self.x2,other.x2):
            return 1
        else:
            return 0   #####THIS DOESNT WORK AT ALL

    def __str__(self):
        return("%s. From '%s' to '%s'\nWith %s\n" % (self.num, self.startPoint.name, self.endPoint.name,", ".join(map(str,self.characters))))
