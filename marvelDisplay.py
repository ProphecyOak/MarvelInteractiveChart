from marvelChart import*
import tkinter as tk

class marvelDisplay():
    lineSeperation = 35
    dotWidth = 4
    xSeperation = 13
    xBuffer = 25
    yBuffer = 25
    def __init__(self):
        self.chart = marvelChart('InputData/Order.csv', 'InputData/EdgeList.csv')
        self.master = tk.Tk()
        self.resetButton = tk.Button(self.master,text='Refresh',command=self.resetChart)
        self.resetButton.pack()
        self.can = tk.Canvas(self.master,width=1500,height=750)
        self.can.pack()
        self.resetChart()
        self.master.update()
        self.chart.checkIntersections()

    def plotPoints(self):
        for x in self.chart.events:
            self.can.create_oval(x.x*marvelDisplay.xSeperation+marvelDisplay.xBuffer-marvelDisplay.dotWidth,
                                 x.height*marvelDisplay.lineSeperation+marvelDisplay.yBuffer-marvelDisplay.dotWidth,
                                 x.x*marvelDisplay.xSeperation+marvelDisplay.xBuffer+marvelDisplay.dotWidth,
                                 x.height*marvelDisplay.lineSeperation+marvelDisplay.yBuffer+marvelDisplay.dotWidth)
    def plotLines(self):
        for x in marvelLine.lines.values():
            self.can.create_line(x.startPoint.x*marvelDisplay.xSeperation+marvelDisplay.xBuffer+marvelDisplay.dotWidth,
                                 x.startPoint.height*marvelDisplay.lineSeperation+marvelDisplay.yBuffer,
                                 x.endPoint.x*marvelDisplay.xSeperation+marvelDisplay.xBuffer-marvelDisplay.dotWidth,
                                 x.endPoint.height*marvelDisplay.lineSeperation+marvelDisplay.yBuffer)

    def resetChart(self):
        self.can.destroy()
        self.can = tk.Canvas(self.master,width=1500,height=750)
        self.can.pack()
        self.chart.reorderEvents()
        self.plotLines()
        self.plotPoints()
        self.master.update()

a = marvelDisplay()

a.master.mainloop()
