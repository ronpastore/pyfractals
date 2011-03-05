
from pyglet import window
from pyglet import clock
from pyglet import font


class ZoomerWindow(window.Window):

    def __init__(self, *args, **kwargs):

        #Let all of the standard stuff pass through
        window.Window.__init__(self, *args, **kwargs)

   
    
    def main_loop(self):
        
        instructions_text = font.Text(
          font.load('Arial', 28), 
          y=10
        )

        while not self.has_exit:
            self.dispatch_events()
            self.clear()

            instructions_text.text = ("Welcome, click a point to begin your fractal journey")
            instructions_text.draw()

            self.flip()

if __name__ == "__main__":
    # Someone is launching this directly
    app = ZoomerWindow()
    app.main_loop()

@app.event
def on_mouse_press(x, y, button, modifiers):
    print 'The left mouse button was pressed.'
