from visual.screen import screen
from fractals.mandlebrot import mandlebrot
import Image

class FrameCreator:
    
    def __init__(self, matrix_size):
        self.matrix_size = matrix_size
            
    def createFrame(self, z_zoom_modifier, y_zoom_modifier, depth):
        s = screen()
        image = Image.new("RGB", (self.matrix_size, self.matrix_size))

        for row in s.matrix:
            for cell in row:        
                m = mandlebrot(z_zoom_modifier, y_zoom_modifier)
                if m.inSet(cell, depth):
                    image.putpixel(
                        (cell.x, cell.y), 
                        (
                         cell.getColor() % 4 * 64, 
                         cell.getColor() % 8 * 32, 
                         cell.getColor() % 16 * 16
                         )
                    )
        return image 
