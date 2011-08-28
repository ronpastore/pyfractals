
from matrix.scale import scale

class mandlebrot: 

    def __init__(self, x_zoom_modifier, y_zoom_modifier):
        self.x_zoom_modifier = x_zoom_modifier
        self.y_zoom_modifier = y_zoom_modifier
        self.iteration = 0
        
    def inSet(self,cell, depth):   
        x0 = scale( cell.x, "X", self.x_zoom_modifier)
        y0 = scale(cell.y, "Y", self.y_zoom_modifier)

        x = 0.0
        y = 0.0
        
        #reset iteration
        self.iteration = 0


        while ( x*x + y*y <= (2.0*2.0)  and  self.iteration < depth ):
            xtemp = x*x - y*y + x0
            y = 2.0*x*y + y0
            x = xtemp
            self.iteration = self.iteration + 1

        if ( self.iteration == depth ):
            return False
        else:
            return True
