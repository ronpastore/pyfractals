
class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setView(self, viewChar):
        self.viewChar = viewChar
        
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
                
    def getViewChar(self):
        return self.viewChar

