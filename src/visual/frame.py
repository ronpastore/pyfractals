from config import MATRIX_SIZE

'''
Created on 11 Nov 2010

@author: Ron Pastore
'''
from matrix.cell import cell

class frame:

    def __init__(self):
        matrix_range = range(1,MATRIX_SIZE)
        self.matrix = [ [ cell(x,y) for x in matrix_range] for y in matrix_range]
        self.frame_number = None
        
    def setFrameNumber(self, frame_number):
        self.frame_number = frame_number
        
    def populateImage(self, image):
        for row in self.matrix:
            for cell in row:
                if not cell.getColor():
                    continue   
                image.putpixel(
                    (cell.x, cell.y), 
                    (
                     cell.getColor() % 4 * 64, 
                     cell.getColor() % 8 * 32, 
                     cell.getColor() % 16 * 16
                    )
                )
        
    
    """not quite working yet"""
    def getPixelSequence(self):
        seq=[]
        for row in self.matrix:
            for cell in row:
                seq.append(( 
                    cell.getColor() % 4 * 64,
                    cell.getColor() % 8 * 32, 
                    cell.getColor() % 16 * 16
                ))
                                
        return seq