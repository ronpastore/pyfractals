
from matrix.scale import scale
from config import DEPTH

class mandlebrot: 

    def __init__(self, x_zoom_modifier, y_zoom_modifier):
        self.x_zoom_modifier = x_zoom_modifier
        self.y_zoom_modifier = y_zoom_modifier

    def inSet(self,cell):   
        x0 = scale( cell.x, "X", self.x_zoom_modifier)
        y0 = scale(cell.y, "Y", self.y_zoom_modifier)

        x = 0.0
        y = 0.0

        iteration = 0
        max_iteration = 50

        global DEPTH

        while ( x*x + y*y <= (2.0*2.0)  and  iteration < DEPTH ):
            xtemp = x*x - y*y + x0
            y = 2.0*x*y + y0
            x = xtemp
            iteration = iteration + 1

        if ( iteration == max_iteration ):
            return False
        else:
            cell.setColor(iteration)
            cell.setView(".")
            return True
