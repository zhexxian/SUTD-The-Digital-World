class Triangle (object):
    
    def __init__(self, color = 'green', filled = True, side1 = 1.0, side2 = 1.0, side3=1.0):
        self.color = color
        self.filled = filled
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getColor(self):
        return self.color
    def setColor(self, hmm):
        self.color = hmm
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
        