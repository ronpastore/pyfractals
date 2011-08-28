from visual.frame import frame
from fractals.mandlebrot import mandlebrot


class FrameCreator:
    
    def __init__(self, matrix_size):
        self.matrix_size = matrix_size
            
    def createFrame(self, z_zoom_modifier, y_zoom_modifier, depth):
        f = frame()
        for row in f.matrix:
            for cell in row:        
                m = mandlebrot(z_zoom_modifier, y_zoom_modifier)
                if m.inSet(cell, depth):
                    cell.setColor(m.iteration)                    
                    
                    
        return f 
