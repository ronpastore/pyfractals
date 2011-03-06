
from pyglet import window
from pyglet import clock
from pyglet import font
from pyglet import resource
import config
class ZoomerWindow(window.Window):

    def __init__(self, *args, **kwargs):
        window.Window.__init__(self, *args, **kwargs)
        #set size
        #self.set_size(int(config.MATRIX_SIZE), int(config.MATRIX_SIZE))
    
    def on_mouse_release(self, x, y, button, modifiers):
        print 'The left mouse button was pressed.'
        
    def main_loop(self):
        
        
        self.push_handlers(window.event.WindowEventLogger())
        
        image = resource.image("mandel.png")
        instructions_text = font.Text(
          font.load('Arial', 12), 
          y=10
        )

        while not self.has_exit:
            self.dispatch_events()
            self.clear()

            
            image.blit(0,0)
            
            instructions_text.text = ("Welcome, click a point to begin your fractal journey")
            instructions_text.draw()
            
            
            self.flip()

if __name__ == "__main__":

    
    # Someone is launching this directly
    app = ZoomerWindow()
    app.main_loop()
    
    
    
