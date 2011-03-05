
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


"""
image_frames = ["images/%s.png" % x for x in range(1,54)]

# Create the list of pyglet images
images = map(lambda img: pyglet.image.load(img),
      image_frames)

animation = pyglet.image.Animation.from_image_sequence(
       images, 0.13)

animSprite = pyglet.sprite.Sprite(animation)

 # The main pyglet window with OpenGL context
w = animSprite.width
h = animSprite.height
win = pyglet.window.Window(width=w, height=h)

 # Set window background color to white.
pyglet.gl.glClearColor(1, 1, 1, 1)

@win.event
def on_draw():
    win.clear()
    animSprite.draw()



pyglet.app.run()

"""