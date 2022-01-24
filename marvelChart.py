from marvelCharacter import *
from marvelNode import *
from marvelLine import *
import csv
from random import shuffle

class marvelChart():
    def __init__(self,N,C):
        self.makeEvents(N)
        self.makeCharacters(C)
    def makeCharacters(self,C):
        self.characters = []
        self.charactersByName = {}
        with open(C, newline='') as csvfile:
            edgeReader = csv.reader(csvfile, delimiter=',', quotechar='|')
            edgeList = []
            for row in edgeReader:
                edgeList.append(row)
        newChar = 0
        curChar = ''
        prevNode = None
        for x in edgeList:
            if x == []:
                newChar = 1
            elif newChar == 1:
                newChar = 0
                curChar = x[0]
                self.characters.append(marvelCharacter(name=curChar))
                self.charactersByName[curChar] = self.characters[-1]
                firstEdge = 1
            else:
                if firstEdge == 0:
                    self.charactersByName[curChar].addPath(self.eventsByName[prevNode],self.eventsByName[x[0]])
                    #print(len(self.charactersByName[curChar].paths))
                else:
                    firstEdge = 0
                prevNode = x[0]
    def makeEvents(self,N):
        self.events = []
        self.eventsByName = {}
        #Open File and add Characters to self.Characters
        with open(N, newline='') as csvfile:
            orderReader = csv.reader(csvfile, delimiter=',', quotechar='|')
            orderList = []
            for row in orderReader:
                orderList.append(row)
        binNames = []
        curBin = 0
        binTitle = 0
        for x in orderList:
            if x == []:
                binTitle = 1
                curBin += 1
            elif binTitle == 1:
                binNames.append(x[0])
                binTitle = 0
            else:
                curType = 'E'
                if len(x) > 4:
                    curType = x[-1]
                self.events.append(marvelNode(bin=curBin, name=x[1], type=curType, main=x[3], prevalence=x[0]))
                self.eventsByName[x[1]] = self.events[-1]
    def reorderEvents(self,means=0):
        if means == 0:
            shuffle(marvelNode.lines)
        for x in self.events:
            x.height = marvelNode.lines.index(x.line)

    def checkIntersections(self):
        x = 0
        while x < len(self.characters)-1:
            for y in range(x+1,len(self.characters)):
                for i in self.characters[x].paths:
                    for j in self.characters[y].paths:
                        if i.crosses(j):
                            print(i,j,'\n') ###THIS DOESNT WORK AT ALL
            x += 1

    def getEvents(self):
        return self.events
    def getCharacters(self):
        return self.characters

    def __str__(self):
        outStr = "Characters:\n"
        for x in self.characters:
            outStr += str(x) + "\n"
        outStr += "\nNodes:"
        for x in self.events:
            if x.prevalence == 'A':
                outStr += "\n" + str(x)
        return(outStr)
